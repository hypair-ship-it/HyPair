# HyPair — Master Launch Tracker

> Updated: 2026-05-31
> Target: Beta v1 → App Store public launch

---

## 🔴 PHASE 1 — Business & Legal Foundation

### Company registration
- [ ] **Register HyPair Ltd** at cro.ie (~€50) or Formations.ie same-day (~€150)
- [ ] **Apply for DUNS number** at dnb.com — do this the same day company registers (takes 5–14 business days)
- [ ] **Open business bank account** (needed for Apple/Google payouts)
- [ ] **Set up hello@hypair.app** as a proper business email (Google Workspace ~€6/mo)

### Apple
- [ ] **Enroll Apple Developer Program** at developer.apple.com/enroll — $99/yr as organisation (needs company + DUNS)
- [ ] **Get Apple Team ID** from Membership → fill in `eas.json`

### Google Play
- [ ] **Register Google Play Developer account** at play.google.com/console — $25 one-time (can do today, no company needed)

### Legal policies
- [ ] **Replace Privacy Policy with iubenda** — sign up at iubenda.com, use their wizard (GDPR + CCPA auto-updating, ~€9–29/mo, Apple/Google accepted). Update `privacy.html` with their version.
- [ ] **Generate Terms & Conditions via iubenda** — same wizard, covers user accounts, acceptable use, IP, liability, governing law (Ireland)
- [ ] **Publish Terms at hypair.app/terms.html** — required for App Store
- [ ] **Add Terms link to app** — Settings screen already has placeholder, wire it to live URL
- [ ] **Cookie policy** — iubenda generates this too, add to website footer
- [ ] **Have solicitor review** both policies when registering company (one-time, ~€300–500)

---

## 🟠 PHASE 2 — Technical Build Checklist

### Completed
- [x] All icons correct sizes (icon.png 1024×1024, android 512×512, notification 96×96)
- [x] Privacy Policy live at hypair.app/privacy.html
- [x] Database migrations run (RLS security fixes + start_time column)
- [x] All UX/UI polish committed (Gemini review rounds 1–5)

### Remaining
- [ ] **Set EXPO_PUBLIC_SENTRY_DSN** — create project at sentry.io, add DSN to `.env` and EAS env vars
- [ ] **Android build** — `eas login` then `eas build --profile preview --platform android`
- [ ] **iOS build** — blocked on Apple Developer account
- [ ] **iOS TestFlight** — `eas submit --platform ios` after build, then invite internal testers in App Store Connect

### Pre-launch code items
- [ ] **NSLocationWhenInUseUsageDescription** — add to `app.json` if location used anywhere
- [ ] **`eas build --profile production`** for final App Store submission (different from preview)

---

## 🟡 PHASE 3 — Quality & Testing

### Smoke test 6 core flows (real device, not Simulator)
| Flow | Status |
|---|---|
| Sign up → onboarding → home | ⬜ |
| Browse event → register → find partner | ⬜ |
| Send connect request → accept → chat | ⬜ |
| Two-step lock-in → paired state | ⬜ |
| Gym owner create event → manage signups | ⬜ |
| Settings → change email → sign out → sign back in | ⬜ |

### Device testing
- [ ] Dynamic Island (iPhone 15 Pro) — safe area / notch
- [ ] iPhone SE — small screen, keyboard avoidance on all forms
- [ ] Android — mid-range device (Pixel or Samsung)
- [ ] iPad — excluded from build, verify it's blocked correctly

### Technical checks
- [ ] Sentry receiving crashes from production build
- [ ] Supabase realtime working on device (not just Simulator)
- [ ] Push notifications end-to-end (send request → notification arrives)
- [ ] Photo upload from camera roll on real device
- [ ] Deep links working (if implemented)

---

## 🏪 PHASE 4 — App Store Assets & Listing

### Screenshots (required before submission)
- [ ] **iPhone 6.5"** — 1284×2778px, minimum 3, up to 10
- [ ] **iPhone 5.5"** — 1242×2208px (required as well)
- [ ] **Screens to show:** Home feed, Events browse, Partner browse, Chat + lock-in, Profile, Gym owner manage
- [ ] **Add text overlays** — short captions on each screenshot ("Find your race partner", "Matched by pace")

### App listing copy (iOS + Android)
- [ ] **App name:** HyPair — Race Partner Finder *(30 chars max iOS)*
- [ ] **Subtitle (iOS):** Find your HYROX doubles match *(30 chars)*
- [ ] **Short description (Google Play):** Find a doubles partner for HYROX and TRYKA races — matched by pace, goal and event. *(80 chars)*
- [ ] **Full description** — write 3–4 paragraphs covering: what it does, who it's for, key features, call to action *(4000 chars max)*
- [ ] **Keywords (iOS):** HYROX, TRYKA, doubles, race partner, hybrid race, fitness, athlete, partner matching *(100 chars)*
- [ ] **Support URL:** hypair.app or a dedicated support page
- [ ] **Marketing URL:** hypair.app
- [ ] **Privacy Policy URL:** hypair.app/privacy.html ✅
- [ ] **Terms URL:** hypair.app/terms.html (once created)

### App Store Connect setup (iOS)
- [ ] Create app record in App Store Connect
- [ ] Fill in Privacy Nutrition Label (data types collected, usage)
- [ ] Age rating questionnaire (result should be 17+ or 12+)
- [ ] Content rights declaration
- [ ] App Review notes (test account credentials for Apple reviewer)

### Google Play setup
- [ ] Create app in Google Play Console
- [ ] Feature graphic — 1024×500px banner (HyPair brand, "Meet your match")
- [ ] Data safety section (matches Privacy Policy)
- [ ] Content rating questionnaire
- [ ] Target audience (17+)
- [ ] App category: Health & Fitness

---

## 📣 PHASE 5 — Marketing Campaign

### Website
- [ ] **Add App Store / TestFlight download button** once live — replace or supplement waitlist form
- [ ] **Add app screenshots to website** — show the actual product
- [ ] **Add social proof** once available — number of athletes, events covered

### Pre-launch (before App Store approval)
- [ ] **Email waitlist** — announce beta is coming, invite to TestFlight (needs ~200 word email)
- [ ] **Instagram announcement post** @hypair.app — "HyPair beta is launching. Here's what it looks like." (screenshots + reel)
- [ ] **Facebook post** on HyPair page
- [ ] **Post in HYROX community groups** — Facebook groups (HYROX Ireland, HYROX UK, HYROX Global), Reddit r/hyrox
- [ ] **Post in TRYKA community** — wherever their community lives online
- [ ] **Personal outreach** — direct message to athletes you know who do doubles

### Launch week
- [ ] **App Store launch post** — "HyPair is live. Download now." on Instagram + Facebook
- [ ] **Story series** — how to sign up, find a partner, lock in (3-part story walkthrough)
- [ ] **Reels / short video** — 30–60 second demo of the core flow (find event → find partner → chat → paired)
- [ ] **Email to full waitlist** — "You're in. Download here." with App Store links
- [ ] **Post in every relevant fitness/HYROX community** — with App Store link

### Ongoing
- [ ] **Content calendar** — 3x per week Instagram: athlete features, race tips, partner success stories
- [ ] **HYROX event presence** — attend events, hand out cards, demo the app
- [ ] **Gym outreach** — contact CrossFit boxes and HYROX gyms, offer to set up their gym as a SIM event venue
- [ ] **PR outreach** — fitness media (Men's Health, Women's Health, Running Magazine Ireland, HYROX official channels)
- [ ] **Influencer outreach** — HYROX athletes with 5k–50k following, offer early access

### App Store Optimisation (ASO)
- [ ] **A/B test screenshots** — App Store Connect allows this after launch
- [ ] **Monitor keyword rankings** — use AppFollow or Sensor Tower
- [ ] **Respond to every early review** — critical for algorithm ranking

---

## ⚙️ PHASE 6 — Post-Launch Features (Roadmap)

### Near-term (v1.1)
- [ ] Push notifications end-to-end (Expo push tokens → Supabase edge function)
- [ ] In-app notification badge on tab bar
- [ ] Face ID / Touch ID login
- [ ] Profile photo crop/zoom on upload
- [ ] Deep links — share event, share profile

### Medium-term (v1.5)
- [ ] Wave management for gym owners
- [ ] Analytics dashboard for gym owners
- [ ] Dark/light mode toggle
- [ ] Chat inbox tab
- [ ] Community feed

### Long-term
- [ ] Spartan Race + Athex support
- [ ] Strava / Garmin integration
- [ ] Subscription / Pro plan
- [ ] Push notification campaigns for gym owners

---

## ✅ Done

### This session
- [x] Full Gemini UX/UI review — 5 rounds, ~30 fixes across 21 files
- [x] Green purge across entire codebase — all Colors.green replaced
- [x] Profile: sign-out button, edit+settings icons safe-area fix
- [x] Database migrations — RLS security fixes + start_time column
- [x] Website copy updated — races, features, nav tag
- [x] Privacy Policy draft created at hypair.app/privacy.html
- [x] All assets correct sizes — icons, splash, notification, adaptive
- [x] TRYKA tab colour softened
- [x] Card badge alignment fixed across Home + Events
- [x] Capture script rewritten with Supabase ID fetch + zip output

### Build & config
- [x] `tsc --noEmit` passes with zero errors
- [x] Bundle IDs, version, build number set
- [x] App icon, splash screen, Android adaptive icon all sized correctly
- [x] EAS build config (development / preview / production profiles)
- [x] Dark mode, portrait lock, iPad excluded

### Security
- [x] All RLS policies applied (own-row rules, event-owner rules, partner visibility)
- [x] Messages injection hole closed
- [x] Profiles block unauthenticated reads
- [x] No service-role key in client code

### Features
- [x] Full auth flow (sign-up, log-in, forgot password, OTP verify)
- [x] 6-step onboarding
- [x] Event browse, register, partner search
- [x] Connect / accept / decline / revoke requests
- [x] Real-time chat, two-step lock-in, cancel pairing
- [x] Home activity feed with unread badges
- [x] Gym owner: create events, manage signups, wave assignment
- [x] Organiser/admin mode with AsyncStorage cache
- [x] Race history log with delete confirmation
- [x] Sign out from profile
