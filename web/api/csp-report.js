// Vercel serverless function — CSP violation report sink.
//
// This is the ONE piece of backend infrastructure this static site has.
// It exists solely so the `report-uri` / `report-to` directives on the
// Content-Security-Policy header (see web/vercel.json) have somewhere to
// POST to. Browsers send violation reports here automatically — nothing
// on the page has to call this.
//
// Current behavior: validate + console.log the report, return 204.
// Logged output lands in Vercel's function invocation logs (Project ->
// Logs / `vercel logs`), which are short-retention and not searchable
// long-term. There is NO persistent store, alerting, or dedup here.
//
// Decision needed before relying on this for anything beyond occasional
// manual log-checking: wire these reports into a durable sink. Options,
// roughly in order of lift:
//   1. Point report-uri/report-to directly at an existing Sentry project's
//      security-header endpoint (Sentry already ingests CSP reports
//      natively) — HyPair already has a Sentry org for the app, so this
//      would reuse existing infra rather than create anything new, but it
//      needs a human to grab that project's DSN-derived security endpoint
//      URL from the Sentry dashboard.
//   2. Insert rows into a Supabase table via this function using a
//      restricted key — real backend logic, more to maintain.
//   3. A free third-party collector (e.g. report-uri.com) — requires
//      creating a new third-party account, which needs explicit sign-off.
// This function intentionally does none of those yet.

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    res.status(405).end();
    return;
  }

  let body = '';
  try {
    for await (const chunk of req) {
      body += chunk;
      // Hard cap so a malformed/huge report can't be used to abuse the function.
      if (body.length > 20000) break;
    }
    const parsed = body ? JSON.parse(body) : null;
    // Modern Reporting API sends an array of report objects; legacy
    // `report-uri` sends a single { "csp-report": {...} } object.
    console.log('[csp-report]', JSON.stringify(parsed));
  } catch (err) {
    console.log('[csp-report] failed to parse report body:', err.message);
  }

  // 204: browsers expect no content back for report endpoints.
  res.status(204).end();
}
