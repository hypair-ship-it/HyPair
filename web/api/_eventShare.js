// Shared helpers for the event link preview (api/event/[id].js) and its card image
// (api/event-card.js). Underscore prefix: Vercel does not turn this file into a route.
//
// Only reads what any logged-out visitor can already read: a LIVE event's name, date,
// start time, city and formats (policy events_public_read). Nothing about athletes,
// and nothing for draft or hidden events (the query returns no row, so the caller
// falls back to the generic site card).

const SUPABASE_URL = 'https://lsxprzoxoarfakhxhoab.supabase.co';
const SUPABASE_PUBLIC_KEY = 'sb_publishable_9U61L_y4qyiXga9-VK0rFw_oaDrGmIT';

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

function isEventId(id) {
  return typeof id === 'string' && UUID.test(id);
}

async function fetchEvent(id) {
  if (!isEventId(id)) return null;
  try {
    const res = await fetch(
      `${SUPABASE_URL}/rest/v1/events?id=eq.${encodeURIComponent(id)}&is_live=eq.true&select=name,date,date_end,start_time,city,formats,is_sim`,
      { headers: { apikey: SUPABASE_PUBLIC_KEY, Authorization: `Bearer ${SUPABASE_PUBLIC_KEY}` } },
    );
    if (!res.ok) return null;
    const rows = await res.json();
    return Array.isArray(rows) && rows[0] ? rows[0] : null;
  } catch {
    return null;
  }
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/** "Sat 18 Oct 2026" from a YYYY-MM-DD string, computed in UTC so the day never shifts. */
function prettyDate(iso) {
  if (typeof iso !== 'string') return '';
  const d = new Date(`${iso}T00:00:00Z`);
  if (isNaN(d.getTime())) return '';
  return d.toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' });
}

/** "10:00" from "10:00:00" or "10:00". */
function prettyTime(t) {
  return typeof t === 'string' && /^\d{2}:\d{2}/.test(t) ? t.slice(0, 5) : '';
}

/** One line: "Sat 18 Oct 2026 · 10:00 · Leeds". */
function whenWhere(ev) {
  return [prettyDate(ev.date), prettyTime(ev.start_time), ev.city].filter(Boolean).join(' · ');
}

module.exports = { SUPABASE_URL, isEventId, fetchEvent, escapeHtml, prettyDate, prettyTime, whenWhere };
