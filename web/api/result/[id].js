// Vercel serverless function — per-shared-result OG-tag page (Ref 155).
//
// Generated per-request, not a checked-in static file — this does NOT
// reopen the retired "dedicated static page per entity" decision (see
// HyPair/CLAUDE.md's SEO landing pages section). It exists purely so a
// shared race-result link gets a rich, result-specific preview when
// pasted into iMessage/WhatsApp/etc, instead of the site's generic
// homepage OG tags.
//
// Reads from HyPairApp's `public_race_results` view (migration
// 20260915130000_public_race_result_view.sql) — a narrow, anon-readable
// view exposing only event_name/race_date/division/total_time, never
// user_id or any name/bio field. That column list is the actual
// enforcement of "keep shared data minimal" — this function can't widen
// it by editing its own query.
//
// A crawler (link-preview bot) reads the OG tags straight out of this
// HTML response. A real visitor gets bounced onward via meta-refresh +
// a JS fallback — deliberately NOT an HTTP redirect, since most crawlers
// follow 3xx redirects and would then see the homepage's generic OG tags
// instead of this result's.

const SUPABASE_URL = 'https://lsxprzoxoarfakhxhoab.supabase.co';
const SUPABASE_PUBLIC_KEY = 'sb_publishable_9U61L_y4qyiXga9-VK0rFw_oaDrGmIT';

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

module.exports = async function handler(req, res) {
  const { id } = req.query;

  if (!id || typeof id !== 'string') {
    res.writeHead(302, { Location: '/' });
    res.end();
    return;
  }

  let result = null;
  try {
    const apiRes = await fetch(
      `${SUPABASE_URL}/rest/v1/public_race_results?id=eq.${encodeURIComponent(id)}&select=event_name,race_date,division,total_time`,
      { headers: { apikey: SUPABASE_PUBLIC_KEY, Authorization: `Bearer ${SUPABASE_PUBLIC_KEY}` } },
    );
    const rows = await apiRes.json();
    result = Array.isArray(rows) ? rows[0] : null;
  } catch (err) {
    console.log('[result page] fetch failed:', err.message);
  }

  if (!result) {
    res.writeHead(302, { Location: '/' });
    res.end();
    return;
  }

  const title = escapeHtml(result.event_name);
  const time = result.total_time ? ` — ${escapeHtml(result.total_time)}` : '';
  const description = `Just finished ${title}${time} on HyPair. Find your next race partner.`;
  const resultUrl = `https://hypair.app/api/result/${encodeURIComponent(id)}`;
  const cardUrl = `https://hypair.app/api/result/${encodeURIComponent(id)}/card.png`;

  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.status(200).end(`<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${title} — HyPair</title>
<meta property="og:type" content="website">
<meta property="og:title" content="${title}${time} — HyPair">
<meta property="og:description" content="${escapeHtml(description)}">
<meta property="og:image" content="${cardUrl}">
<meta property="og:url" content="${resultUrl}">
<meta name="twitter:card" content="summary_large_image">
<meta http-equiv="refresh" content="0;url=/">
<style>body{background:#0F1318;color:#fff;font-family:sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;margin:0;}a{color:#F2D079;}</style>
</head>
<body>
<p>Taking you to HyPair… <a href="/">Continue</a></p>
<script>window.location.replace('/');</script>
</body>
</html>`);
};
