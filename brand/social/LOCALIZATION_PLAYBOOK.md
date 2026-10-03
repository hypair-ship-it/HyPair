# Social carousel localization playbook

How the 4-slide "HyPair is live" carousel gets adapted per market/city. Started 18 Sep 2026
when localizing for Toronto/Tampa/Birmingham/Denver/Dallas and building a real US-market
version of slide 1 and the "Partner dropped out?" slide using actual app screenshots
instead of mockups.

## Folder structure (reorganized 2 Oct 2026)

`brand/social/posts/` is split into:
- **`events/<city-or-event>/`** — one folder per event: the carousel/moment SVG sources, a
  `png-export/` folder for the finals, screenshots, and captions. Currently birmingham,
  boston, dublin-series2 (Tryka Series 2 Race 1), hyrox-dublin, tampa, and
  tryka-grand-finale-lisbon. The event's unposted teaser SVG lives in its folder.
  (Boston was folded into `events/boston/` on 2 Oct after its post went live.)
- **`features/`** — Thursday feature posts (texture-layout mockups, e.g. Pace match).
- **`gyms/`** — gym-facing assets: the founding-gym cold email/DM sequence (sim-partner
  promo, general share, feedback poll, app-preview proof) and `public-carousel/`, the public
  gym-features carousel live on Facebook/Instagram since 1 Oct 2026. The outreach pieces are
  not posted to public Facebook groups — see the Founding Gym Program memory.
- **`_templates/`** — generic launch slides kept as editable sources for new cities.
- **`_archive/`** — finished events and old material: `2026-09/launch-carousel/` (the 14 Sep
  launch set) and `reference-archive/`. Move an event folder here once the race has happened.
- **`_templates/moments/`** — the three-posting-moments plan and `make_moment1.py` (B2C session).

## The 4 slides (in `_archive/2026-09/launch-carousel/`; generic sources in `_templates/`)

1. **Live announcement** — now built in two forms:
   - `hypair-live-announcement-events.svg` — original version: eyebrow "NOW LIVE", headline
     "HyPair is live.", plain-text store line, body copy, phone screenshot of the Events tab.
   - `hypair-us-live-events-v2` (SVG deleted 2 Oct 2026, PNG kept in `_archive/2026-09/launch-carousel/`; the pattern lives on in `events/tampa/slide1-on-sale.svg`) — **redesigned version, settled 18 Sep** (see below) —
     use this pattern for any new market going forward, not the original.
2. **Not whoever asked first** — fully generic problem slide (match-score mockup). No
   location or country reference anywhere on it. Reuse as-is everywhere.
3. **Partner dropped out?** — "THE FIX" problem/solution slide with a phone screenshot.
   Prefer `hypair-partner-dropped-out-v2.svg` (real Boston "Find a Partner" screen — Saoirse,
   Grace, Ciara, all 65% match) over the plain mockup version (deleted in the 29 Sep
   cleanup — v2 is now the only copy).
4. **Every race, one app** — fully generic closing/product slide (home-screen mockup with
   London Race 5 / HYROX Dublin baked into the UI text). No country claim in the copy
   itself, so safe to reuse everywhere — the UI content shown is decorative, not a claim.

Slides 2 and 4 need no market-specific edits. Slides 1 and 3 are the ones with a phone
screenshot that benefits from showing races relevant to the market being posted into.

## Slide 1 copy & layout — RESOLVED 18 Sep 2026

Old copy (eyebrow "NOW LIVE" / "HyPair is live." / plain-text store line / "Find your HYROX
or Tryka doubles partner...") is superseded. Settled direction, built in
`hypair-us-live-events-v2.svg`:

- Eyebrow (red): "STUCK FOR A PARTNER?"
- Brand line (gold, its own line): "HyPair"
- Headline (white): "Meet your match." (reuses the app's actual tagline)
- Real Apple + Google store badges (not plain text) — sourced from Apple's official badge
  API (`tools.applemediaservices.com/api/badges/...`) and Google's official generic badge
  PNG, saved to `brand/badges/`. Apple's own guideline: use the **black** badge whenever
  shown alongside another platform's badge. The Google PNG has ~41px of transparent padding
  baked into its canvas that Apple's doesn't — crop it to content bounds first
  (`im.crop(im.getbbox())`) or the two badges render at visibly different sizes even at
  equal height.
- Body copy moved up right under the badges (old version had it much lower, leaving dead
  space above).
- **US-market copy drops Tryka**: "HyPair matches you by pace, goal and the exact race
  you're entering. Find your HYROX doubles partner today." — Tryka is only real in
  Ireland/UK, never mention it in US/Canada copy.
- Vertical balance: don't compress everything into the top third — spread eyebrow → brand →
  headline → badges → body across roughly the same vertical span as the phone mockup, or
  the bottom-left corner reads as an obvious empty gap next to the phone's full-height
  content.

**No EU equivalent of this v2 redesign exists yet** — still using the original
`hypair-live-announcement-events.svg` copy/layout for EU markets (Birmingham, etc.). Same
redesign (badges, "Meet your match.", Tryka kept in body copy this time) should carry over
when built.

## What changes per market

- **Caption text** (written fresh per post, not baked into the image): race name, date,
  hashtag. Never claim a specific country in the caption unless it's true for every group
  the post goes to — e.g. never say "now live in the US" when posting to Canada.
- **Tryka mentions**: drop entirely from US/Canada copy (see above).
- **Slide 1 phone screenshot**: swap to a real Events-tab screenshot whose visible races
  match the market being posted into. Two exist so far (EU and US) — see
  `_archive/2026-09/launch-carousel/png-export/`.
- **Slide 3 phone screenshot**: swap to a real "Find a Partner" screenshot with populated,
  good-looking matches (high match %, real photos, no empty state). Seed the sandbox DB
  first if the real candidate pool is empty (see the sandbox test-data toolkit memory).

**Never reuse a market-specific screenshot outside its market** — a screenshot with a real
event's name/date baked into the image itself (like the deleted SLC-branded slide) only
works for that one post. Check `_needs-decision/` before reusing anything from there.

## How to build a new market's slide 1 or slide 3

1. Get a real screenshot showing what you want visible (Events tab for slide 1, a
   populated Find a Partner screen for slide 3) — from the iOS Simulator or the live app.
2. Swap the screenshot into a **copy** of the existing SVG source (never overwrite the
   original) — the phone mockup is a flat embedded PNG (base64) inside the SVG, not
   editable text, so this is a base64 find/replace:
   ```python
   import re, base64
   with open('events/tampa/slide1-on-sale.svg') as f:
       content = f.read()
   with open('<path to new screenshot>.png', 'rb') as f:
       new_img_b64 = base64.b64encode(f.read()).decode('ascii')
   new_content = re.sub(r'href="data:image/png;base64,[^"]+"',
                         'href="data:image/png;base64,' + new_img_b64 + '"', content)
   with open('<new-name>.svg', 'w') as f:
       f.write(new_content)
   ```
   The SVG's `preserveAspectRatio="xMidYMid slice"` on that `<image>` element auto-crops
   whatever resolution screenshot you feed it, so exact source dimensions don't matter.
   Watch out if the SVG has more than one `<image>` tag (e.g. after adding badges) — a
   generic regex will grab the first match, which may not be the phone mockup. Match on the
   phone's specific `width`/`height` attributes instead.
3. Render to an exact 1080×1080 PNG with `rsvg-convert` (installed via
   `brew install librsvg` — the browser's own screenshot tool scales to fit the pane and is
   **not** pixel-exact, don't use it for final exports):
   ```bash
   rsvg-convert -w 1080 -h 1080 -o <new-name>.png <new-name>.svg
   ```
4. Copy the result into `_archive/2026-09/launch-carousel/png-export/` alongside the others.

## Open gap — pre-race urgency content (flagged 29 Sep 2026)

The launch carousel covers "we exist" for a new market. Nothing yet covers "race week is
here, last chance to find a partner" urgency for a specific approaching event — the
teaser SVGs now live inside their event folders (`events/hyrox-dublin/`, `events/dublin-series2/`,
`events/birmingham/`); the three-moments plan in `_templates/moments/` has superseded this gap for group posts. Birmingham (27–28 Oct) is the nearest upcoming
race as of 29 Sep — good candidate to build the first proper version of this against.
