# HyPair Brand Guidelines

HyPair is a race partner matching app for hybrid athletes. These guidelines exist to keep the brand consistent across every touchpoint — the app, the website, social media, and any future marketing materials.

---

## 1. Brand Identity

### Mission
Connect hybrid athletes with their perfect race partner — same event, same pace, same mindset.

### Brand Personality
- **Energetic** — we speak to athletes who push hard
- **Direct** — no fluff, no filler, just what matters
- **Community-driven** — we exist because athletes need each other
- **Credible** — built by athletes, for athletes

### Tone of Voice
- Bold and punchy. Short sentences. Strong verbs.
- Speak to the problem first, then the solution.
- Never corporate. Never overly polished.
- Use "you" not "our users" or "athletes".
- OK to use caps for emphasis: HYROX, NO PARTNER. NO RACE.

**Do:** "No partner. No race. We built the fix."
**Don't:** "HyPair provides a comprehensive matching solution for hybrid fitness enthusiasts."

---

## 2. Logo

### The Mark
The HyPair icon is a geometric symbol combining a U-shape (representing two athletes) and an arch with a circle — referencing the structure of a race. It is the primary brand asset and should be treated with care.

### Versions
| Version | Usage |
|---|---|
| Icon mark + wordmark (full) | Primary — use wherever space allows |
| Icon mark only | App icon, favicon, small placements |
| Wordmark only | Where the icon has already appeared nearby |

### Colours
| Background | Icon colour | Wordmark colour |
|---|---|---|
| Forest green `#2d4a2d` | Gold `#F8C662` | Gold `#F8C662` |
| Black `#0a0a0a` | Gold `#F8C662` | Gold `#F8C662` |
| White | Navy `#2C263F` | Navy `#2C263F` |
| Gold `#F8C662` | Navy `#2C263F` | Navy `#2C263F` |

### Clear Space
Always maintain clear space around the logo equal to the height of the letter "H" in the wordmark on all sides. Never crowd the logo.

### Logo Don'ts
- Do not change the logo colours outside of the approved combinations above
- Do not stretch, rotate, or distort the mark
- Do not place the logo on a busy photo without a solid background behind it
- Do not recreate the logo in a different typeface
- Do not add drop shadows or effects to the logo
- Do not use the navy icon on dark backgrounds — it will disappear

---

## 3. Colour Palette

### Primary Colours

| Name | Hex | RGB | Usage |
|---|---|---|---|
| Forest Green | `#2d4a2d` | 45, 74, 45 | Primary background |
| Dark Green | `#1a2e1a` | 26, 46, 26 | Darker background, nav |
| Gold | `#F8C662` | 248, 198, 98 | Primary accent, CTAs, logo |
| White | `#ffffff` | 255, 255, 255 | Body text on dark backgrounds |

### Secondary Colours

| Name | Hex | RGB | Usage |
|---|---|---|---|
| Navy | `#2C263F` | 44, 38, 63 | Icon on light backgrounds |
| Black | `#0a0a0a` | 10, 10, 10 | Alternative dark background |
| Dark Navy | `#12080e` | 18, 14, 30 | Story/editorial posts |

### Functional Colours

| Name | Hex | Usage |
|---|---|---|
| White 60% | `rgba(255,255,255,0.6)` | Body text, secondary content |
| White 35% | `rgba(255,255,255,0.35)` | Placeholder text, muted labels |
| White 15% | `rgba(255,255,255,0.15)` | Borders, dividers |
| Gold dim | `rgba(248,198,98,0.12)` | Icon backgrounds, subtle highlights |
| Gold border | `rgba(248,198,98,0.35)` | Chip borders, card accents |

### Colour Rules
- Gold is always the action colour — buttons, CTAs, key highlights
- Never use gold as a background for large areas
- Green is the brand home — default to dark green for backgrounds
- Black backgrounds work for high-contrast social posts
- Never use pure white as a background — it conflicts with the brand warmth

---

## 4. Typography

### Typefaces

| Role | Font | Weight | Usage |
|---|---|---|---|
| Display / Headlines | Barlow Condensed | 900 (Black) | Hero headlines, post headlines, app screens |
| Display / Sub-headlines | Barlow Condensed | 700 (Bold) | Section headers, card titles |
| Body | Barlow | 300 (Light) | Taglines, descriptions, body copy |
| Body emphasis | Barlow | 500 (Medium) | Feature titles, labels |

Both fonts are available free on Google Fonts: [fonts.google.com](https://fonts.google.com)

### Type Scale (web)

| Role | Size | Weight | Transform |
|---|---|---|---|
| Hero headline | clamp(44px, 10vw, 64px) | 900 | Uppercase |
| Section headline | 40–48px | 700 | Uppercase |
| Feature title | 14–16px | 500 | Sentence case |
| Body / tagline | 15–17px | 300 | Sentence case |
| Labels / eyebrow | 11px | 400 | Uppercase, 2px letter-spacing |
| Small / legal | 11–12px | 400 | Sentence case |

### Type Rules
- Headlines are always uppercase in Barlow Condensed
- Body copy is always sentence case — never ALL CAPS for paragraphs
- Line height for body: 1.6–1.7
- Line height for display: 0.95–1.0 (tight)
- Letter spacing for eyebrow labels: 2–2.5px
- Do not use weights below 300 or above 900
- Do not mix more than two weights in a single composition

---

## 5. Social Media

### Supported Races (current)
Always refer to these in this order when listing:
1. HYROX (all caps)
2. Spartan
3. Tryka
4. Athex

"+ more coming" when listing all four together.

### Instagram Handle
`@hypair.app`

### Post Format
- Square 1:1 (1080×1080px) for feed posts
- Always include "link in bio" in captions — never put URLs on graphics
- Do not put the handle on the graphic — it is visible from the account
- Caption structure: hook → problem/solution → CTA → hashtags

### Core Hashtags
```
#HyPair #HYROX #HYROXdoubles #HybridAthlete #RacePartner
#HybridTraining #FunctionalFitness #Spartan #Tryka #Athex
```

### Background Styles (approved)
| Style | Hex | When to use |
|---|---|---|
| Dark green | `#1a2e1a` | Default, problem/solution posts |
| Black | `#0a0a0a` | High contrast, bold statements |
| Forest green | `#2d4a2d` | Waitlist, community posts |
| Dark navy | `#12080e` | Founder story, personal posts |

---

## 6. Tech Stack Reference

| Layer | Tool | Notes |
|---|---|---|
| Website | Vercel | Auto-deploys from GitHub main branch |
| Domain | hypair.app via Porkbun | DNS pointed to Vercel |
| Database | Supabase (PostgreSQL) | Waitlist table, future user data |
| Email | Cloudflare Email Routing → Gmail | Forward only for now |
| Mobile app | Expo (React Native) | Planned — iOS + Android |
| Email sending | Resend (planned) | Transactional + launch emails |

### Supabase Project
- Project URL: `https://llkdujodseyilzbkzdbf.supabase.co`
- Tables: `waitlist (id, email, created_at)`

---

## 7. Brand Assets Checklist

- [x] SVG logo (transparent background, colour version)
- [x] SVG logo (transparent background, black/white version)
- [x] Waitlist website live at hypair.app
- [x] Instagram post graphics (4 × 1080px)
- [ ] App icon (1024×1024px)
- [ ] Favicon (32×32px, 16×16px)
- [ ] White logo version for dark app backgrounds
- [ ] Figma brand file

---

## 8. File Structure

```
hypair-waitlist/
├── index.html          — Waitlist landing page
├── BRAND.md            — This file
└── brand/
    ├── logo/
    │   ├── hypair-logo-colour.svg
    │   ├── hypair-logo-white.svg
    │   └── hypair-icon-only.svg
    └── social/
        ├── hypair_post1_problem.jpg
        ├── hypair_post2_solution.jpg
        ├── hypair_post3_waitlist.jpg
        └── hypair_post4_founder.jpg
```

---

*Last updated: March 2026. Maintained by the HyPair founding team.*
