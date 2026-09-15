// Vercel Edge Function — branded PNG card for a shared race result (Ref 155).
//
// Rendered server-side via @vercel/og (Satori) rather than captured on-device
// — any native image-capture lib needs a real eas build regardless of which
// one is chosen, so this ships the card without waiting on that native
// rebuild. On-device capture is a later phase.
//
// No JSX here (this repo has no build step / bundler) — @vercel/og's
// ImageResponse accepts a plain Satori-compatible element tree of
// { type, props: { style, children } } objects instead.
//
// Reads the same narrow public_race_results view as ../[id].js — see that
// file's header for why (minimal-data enforcement at the DB layer).

import { ImageResponse } from '@vercel/og';

export const config = { runtime: 'edge' };

const SUPABASE_URL = 'https://lsxprzoxoarfakhxhoab.supabase.co';
const SUPABASE_PUBLIC_KEY = 'sb_publishable_9U61L_y4qyiXga9-VK0rFw_oaDrGmIT';

function el(type, style, children) {
  return { type, props: { style, children } };
}

export default async function handler(request) {
  const url = new URL(request.url);
  const id = url.searchParams.get('id');

  let result = null;
  if (id) {
    try {
      const apiRes = await fetch(
        `${SUPABASE_URL}/rest/v1/public_race_results?id=eq.${encodeURIComponent(id)}&select=event_name,division,total_time`,
        { headers: { apikey: SUPABASE_PUBLIC_KEY, Authorization: `Bearer ${SUPABASE_PUBLIC_KEY}` } },
      );
      const rows = await apiRes.json();
      result = Array.isArray(rows) ? rows[0] : null;
    } catch {
      // fall through to the generic card below
    }
  }

  const eventName = result?.event_name ?? 'HyPair';
  const time = result?.total_time;
  const division = result?.division;

  const tree = el('div', {
    display: 'flex', flexDirection: 'column', justifyContent: 'space-between',
    width: '1200px', height: '630px', padding: '64px',
    background: '#0F1318', color: '#fff', fontFamily: 'sans-serif',
  }, [
    el('div', { display: 'flex', alignItems: 'center' }, [
      el('div', {
        fontSize: 28, fontWeight: 700, letterSpacing: 4, textTransform: 'uppercase', color: '#F2D079',
      }, 'HyPair'),
    ]),
    el('div', { display: 'flex', flexDirection: 'column' }, [
      division && el('div', { fontSize: 30, color: '#F2D079', marginBottom: 16, textTransform: 'uppercase', letterSpacing: 2 }, division),
      el('div', { display: 'flex', fontSize: 72, fontWeight: 900, lineHeight: 1.15 }, eventName),
      time && el('div', { display: 'flex', fontSize: 56, fontWeight: 700, color: 'rgba(255,255,255,0.85)', marginTop: 12 }, time),
    ].filter(Boolean)),
    el('div', { display: 'flex', fontSize: 24, color: 'rgba(255,255,255,0.5)' }, 'Find your next race partner — hypair.app'),
  ]);

  return new ImageResponse(tree, { width: 1200, height: 630 });
}
