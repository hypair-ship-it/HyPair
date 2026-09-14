# CLAUDE.md

Guidance for Claude Code when working in this repository (HyPair website).

---

## Project overview

HyPair is a mobile app that matches athletes with doubles partners for **HYROX** and
**Tryka** — official events and gym simulation events. Matching is based on pace, finish
goal, race format, and the specific event entered. It is **not** a dating app and not a
general fitness app. Spartan and Athex are explicitly out of scope — remove any reference
if found; an earlier version of this doc listed them as in-scope, which was wrong.

This repo is the **marketing website** — `hypair.app`. The mobile app lives in a
separate repo: `github.com/hypair-ship-it/HyPairApp`.

**Tone:** fun, social, community — finding the right person to race with, whether that's
chasing a PB or just wanting to meet people through sport. Warm, not corporate. The
emotional core copy and design should point toward: *"I did something hard, with someone
great, and it was fun."*

---

## Standing content rules — do not re-litigate these

1. **No "5K"** anywhere in website copy — say "pace" or "running pace". The app uses 5K
   pace internally as the matching input, but external copy never names it.
2. **No TikTok** in footer/social links on any page — handle is claimed but parked, not
   posted to. Instagram + Facebook only.
3. **No "→" arrow** on CTA buttons — they're buttons, not links.
4. **No founding-gym-programme offer on the website.** It's a personal, one-to-one
   conversation Ante has directly with gyms (free forever, in exchange for feedback) —
   never public messaging, never numbers, never named partners.
5. **No gym pricing on the website.** Gym pricing isn't confirmed; the site should say
   "get in touch to find out how listing your events works," nothing more specific.
6. **Not a dating app.** Copy must never imply romantic matching — community/sport framing
   only.

---

## Repo structure

```
HyPair/                              ← repo root (project container)
│
├── web/                             ← web root — everything Vercel serves
│   ├── index.html                   Main landing page (hypair.app)
│   ├── support.html                 → hypair.app/support — contact form (see below)
│   ├── for-gyms.html                → hypair.app/for-gyms
│   ├── terms.html                   → hypair.app/terms
│   ├── privacy.html                 → hypair.app/privacy
│   ├── cookies.html                 → hypair.app/cookies
│   ├── reset-password.html          → hypair.app/reset-password (noindex — app deep-link target, not a marketing page)
│   ├── favicon.ico / favicon.svg    Site favicon — dark bg (#13181F) + gold HyPair mark, matches the nav logo's colour family
│   ├── og-image.jpg                 Open Graph image (referenced in index.html) — dates from before the current hero redesign (pill/badge removed, store badges now white); check it still matches before assuming it's current
│   ├── robots.txt / sitemap.xml     SEO config
│   ├── googleb13411129c6994e3.html  Google Search Console verification
│   ├── vercel.json                  Vercel config — must live inside web/ (the Root Directory)
│   ├── api/csp-report.js            Vercel serverless function — CSP violation reporting endpoint
│   ├── .well-known/                 apple-app-site-association + assetlinks.json (iOS/Android universal/app links) — keep package names and signing fingerprints in sync with HyPairApp's app.config.js
│   └── assets/
│       ├── fonts/                   Self-hosted Barlow/Barlow Condensed woff2 files
│       └── screenshots/             Real app UI screenshots actually used on the site — never fabricate/mock these, the site was rebuilt specifically to remove fake-looking content
│
├── brand/                           ← all design assets (not served publicly)
│   ├── swiss-alps/                  Dark theme
│   │   ├── logo/                    Logos (SVG, PNG, ICO)
│   │   └── social/                  Social covers (FB, IG, LinkedIn, Twitter, Zoom)
│   ├── tundra-light/                Light theme
│   │   ├── logo/                    Logos (SVG, PNG, ICO)
│   │   └── social/                  Social covers (FB, IG, LinkedIn, Twitter, Zoom)
│   ├── social/
│   │   ├── posts/                   Published post images
│   │   └── inspiration/             Reference / source images
│   └── BRAND.md                     Design system reference (colours, fonts, tokens)
│
└── CLAUDE.md                        This file
```

**`vercel.json` must live inside `web/`** (the project's Vercel "Root Directory" is set to `web` in
the dashboard) — a copy at the git repo root is silently ignored: `redirects` and `headers` never
applied, with no error or warning anywhere, while `cleanUrls`-style file serving kept working
regardless (that part isn't sourced from the config file at all). Confirmed 4 Sep 2026 after
`/hyrox-dublin` etc. redirects silently no-opped in production for a day. Diagnose this class of bug
by comparing response headers on a real page vs `curl`-ing a definitely-nonexistent path — if the
security headers defined in `vercel.json` are missing on *every* response, the file isn't being read
at all, regardless of what its content says.

---

## Page architecture

Every page — HTML, CSS, and JavaScript — is self-contained in its own file in `web/`. No build
step, no package manager, no framework. Preview locally:

```bash
python3 -m http.server 3456 --directory web
```

Or use the `.claude/launch.json` config which is already set up.

### index.html

Hero leads with App Store/Google Play badges (white background, so they stand out against the
dark hero — they used to be black, which blended in). There is **no waitlist form** on this
site — the waitlist was retired 5 Sep 2026 (both iOS and Android live, 9 signups emailed and
closed) and the form/JS/`SUPABASE_URL`/`SUPABASE_ANON_KEY` constants were removed from
`index.html` entirely. If you see a reference to `#waitlist-section` or a waitlist Supabase
write anywhere, it's stale; the site only links out to the real App Store/Play listings now.
The `waitlist` table and its RLS policies still exist in the Supabase project
(`llkdujodseyilzbkzdbf`) but nothing on the live site writes to them anymore. The 9
historical rows were deleted on 14 Sep 2026 (table is now empty); `privacy.html`'s
legacy-data disclosure was updated to past tense to match. Don't reintroduce waitlist
language without also reviving a real collection mechanism.

Nav: How it works · For athletes · For gyms · FAQ · **Contact** (→ `/support#contact-athletes`)
· Get the App. The "Contact" link exists so an individual athlete has a path to the contact
page from the homepage — it didn't always.

### support.html — "Get in touch"

Two independent contact forms behind a **tab switcher** (`For athletes` / `For gyms`), not two
stacked sections — a stacked layout was tried first and reviewed as confusing (you'd have to
scroll past a full athlete form with no cue that a gym form existed below it).

- Athlete categories: country availability, can't download, report/block, delete account,
  something's broken, general.
- Gym categories: list simulation events, general enquiry — plus gym name/location/website
  fields.
- Deep-link scheme: `?audience=athlete|gym&category=<code>#contact-athletes|#contact-gyms`.
  The query param drives which tab opens *and* pre-selects that form's category dropdown; the
  hash alone (no query params) also selects the right tab. Every inbound link (homepage nav,
  gym section CTA, FAQ links) uses this scheme — if you add a new link into support.html, match
  it, not the old flat `?category=gym#contact` scheme (retired 14 Sep 2026).
- Both forms POST directly to `${SUPABASE_URL}/rest/v1/contact_messages` with the public
  anon key — see Supabase section below for the schema. This is a *different* Supabase
  project (`lsxprzoxoarfakhxhoab`, production) from the retired waitlist's
  (`llkdujodseyilzbkzdbf`) — don't conflate the two.

### Design tokens

CSS custom properties in `:root` (defined per-page, not shared — each HTML file has its own
`<style>` block). Key tokens:
- `--red: #E22424` — primary action colour (matches app `Colors.red`)
- `--gold: #F2D079` — "Sun Valley", logo/brand warmth accent (per `brand/BRAND.md` §3 Swiss Alps palette — the app's own gold, `Colors.GOLD` `#F0B429`, is intentionally different; see `brand/BRAND.md` Tundra Light section)
- `--hero-bg: #0F1318` — dark hero background
- `--dark-bg: #13181F` — dark section background (gym section, footer, favicon background)
- `--light-bg: #F2F2EF` — light content section

All colours and spacing must reference these variables, not raw values.

### Fonts

Self-hosted Barlow/Barlow Condensed woff2 files under `web/assets/fonts/` (not Google Fonts —
loaded via `@font-face` in each page's own `<style>` block):
- `Barlow Condensed` — headings and buttons
- `Barlow` — body copy

---

## Supabase

**Production project:** `lsxprzoxoarfakhxhoab`. The website's contact form is the only thing
this repo talks to directly (waitlist collection was retired — do not reintroduce it here; the
app's own Supabase usage is documented in `HyPairApp/CLAUDE.md`).

**`contact_messages` table** — `type` is the *audience* (`'athlete'` or `'gym'`), matching
support.html's two tabs; `category` is free text holding that tab's own dropdown answer (the
two category lists don't overlap, so it's not a shared CHECK enum). Gym rows additionally carry
`gym_name`, `location`, `website`. A database webhook fires `notify-contact-message` (Edge
Function) on every INSERT, which emails `hello@hypair.app` with `reply_to` set to the
submitter's address — there is currently **no auto-reply email to the submitter**, only the
in-page "Thanks — your message is in" confirmation. This schema replaced an earlier flat
`gym`/`region`/`general` model on 14 Sep 2026.

**Gotcha — leftover debug objects caused a real outage, not a platform bug.** While
diagnosing a run of failed contact-form submissions, an earlier debugging pass added a
trigger that unconditionally `RAISE EXCEPTION`'d on every INSERT (to leak `current_user`/JWT
claims into the error response). It was never cleaned up. Every subsequent submission failed
with the same error regardless of what schema/RLS changes were made, which looked exactly like
a stuck PostgREST schema cache and was mis-diagnosed as a Supabase platform bug for days. It
wasn't — it was this leftover trigger, plus separately some migrations that had been committed
to git but never actually `supabase db push`ed. Both are gone now (dropped 14 Sep 2026). If
contact-form submissions ever silently fail again with no clear cause, check for
debug-only DB objects (triggers, functions) left over from a previous investigation before
assuming it's platform-side.

---

## Infrastructure

| Service | Detail |
|---|---|
| Hosting | Vercel — auto-deploys from `main` branch |
| Database | Supabase `lsxprzoxoarfakhxhoab` (production) — `contact_messages` table (active) |
| Database (legacy) | Supabase `llkdujodseyilzbkzdbf` — `waitlist` table, retired 5 Sep 2026, no longer written to |
| Email | Resend (smtp.resend.com:465) from `hello@hypair.app`, sent via the `notify-contact-message` Edge Function |
| DNS | Porkbun — DKIM, SPF, MX, DMARC all live |
| Analytics | Vercel Analytics (snippet in every HTML page) |
| Search | Google Search Console verified |

---

## SEO landing pages

Each page is self-contained HTML directly in `web/`, served at its clean URL by
`cleanUrls: true` in `web/vercel.json` — no rewrite needed (the same mechanism that
serves `web/index.html` at `/`). An earlier version of this repo nested these
under `web/site/` with explicit `vercel.json` rewrites to the clean path; that
combination of `rewrites` + `cleanUrls` proved unreliable in production (404s
that two separate fix attempts couldn't resolve), so the pages were moved to
`web/` root instead, removing the rewrites entirely.

| File | URL | Target keyword |
|---|---|---|
| `for-gyms.html` | `/for-gyms` | gym owners, SIM events |

`hyrox-dublin.html`, `tryka-dublin.html` and `hyrox-doubles-partner.html` existed here at various
points but were retired 4 Sep 2026 — a dedicated static page per event doesn't scale (a new one
would be needed every time a race is announced), and none were linked from the homepage anyway.
Their old URLs 301-redirect to `/` via `web/vercel.json`; do not recreate this pattern for a new
event without discussing it first.

When adding a new SEO page: add the file directly to `web/`, and add the URL to `web/sitemap.xml`.
Do not use a `vercel.json` rewrite for this — see above.

---

## Related repos & resources

- **App repo:** `github.com/hypair-ship-it/HyPairApp` — React Native / Expo app
- **App CLAUDE.md:** `HyPairApp/CLAUDE.md` — full app architecture, DB schema, design rules
- **Brand guide:** `brand/BRAND.md` in this repo
- **Notion HQ:** https://app.notion.com/p/32b1c734a8f781138577c191fa51d4db
- **Project map:** https://app.notion.com/p/38e1c734a8f781778290df0289ee7c79
