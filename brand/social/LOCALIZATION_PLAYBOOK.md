# Social carousel localization playbook

How the 4-slide "HyPair is live" carousel gets adapted per market/city. Started 18 Sep 2026
when localizing for Toronto/Tampa/Birmingham/Denver/Dallas and building a real US-market
version of slide 1 and the "Partner dropped out?" slide using actual app screenshots
instead of mockups.

## The 4 slides

1. **Live announcement** — eyebrow "NOW LIVE", headline, store line, body copy, phone
   screenshot of the app's Events tab.
2. **Not whoever asked first** — fully generic problem slide (match-score mockup). No
   location or country reference anywhere on it. Reuse as-is everywhere.
3. **Partner dropped out?** — "THE FIX" problem/solution slide, phone screenshot.
4. **Every race, one app** — fully generic closing/product slide (home-screen mockup with
   London Race 5 / HYROX Dublin baked into the UI text). No country claim in the copy
   itself, so safe to reuse everywhere — the UI content shown is decorative, not a claim.

Slides 2 and 4 need no market-specific edits. Slides 1 and 3 are the ones with a phone
screenshot that benefits from showing races relevant to the market being posted into.

## What changes per market

- **Caption text** (written fresh per post, not baked into the image): race name, date,
  hashtag. Never claim a specific country in the caption unless it's true for every group
  the post goes to — e.g. never say "now live in the US" when posting to Canada.
- **Tryka mentions**: Tryka is only a real, relevant event brand in Ireland/UK. Drop it
  entirely from any US/Canada-targeted copy — "Find your HYROX doubles partner", not
  "HYROX or Tryka".
- **Slide 1 phone screenshot**: swap to a real Events-tab screenshot whose visible races
  match the market being posted into (see below). Two exist so far:
  - `hypair-live-announcement-events.png` — EU/Ireland-UK (London Race 5, Series 2 Race 1
    Dublin, HYROX Dublin)
  - `hypair-us-live-events.png` — US (Salt Lake City, Boston, Tampa, Denver)
- **Slide 3 phone screenshot**: swap to a real "Find a Partner" screenshot with populated,
  good-looking matches (high match %, real photos, no empty state). So far:
  - `hypair-partner-dropped-out.png` — original generic match/chat mockup, still fine as a
    fallback
  - `hypair-partner-dropped-out-v2.png` — real Boston "Find a Partner" screen (Saoirse,
    Grace, Ciara, all 65% match) — more authentic, prefer this one going forward

**Never reuse a market-specific screenshot outside its market** — e.g. the SLC-branded
"NOW LIVE IN THE US" slide (`hypair-us-live-slc.png`) has "Salt Lake City" and "18-20 SEP"
baked into the image itself and only works for that one post.

## How to build a new market's slide 1 or slide 3

1. Get a real screenshot showing what you want visible (Events tab for slide 1, a
   populated Find a Partner screen for slide 3) — from the iOS Simulator or the live app.
   For slide 3, seed the sandbox DB with a few well-matched demo profiles first if the real
   candidate pool is empty (see the sandbox test-data toolkit memory) so the screenshot
   doesn't show an empty state.
2. Swap the screenshot into a **copy** of the existing SVG source (never overwrite the
   original) — the phone mockup is a flat embedded PNG (base64) inside the SVG, not
   editable text, so this is a base64 find/replace:
   ```python
   import re, base64
   with open('hypair-live-announcement-events.svg') as f:
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
3. Render to an exact 1080×1080 PNG with `rsvg-convert` (installed via
   `brew install librsvg` — the browser's own screenshot tool scales to fit the pane and is
   **not** pixel-exact, don't use it for final exports):
   ```bash
   rsvg-convert -w 1080 -h 1080 -o <new-name>.png <new-name>.svg
   ```
4. Copy the result into `png-export/` alongside the others.

## Open decision — slide 1 copy & layout (not yet settled, 18 Sep 2026)

Current copy:
- Eyebrow: "NOW LIVE"
- Headline: "HyPair is live."
- Store line: "App Store & Google Play" (plain gold text)
- Body: "Find your HYROX or Tryka doubles partner — matched by pace, goal and the race
  you're entering."

Under discussion:
- Body copy sits too low / too much dead space above it — move it up, closer under the
  store line.
- Replace the plain-text "App Store & Google Play" line with the actual official store
  badge graphics (small, under the headline) — same badges already used on the website
  hero, for instant recognizability instead of a text line.
- For US-only posts, drop "Tryka" — "Find your HYROX doubles partner — matched by pace,
  goal and the race you're entering."
- Headline itself may change too (e.g. leading with the problem instead of the
  announcement) — no final direction chosen yet.

Not resolved as of 18 Sep — next session should check whether a direction was agreed before
re-touching the slide 1 SVGs.
