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
│   ├── og-image.jpg / og-card.svg   Open Graph image
│   ├── robots.txt / sitemap.xml     SEO config
│   ├── googleb13411129c6994e3.html  Google Search Console verification
│   ├── site/                        All other pages (served via Vercel rewrites)
│   │   ├── for-gyms.html            → hypair.app/for-gyms
│   │   ├── hyrox-dublin.html        → hypair.app/hyrox-dublin
│   │   ├── tryka-dublin.html        → hypair.app/tryka-dublin
│   │   ├── hyrox-doubles-partner.html → hypair.app/hyrox-doubles-partner
│   │   ├── terms.html               → hypair.app/terms
│   │   ├── privacy.html             → hypair.app/privacy
│   │   └── cookies.html             → hypair.app/cookies
│   └── assets/
│       └── icons/                   PWA notification icons
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
├── screenshots/                     App UI screenshots (used for marketing)
│
├── vercel.json                      Vercel config — must stay at repo root
└── CLAUDE.md                        This file
```

**`vercel.json` must stay at repo root** — Vercel reads it before applying `rootDirectory`.

---

## web/index.html architecture

Everything — HTML, CSS, and JavaScript — lives in `web/index.html`. No build step,
no package manager, no framework. Preview locally:

```bash
python3 -m http.server 3456 --directory web
```

Or use the `.claude/launch.json` config which is already set up.

### Page states

Two states toggled by JavaScript:
- **Waitlist state** (`#waitlist-section`): hero with email capture form
- **Success state** (`#success-section`): shown after form submission

### Supabase integration (active)

Waitlist emails are written to the `waitlist` table in Supabase project
`llkdujodseyilzbkzdbf`. Constants at the top of the `<script>` block:
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`

A welcome email edge function (`send-welcome-email`) fires on INSERT via a
Supabase webhook.

### Design tokens

CSS custom properties in `:root`. Key tokens:
- `--red: #E22424` — primary action colour (matches app `Colors.red`)
- `--gold: #D4AA50` — achievement / race accent (matches app `Colors.gold`)
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
| Database | Supabase `llkdujodseyilzbkzdbf` — `waitlist` table |
| Email | Resend (smtp.resend.com:465) from `hello@hypair.app` |
| DNS | Porkbun — DKIM, SPF, MX, DMARC all live |
| Analytics | Vercel Analytics (snippet in every HTML page) |
| Search | Google Search Console verified |

---

## SEO landing pages

Each page is self-contained HTML in `web/site/`, served at a clean URL via `vercel.json` rewrites:

| File | URL | Target keyword |
|---|---|---|
| `for-gyms.html` | `/for-gyms` | gym owners, SIM events |
| `hyrox-dublin.html` | `/hyrox-dublin` | HYROX Dublin partner |
| `tryka-dublin.html` | `/tryka-dublin` | Tryka Dublin partner |
| `hyrox-doubles-partner.html` | `/hyrox-doubles-partner` | HYROX doubles partner |

When adding a new SEO page: add the file to `web/site/`, add a rewrite to `vercel.json`, and add the URL to `web/sitemap.xml`.

---

## Related repos & resources

- **App repo:** `github.com/hypair-ship-it/HyPairApp` — React Native / Expo app
- **App CLAUDE.md:** `HyPairApp/CLAUDE.md` — full app architecture, DB schema, design rules
- **Brand guide:** `brand/BRAND.md` in this repo
- **Notion HQ:** https://app.notion.com/p/32b1c734a8f781138577c191fa51d4db
- **Project map:** https://app.notion.com/p/38e1c734a8f781778290df0289ee7c79
