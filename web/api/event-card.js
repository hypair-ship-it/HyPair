// Vercel Edge Function — the preview card image for a shared event (1200x630 PNG).
//
// Drawn on the server with @vercel/og (Satori) from the event's public details, so the gym
// never has to make or upload a picture: the chat app fetches this URL itself when the link
// is pasted. No JSX here (this site has no build step), so the card is a plain element tree.
//
// Same data and same limits as api/event/[id].js: live events only, no athlete data.
// A draft, hidden or unknown event gets the generic HyPair card.
//
// Edge runtime cannot require() the shared helper, so the few lines needed are repeated here.

import { ImageResponse } from '@vercel/og';

export const config = { runtime: 'edge' };

const SUPABASE_URL = 'https://lsxprzoxoarfakhxhoab.supabase.co';
const SUPABASE_PUBLIC_KEY = 'sb_publishable_9U61L_y4qyiXga9-VK0rFw_oaDrGmIT';
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

const BG = '#0F1318';
const GOLD = '#F2D079';
const RED = '#E22424';

function el(type, style, children) {
  return { type, props: { style, children } };
}

function prettyDate(iso) {
  const d = new Date(`${iso}T00:00:00Z`);
  return isNaN(d.getTime()) ? '' : d.toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' });
}

async function fetchEvent(id) {
  if (!id || !UUID.test(id)) return null;
  try {
    const res = await fetch(
      `${SUPABASE_URL}/rest/v1/events?id=eq.${encodeURIComponent(id)}&is_live=eq.true&select=name,date,start_time,city,formats`,
      { headers: { apikey: SUPABASE_PUBLIC_KEY, Authorization: `Bearer ${SUPABASE_PUBLIC_KEY}` } },
    );
    if (!res.ok) return null;
    const rows = await res.json();
    return Array.isArray(rows) && rows[0] ? rows[0] : null;
  } catch {
    return null;
  }
}

export default async function handler(request) {
  const id = new URL(request.url).searchParams.get('id');
  const ev = await fetchEvent(id);

  const name = ev?.name ?? 'Meet your match';
  const when = ev
    ? [prettyDate(ev.date), typeof ev.start_time === 'string' ? ev.start_time.slice(0, 5) : '', ev.city].filter(Boolean).join('  ·  ')
    : 'Find your HYROX and TRYKA doubles partner';
  const formats = Array.isArray(ev?.formats) ? ev.formats.slice(0, 4) : [];
  const nameSize = name.length > 44 ? 56 : name.length > 28 ? 68 : 84;

  const tree = el('div', {
    display: 'flex', flexDirection: 'column', justifyContent: 'space-between',
    width: '1200px', height: '630px', padding: '64px',
    background: BG, color: '#fff', fontFamily: 'sans-serif',
    borderTop: `10px solid ${RED}`,
  }, [
    el('div', { display: 'flex', alignItems: 'center' }, [
      { type: 'img', props: { src: 'https://hypair.app/assets/hypair-icon-only.png', width: 56, height: 56, style: { marginRight: 16 } } },
      el('div', { display: 'flex', fontSize: 34, fontWeight: 700, color: GOLD }, 'HyPair'),
    ]),
    el('div', { display: 'flex', flexDirection: 'column' }, [
      ev && el('div', { display: 'flex', fontSize: 28, letterSpacing: 4, color: GOLD, marginBottom: 18 }, 'FIND YOUR PARTNER'),
      el('div', { display: 'flex', fontSize: nameSize, fontWeight: 900, lineHeight: 1.1 }, name),
      el('div', { display: 'flex', fontSize: 36, color: 'rgba(255,255,255,0.85)', marginTop: 22 }, when),
      formats.length > 0 && el('div', { display: 'flex', marginTop: 28 },
        formats.map((f) => el('div', {
          display: 'flex', fontSize: 26, color: GOLD, border: `2px solid ${GOLD}`, borderRadius: 999,
          padding: '8px 22px', marginRight: 14,
        }, f))),
    ].filter(Boolean)),
    el('div', { display: 'flex', justifyContent: 'space-between', fontSize: 28, color: 'rgba(255,255,255,0.6)' }, [
      el('div', { display: 'flex' }, 'Sign up and find your partner'),
      el('div', { display: 'flex', color: GOLD }, 'hypair.app'),
    ]),
  ]);

  return new ImageResponse(tree, {
    width: 1200,
    height: 630,
    headers: { 'Cache-Control': 'public, immutable, no-transform, s-maxage=3600, max-age=3600' },
  });
}
