// Vercel Edge Function — the preview card image for a shared event (1200x630 PNG).
//
// Drawn on the server with @vercel/og (Satori) from the event's public details, so the gym never
// has to make or upload a picture: the chat app fetches this URL itself when the link is pasted.
// No JSX here (this site has no build step), so the card is a plain element tree.
//
// Design (founder feedback 9 Oct 2026): the EVENT is the hero, not HyPair. Event name in the brand's
// display font (Bebas Neue), the date in gold, the place, the formats as quiet pills, and one small
// HyPair mark at the bottom. No stripe, no "find your partner" slogan. A gym should be able to post
// this as "we're running this event", with HyPair as the way to join.
//
// Same data and limits as api/event/[id].js: live events only, no athlete data, no gym name (gyms
// are not readable logged out). A draft, hidden or unknown event gets the generic HyPair card.
//
// Edge runtime cannot require() the shared helper, so the few lines needed are repeated here.

import { ImageResponse } from '@vercel/og';

export const config = { runtime: 'edge' };

const SUPABASE_URL = 'https://lsxprzoxoarfakhxhoab.supabase.co';
const SUPABASE_PUBLIC_KEY = 'sb_publishable_9U61L_y4qyiXga9-VK0rFw_oaDrGmIT';
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

const GOLD = '#F2D079';
const RED = '#E22424';   // the app's primary-button red
const INK = '#0F1318';

// The brand mark (same paths as favicon.svg), cropped to the mark itself, as an image Satori can draw.
function markSvg(fill) {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="222 150 256 350"><path fill="${fill}" d="M350,399.3c-26.8,0-48.6,21.8-48.6,48.6c0,26.8,21.8,48.6,48.6,48.6s48.6-21.8,48.6-48.6C398.6,421.1,376.8,399.3,350,399.3z M350,463.9c-8.8,0-16-7.2-16-16c0-8.8,7.2-16,16-16c8.8,0,16,7.2,16,16C366,456.7,358.8,463.9,350,463.9z"/><polygon fill="${fill}" points="412.1,154.1 374.4,154.1 374.4,281.6 325.6,281.6 325.6,154.1 287.9,154.1 287.9,319.2 412.1,319.2"/><polygon fill="${fill}" points="401.5,336.6 298.5,336.6 298.4,336.6 298.4,336.8 226,409.1 226,496.4 258.5,496.4 258.5,422.6 306.9,374.3 393.1,374.3 441.5,422.6 441.5,496.4 474,496.4 474,409.1"/></svg>`;
  return `data:image/svg+xml;base64,${btoa(svg)}`;
}

function el(type, style, children) {
  return { type, props: { style, children } };
}

function prettyDate(iso) {
  const d = new Date(`${iso}T00:00:00Z`);
  return isNaN(d.getTime()) ? '' : d.toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' }).replace(',', '');
}

async function fetchEvent(id) {
  if (!id || !UUID.test(id)) return null;
  try {
    const res = await fetch(
      `${SUPABASE_URL}/rest/v1/events?id=eq.${encodeURIComponent(id)}&is_live=eq.true&select=name,type,is_sim,date,date_end,start_time,city,country,formats`,
      { headers: { apikey: SUPABASE_PUBLIC_KEY, Authorization: `Bearer ${SUPABASE_PUBLIC_KEY}` } },
    );
    if (!res.ok) return null;
    const rows = await res.json();
    return Array.isArray(rows) && rows[0] ? rows[0] : null;
  } catch {
    return null;
  }
}

// Fonts are static files on this same site (assets/fonts/*.ttf); Satori cannot read woff2.
async function loadFonts(origin) {
  const get = async (file) => (await fetch(`${origin}/assets/fonts/${file}`)).arrayBuffer();
  const [bebas, barlow, barlowBold] = await Promise.all([get('BebasNeue-Regular.ttf'), get('Barlow-Medium.ttf'), get('Barlow-Bold.ttf')]);
  return [
    { name: 'Bebas', data: bebas, weight: 400, style: 'normal' },
    { name: 'Barlow', data: barlow, weight: 500, style: 'normal' },
    { name: 'Barlow', data: barlowBold, weight: 700, style: 'normal' },
  ];
}

/** "HYROX SIMULATION" for a gym's event, "HYROX" / "TRYKA" for an official race. */
function eyebrowFor(ev) {
  const series = ev.type === 'TRYKA' ? 'TRYKA' : 'HYROX';
  return ev.is_sim ? `${series} SIMULATION` : series;
}

/** Event names vary from "Dublin" to a full sentence; shrink the type so two lines always fit. */
function nameSize(name) {
  const n = name.length;
  if (n <= 14) return 168;
  if (n <= 24) return 132;
  if (n <= 36) return 104;
  if (n <= 48) return 84;
  if (n <= 64) return 68;
  return 56;
}

/** Past ~90 characters even the smallest size would run to a third line. */
function shortened(name) {
  return name.length > 90 ? `${name.slice(0, 87).trimEnd()}…` : name;
}

function background() {
  return {
    display: 'flex', position: 'relative', flexDirection: 'column', justifyContent: 'space-between',
    width: '1200px', height: '630px', padding: '64px 72px',
    backgroundColor: INK,
    backgroundImage: 'linear-gradient(135deg, #0F1318 0%, #141B24 60%, #1A2430 100%)',
    color: '#fff', fontFamily: 'Barlow',
  };
}

function glow() {
  return el('div', {
    position: 'absolute', display: 'flex', right: '-220px', top: '-260px', width: '760px', height: '760px', borderRadius: '380px',
    backgroundImage: 'radial-gradient(circle, rgba(242,208,121,0.20) 0%, rgba(242,208,121,0) 68%)',
  }, []);
}

function redGlow() {
  return el('div', {
    position: 'absolute', display: 'flex', left: '-260px', bottom: '-380px', width: '760px', height: '760px', borderRadius: '380px',
    backgroundImage: 'radial-gradient(circle, rgba(226,36,36,0.16) 0%, rgba(226,36,36,0) 68%)',
  }, []);
}

// Small red marker in front of the gold line at the top (a dot, not a stripe).
function eyebrow(text) {
  return el('div', { display: 'flex', alignItems: 'center', marginBottom: 14 }, [
    el('div', { display: 'flex', width: 14, height: 14, borderRadius: 7, backgroundColor: RED, marginRight: 16 }, []),
    el('div', { display: 'flex', fontSize: 26, fontWeight: 700, letterSpacing: 7, color: GOLD }, text),
  ]);
}

function footer() {
  return el('div', { display: 'flex', alignItems: 'center', justifyContent: 'space-between' }, [
    el('div', { display: 'flex', alignItems: 'center' }, [
      { type: 'img', props: { src: markSvg(GOLD), width: 26, height: 36, style: { marginRight: 14 } } },
      el('div', { display: 'flex', fontSize: 32, fontWeight: 700, color: 'rgba(255,255,255,0.92)', letterSpacing: 0.5 }, 'HyPair'),
    ]),
    // The one call to action: the same red as the app's main buttons.
    el('div', { display: 'flex', alignItems: 'center', backgroundColor: RED, borderRadius: 999, padding: '14px 34px' }, [
      el('div', { display: 'flex', fontSize: 30, fontWeight: 700, color: '#fff', letterSpacing: 0.5 }, 'Join on HyPair'),
    ]),
  ]);
}

function eventCard(ev) {
  const when = [prettyDate(ev.date), typeof ev.start_time === 'string' && /^\d{2}:\d{2}/.test(ev.start_time) ? ev.start_time.slice(0, 5) : ''].filter(Boolean).join('  ·  ');
  const place = [ev.city, ev.country].filter(Boolean).join(', ');
  // Four formats and "+N more": an official race can list eight, and half a list reads as a mistake.
  const all = Array.isArray(ev.formats) ? ev.formats : [];
  const formats = all.length > 5 ? [...all.slice(0, 4), `+${all.length - 4} more`] : all;

  return el('div', background(), [
    glow(),
    redGlow(),
    el('div', { display: 'flex', flexDirection: 'column' }, [
      eyebrow(eyebrowFor(ev)),
      el('div', { display: 'flex', fontFamily: 'Bebas', fontSize: nameSize(shortened(ev.name)), lineHeight: 0.98, letterSpacing: 1.5, color: '#fff', maxWidth: '1000px' }, shortened(ev.name)),
      when && el('div', { display: 'flex', fontFamily: 'Bebas', fontSize: 58, letterSpacing: 3, color: GOLD, marginTop: 22 }, when.toUpperCase()),
      place && el('div', { display: 'flex', fontSize: 34, fontWeight: 500, color: 'rgba(255,255,255,0.72)', marginTop: 4 }, place),
      formats.length > 0 && el('div', { display: 'flex', marginTop: 26 },
        formats.map((f) => el('div', {
          display: 'flex', fontSize: 24, fontWeight: 500, color: 'rgba(255,255,255,0.85)', backgroundColor: 'rgba(255,255,255,0.08)',
          border: '1.5px solid rgba(255,255,255,0.16)', borderRadius: 999, padding: '7px 20px', marginRight: 12,
        }, f))),
    ].filter(Boolean)),
    footer(),
  ]);
}

// Unknown, draft or hidden event: the brand card.
function genericCard() {
  return el('div', background(), [
    glow(),
    redGlow(),
    el('div', { display: 'flex', flexDirection: 'column' }, [
      eyebrow('HYROX  ·  TRYKA'),
      el('div', { display: 'flex', fontFamily: 'Bebas', fontSize: 168, lineHeight: 0.98, letterSpacing: 1.5, color: '#fff' }, 'Meet your match'),
      el('div', { display: 'flex', fontSize: 36, fontWeight: 500, color: 'rgba(255,255,255,0.72)', marginTop: 18 }, 'Find a doubles partner for your next race'),
    ]),
    footer(),
  ]);
}

export default async function handler(request) {
  const url = new URL(request.url);
  const ev = await fetchEvent(url.searchParams.get('id'));
  // If the fonts cannot be fetched the card still renders, in the default font, rather than failing outright.
  const fonts = await loadFonts(url.origin).catch(() => []);

  return new ImageResponse(ev ? eventCard(ev) : genericCard(), {
    width: 1200,
    height: 630,
    fonts,
    headers: { 'Cache-Control': 'public, immutable, no-transform, s-maxage=3600, max-age=3600' },
  });
}
