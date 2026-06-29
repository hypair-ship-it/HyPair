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
/
├── index.html                     Main landing page
├── for-gyms.html                  SEO landing page — gym owners
├── hyrox-dublin.html              SEO landing page — HYROX Dublin
├── tryka-dublin.html              SEO landing page — Tryka Dublin
├── hyrox-doubles-partner.html     SEO landing page — doubles partner search
├── terms.html                     Terms of Service
├── privacy.html                   Privacy Policy
├── cookies.html                   Cookie Policy
│
├── favicon.ico / favicon.svg      Site favicon (both formats)
├── og-image.jpg                   Open Graph image (1200×630)
├── og-card.svg                    OG card source
├── robots.txt                     Search crawler rules
├── sitemap.xml                    XML sitemap
├── vercel.json                    Vercel config (clean URLs)
├── googleb13411129c6994e3.html    Google Search Console verification
│
├── brand/
│   ├── logo/
│   │   ├── swiss-alps/            Dark-theme logo set (SVG, PNG, ICO)
│   │   └── tundra-light/          Light-theme logo set (SVG, PNG, ICO)
│   └── social/
│       ├── swiss-alps/            Dark-theme social cover images (all platforms)
│       ├── tundra-light/          Light-theme social cover images (all platforms)
│       ├── posts/                 Exported social post images
│       └── reference/             Reference images (hyrox-profile.jpg, etc.)
│
├── assets/
│   └── icons/                     App icons (notification-icon, notification-icon-192)
│
└── BRAND.md                       Design system reference (colours, fonts, tokens)
```

**All HTML files must remain at root** — their paths are live URLs indexed by
Google. Do not move them without adding Vercel rewrites first.

---

## index.html architecture

Everything — HTML, CSS, and JavaScript — lives in `index.html`. No build step,
no package manager, no framework. Open directly in a browser to preview, or run:

```bash
python3 -m http.server 3456
```

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
- `--red: #E22424` — primary action colour
- `--gold: #D4AA50` — achievement / race accent
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

Each SEO page is self-contained HTML at its own URL:

| File | URL | Target keyword |
|---|---|---|
| `for-gyms.html` | `/for-gyms` | gym owners, SIM events |
| `hyrox-dublin.html` | `/hyrox-dublin` | HYROX Dublin partner |
| `tryka-dublin.html` | `/tryka-dublin` | Tryka Dublin partner |
| `hyrox-doubles-partner.html` | `/hyrox-doubles-partner` | HYROX doubles partner |

When adding a new SEO page: add it to `sitemap.xml` and update `robots.txt` if needed.

---

## Related repos & resources

- **App repo:** `github.com/hypair-ship-it/HyPairApp` (React Native / Expo)
- **App CLAUDE.md:** in root of HyPairApp repo — full app context
- **Notion HQ:** https://app.notion.com/p/32b1c734a8f781138577c191fa51d4db
- **Brand guide:** `BRAND.md` in this repo
