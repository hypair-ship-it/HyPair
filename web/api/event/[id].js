// Vercel serverless function — link preview page for a shared event (/event/<id>).
//
// Before this, /event/:id redirected straight to the home page, so every shared event
// looked identical in WhatsApp/Facebook/iMessage. Now a chat app's preview robot gets
// this event's own Open Graph tags (name, date, city, a card image), and a real visitor
// is sent on to the existing "You've been invited" landing (/?ref=invite).
//
// Deliberately NOT an HTTP redirect for the robot: most robots follow 3xx and would then
// read the home page's generic tags. A meta refresh + script moves people instead.
//
// Installed apps never get here: /event/* is a Universal Link / App Link, so the phone
// hands the tap to the app before the browser is involved.
//
// A draft, hidden or unknown event gets a plain redirect to the landing page (the
// generic site card), exactly as before. No athlete data is read or shown.
//
// Redirected from /event/:id by vercel.json. `?v=...` on the link is ignored here; it
// only exists so a changed message (wave times, results) is a different URL to WhatsApp,
// which remembers previews per URL for days.

const { isEventId, fetchEvent, escapeHtml, whenWhere } = require('../_eventShare');

const LANDING = '/?ref=invite';

module.exports = async function handler(req, res) {
  const { id } = req.query;
  const ev = await fetchEvent(id);

  if (!ev) {
    res.setHeader('Cache-Control', 'public, s-maxage=60');
    res.writeHead(302, { Location: LANDING });
    res.end();
    return;
  }

  const title = escapeHtml(`${ev.name} — HyPair`);
  const formats = Array.isArray(ev.formats) && ev.formats.length ? ` Formats: ${ev.formats.join(', ')}.` : '';
  const description = escapeHtml(`${whenWhere(ev)}.${formats} Find your partner and sign up on HyPair.`);
  const pageUrl = `https://hypair.app/event/${encodeURIComponent(id)}`;
  const cardUrl = `https://hypair.app/api/event-card?id=${encodeURIComponent(id)}`;

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
<meta http-equiv="refresh" content="0;url=${LANDING}">
<style>body{background:#0F1318;color:#fff;font-family:sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;margin:0;}a{color:#F2D079;}</style>
</head>
<body>
<p>Taking you to HyPair… <a href="${LANDING}">Continue</a></p>
<script>window.location.replace('${LANDING}');</script>
</body>
</html>`);
};
