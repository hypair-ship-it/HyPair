// Vercel Edge Function — the preview card image for a shared event (1200x630 PNG).
//
// Drawn on the server with @vercel/og (Satori) from the event's public details, so the gym never
// has to make or upload a picture: the chat app fetches this URL itself when the link is pasted.
// No JSX here (this site has no build step), so the card is a plain element tree.
//
// Design (founder feedback 9 Oct 2026, twice): built on the brand's own social-post system (brand/BRAND.md,
// "Swiss Alps"): solid Summit slate background, the gold mark + wordmark top-left, a letter-spaced RED
// line (the only red), a big white headline, white-toned details, Sun Valley gold only for the logo and the
// format chips. No gradients, glows, stripes or buttons. HyPair appears once (top-left): the chat app already
// prints the domain under the picture, and the gym's event is the point of the card.
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

const GOLD = '#F2D079';   // Sun Valley: logo and chips only
const RED = '#E22424';    // Swiss Alps Red: the one accent line
const SUMMIT = '#4C5F6B'; // brand background for social

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
      `${SUPABASE_URL}/rest/v1/events?id=eq.${encodeURIComponent(id)}&is_live=eq.true&select=name,type,is_sim,date,date_end,start_time,city,country,formats,waves_published`,
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
  const [medium, bold] = await Promise.all([get('Barlow-Medium.ttf'), get('Barlow-Bold.ttf')]);
  return [
    { name: 'Barlow', data: medium, weight: 500, style: 'normal' },
    { name: 'Barlow', data: bold, weight: 700, style: 'normal' },
  ];
}

/** "HYROX SIMULATION" for a gym's event, "HYROX" / "TRYKA" for an official race. */
function eyebrowFor(ev) {
  const series = ev.type === 'TRYKA' ? 'TRYKA' : 'HYROX';
  return ev.is_sim ? `${series} SIMULATION` : series;
}

/**
 * Event names run from "Dublin" to a full sentence. Pick the largest type size whose estimated wrapped height
 * (words wrap, so a character is counted at about 0.58 of the size) fits the 210px the headline may use.
 */
function nameSize(name) {
  const n = name.length;
  for (const size of [140, 120, 104, 92, 80, 72, 64, 56, 50]) {
    const perLine = 1040 / (0.58 * size);
    const lines = Math.ceil(n / perLine);
    if (lines * size * 1.04 <= 210) return size;
  }
  return 44;
}

/** Past ~90 characters even the smallest size would run long. */
function shortened(name) {
  return name.length > 90 ? `${name.slice(0, 87).trimEnd()}…` : name;
}

function canvas(children) {
  return el('div', {
    display: 'flex', flexDirection: 'column', width: '1200px', height: '630px', padding: '60px 76px',
    backgroundColor: SUMMIT, color: '#fff', fontFamily: 'Barlow',
  }, children);
}

// The brand lockup, as on the social posts: gold mark, gold wordmark, top-left.
function lockup() {
  return el('div', { display: 'flex', alignItems: 'center' }, [
    { type: 'img', props: { src: markSvg(GOLD), width: 31, height: 42, style: { marginRight: 16 } } },
    el('div', { display: 'flex', fontSize: 40, fontWeight: 700, color: GOLD }, 'HyPair'),
  ]);
}

// The red line above the headline, letter-spaced capitals, as on the posts.
function eyebrow(text) {
  return el('div', { display: 'flex', fontSize: 28, fontWeight: 700, letterSpacing: 8, color: RED, marginBottom: 18 }, text);
}

function chip(label) {
  return el('div', {
    display: 'flex', fontSize: 24, fontWeight: 500, color: GOLD, backgroundColor: 'rgba(242,208,121,0.12)',
    border: '1.5px solid rgba(242,208,121,0.35)', borderRadius: 999, padding: '7px 22px', marginRight: 12,
  }, label);
}

function eventCard(ev, wavesOut) {
  const name = shortened(ev.name);
  const when = [prettyDate(ev.date), typeof ev.start_time === 'string' && /^\d{2}:\d{2}/.test(ev.start_time) ? ev.start_time.slice(0, 5) : ''].filter(Boolean).join('   ·   ');
  const place = [ev.city, ev.country].filter(Boolean).join(', ');
  // Four formats and "+N more": an official race can list eight, and half a list reads as a mistake.
  const all = Array.isArray(ev.formats) ? ev.formats : [];
  const formats = all.length > 5 ? [...all.slice(0, 4), `+${all.length - 4} more`] : all;

  return canvas([
    lockup(),
    el('div', { display: 'flex', flexDirection: 'column', flexGrow: 1, justifyContent: 'center', paddingTop: 20 }, [
      eyebrow(wavesOut ? 'WAVE TIMES ARE OUT' : eyebrowFor(ev)),
      el('div', { display: 'flex', fontSize: nameSize(name), fontWeight: 700, lineHeight: 1.04, letterSpacing: -1.5, color: '#fff', maxWidth: '1040px' }, name),
      when && el('div', { display: 'flex', fontSize: 46, fontWeight: 700, color: '#fff', marginTop: 26 }, when),
      place && el('div', { display: 'flex', fontSize: 34, fontWeight: 500, color: 'rgba(255,255,255,0.72)', marginTop: 6 }, place),
      formats.length > 0 && el('div', { display: 'flex', marginTop: 28 }, formats.map(chip)),
    ].filter(Boolean)),
  ]);
}

// Unknown, draft or hidden event: the brand card.
function genericCard() {
  return canvas([
    lockup(),
    el('div', { display: 'flex', flexDirection: 'column', flexGrow: 1, justifyContent: 'center' }, [
      eyebrow('HYROX  ·  TRYKA'),
      el('div', { display: 'flex', fontSize: 120, fontWeight: 700, lineHeight: 1.04, letterSpacing: -2, color: '#fff' }, 'Meet your match.'),
      el('div', { display: 'flex', fontSize: 38, fontWeight: 500, color: 'rgba(255,255,255,0.72)', marginTop: 22 }, 'Find a doubles partner for your next race.'),
    ]),
  ]);
}

export default async function handler(request) {
  const url = new URL(request.url);
  const ev = await fetchEvent(url.searchParams.get('id'));
  // If the fonts cannot be fetched the card still renders, in the default font, rather than failing outright.
  const fonts = await loadFonts(url.origin).catch(() => []);
  // ?v=waves only changes the picture once the gym has really shared the waves.
  const wavesOut = url.searchParams.get('v') === 'waves' && ev?.waves_published === true;

  return new ImageResponse(ev ? eventCard(ev, wavesOut) : genericCard(), {
    width: 1200,
    height: 630,
    fonts,
    headers: { 'Cache-Control': 'public, immutable, no-transform, s-maxage=3600, max-age=3600' },
  });
}
