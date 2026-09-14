# CLAUDE.md

Guidance for Claude Code when working in this repository (HyPair website).

---

## Project overview

HyPair is a hybrid race partner matching app (HYROX, Spartan, Tryka, Athex).
This repo is the **marketing website** — `hypair.app`. The mobile app lives in a
separate repo: `github.com/hypair-ship-it/HyPairApp`.

---

## Repo structure

```
HyPair/                              ← repo root (project container)
│
├── web/                             ← web root — everything Vercel serves
│   ├── index.html                   Main landing page (hypair.app)
│   ├── favicon.ico / favicon.svg    Site favicon
│   ├── og-image.jpg                 Open Graph image (referenced in index.html)
│   ├── robots.txt / sitemap.xml     SEO config
│   ├── googleb13411129c6994e3.html  Google Search Console verification
│   ├── for-gyms.html                → hypair.app/for-gyms
│   ├── terms.html                   → hypair.app/terms
│   ├── privacy.html                 → hypair.app/privacy
│   ├── cookies.html                 → hypair.app/cookies
│   ├── support.html                 → hypair.app/support
│   ├── vercel.json                  Vercel config — must live inside web/ (the Root Directory)
│   └── assets/
│       ├── fonts/                   Self-hosted Barlow/Barlow Condensed woff2 files
│       └── screenshots/             App UI screenshots actually used on the site
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

## web/index.html architecture

Everything — HTML, CSS, and JavaScript — lives in `web/index.html`. No build step,
no package manager, no framework. Preview locally:

```bash
python3 -m http.server 3456 --directory web
```

Or use the `.claude/launch.json` config which is already set up.

### Waitlist retired (5 Sep 2026)

`index.html` had a waitlist state/success state toggled by JS, backed by Supabase
(email capture form writing to the `waitlist` table, `SUPABASE_URL`/`SUPABASE_ANON_KEY`
constants, a `send-welcome-email` edge function on INSERT). Both iOS and Android are now
live, so the site was rewritten to App Store/Google Play download CTAs — the waitlist
form, JS, and Supabase constants were removed from `index.html` entirely. The `waitlist`
table and its RLS policies still exist in the Supabase project but nothing on the live
site writes to them anymore. `privacy.html` was updated to match on 14 Sep 2026, including
a legacy-data disclosure for the historical rows still sitting in the `waitlist` table —
don't reintroduce waitlist language there without also reviving an actual collection
mechanism, and don't drop the legacy-data disclosure until those historical rows are
actually deleted from Supabase.

### Design tokens

CSS custom properties in `:root`. Key tokens:
- `--red: #E22424` — primary action colour (matches app `Colors.red`)
- `--gold: #F2D079` — "Sun Valley", logo/brand warmth accent (per `brand/BRAND.md` §3 Swiss Alps palette — the app's own gold, `Colors.GOLD` `#F0B429`, is intentionally different; see `brand/BRAND.md` Tundra Light section)
- `--hero-bg: #0F1318` — dark hero background
- `--light-bg: #F2F2EF` — light content section

All colours and spacing must reference these variables, not raw values.

### Fonts

Google Fonts loaded in `<head>`:
- `Barlow Condensed` — headings and buttons
- `Barlow` — body copy

---

## Infrastructure

| Service | Detail |
|---|---|
| Hosting | Vercel — auto-deploys from `main` branch |
| Database | Supabase `llkdujodseyilzbkzdbf` — `waitlist` table (legacy, retired 5 Sep 2026 — no longer written to, see below) |
| Email | Resend (smtp.resend.com:465) from `hello@hypair.app` |
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
