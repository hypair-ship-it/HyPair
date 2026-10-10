// Vercel serverless function — link preview page for a shared event (/event/<id>).
//
// Before this, /event/:id redirected straight to the home page, so every shared event
// looked identical in WhatsApp/Facebook/iMessage. Now a chat app's preview robot gets
// this event's own Open Graph tags (name, date, city, a card image), and a real visitor
// is sent on to the event invite page (/invite?e=<id>, web/invite.html), which names the event and says how to join.
//
// Deliberately NOT an HTTP redirect for the robot: most robots follow 3xx and would then
// read the home page's generic tags. A meta refresh + script moves people instead.
//
// Installed apps never get here: /event/* is a Universal Link / App Link, so the phone
// hands the tap to the app before the browser is involved.
//
// A draft, hidden or unknown event gets a plain redirect to the invite page without an event (the
// generic site card), exactly as before. No athlete data is read or shown.
//
// :id is the event's full id or its 6-character short code (hypair.app/event/K7M2QX).
// `?v=waves` marks the link a gym shares with its wave schedule: same event, but a different URL (chat apps cache
// a previewed link for days, so the earlier invite picture would otherwise stick) and a preview that says wave
// times are out. It only applies once the gym has actually shared the waves.
// Redirected from /event/:id by vercel.json. `?v=...` on the link is ignored here; it
// only exists so a changed message (wave times, results) is a different URL to WhatsApp,
// which remembers previews per URL for days.

const { isShortCode, fetchEvent, escapeHtml, whenWhere } = require('../_eventShare');

const LANDING = '/invite';   // the event invite page (web/invite.html); an event id is added as ?e=

module.exports = async function handler(req, res) {
  const { id, v } = req.query;
  const ev = await fetchEvent(id);

  if (!ev) {
    res.setHeader('Cache-Control', 'public, s-maxage=60');
    res.writeHead(302, { Location: LANDING });
    res.end();
    return;
  }

  // The landing page looks the event up again by id, to say which event the link was for. id is a
  // UUID taken from the database row, so it is safe in a URL and in the script below.
  const landing = `${LANDING}?e=${encodeURIComponent(ev.id)}`;
  const waves = v === 'waves' && ev.waves_published === true;
  const title = escapeHtml(waves ? `Wave times: ${ev.name} — HyPair` : `${ev.name} — HyPair`);
  const formats = Array.isArray(ev.formats) && ev.formats.length ? ` Formats: ${ev.formats.join(', ')}.` : '';
  const description = escapeHtml(waves
    ? `Wave times are out for ${ev.name}. ${whenWhere(ev)}. Find your wave in HyPair.`
    : `${whenWhere(ev)}.${formats} Find your partner and sign up on HyPair.`);
  // og:url keeps the ?v=waves tag: Facebook caches by this canonical address, so dropping it would bring back the old picture.
  const pageUrl = `https://hypair.app/event/${isShortCode(id) ? encodeURIComponent(id.toUpperCase()) : encodeURIComponent(id)}${waves ? '?v=waves' : ''}`;
  const cardUrl = `https://hypair.app/api/event-card?id=${encodeURIComponent(ev.id)}${waves ? '&v=waves' : ''}`;

  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  // Events change (date, name); keep previews fresh enough but protect the function from bursts.
  res.setHeader('Cache-Control', 'public, s-maxage=300, stale-while-revalidate=3600');
  res.status(200).end(`<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${title}</title>
<meta name="description" content="${description}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="HyPair">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${description}">
<meta property="og:image" content="${cardUrl}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="${pageUrl}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${title}">
<meta name="twitter:description" content="${description}">
<meta name="twitter:image" content="${cardUrl}">
<meta http-equiv="refresh" content="0;url=${escapeHtml(landing)}">
<style>body{background:#0F1318;color:#fff;font-family:sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;margin:0;}a{color:#F2D079;}</style>
</head>
<body>
<p>Taking you to HyPair… <a href="${escapeHtml(landing)}">Continue</a></p>
<script>window.location.replace('${landing}');</script>
</body>
</html>`);
};
