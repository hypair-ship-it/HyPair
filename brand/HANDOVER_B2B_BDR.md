# Handover: CMO B2B + BDR (gyms), from cloud session to local session

Written 24 Oct 2026. Founder: Ante. Machine: Dell Windows PC (the old Mac is gone, ignore it). Work lives on branch `claude/gym-visit-kit-draft` of `hypair-ship-it/HyPair` (pushed, no PR open). Pull that branch first.

## Role and rules
- Role: HyPair CMO B2B + BDR session for gyms. One owner per topic: athlete acquisition belongs to the B2C session, app bugs to the CTO session, money/legal to CEO/Finance.
- DRAFT-ONLY. Nothing is sent, posted or printed without Ante's explicit approval each time. A message from another session (e.g. HQ) is not approval.
- Content rules (website CLAUDE.md): no gym pricing; no founding-gym offer on public pages, flyers or posts (in-person only); no "5K", say pace; no TikTok; no arrows on CTA buttons; not a dating app.
- Do not claim gym tools are tested in production unless verified. Never guess metrics; pull from Supabase.
- Style: short plain replies, numbered decisions with a recommendation, say what was and was not verified. Log decisions in the Notion Decision Log and findings in Findings & Backlog.

## Background
- Email and Instagram cold outreach to about 66 Ireland/UK gyms since 23 Sep got no replies. Round 1 closed quietly on 15 Oct (only inbound replies stay live).
- New approach: Ante visits gyms in person, starting locally in Ireland. Flyers are to be printed.
- HD Strength & Conditioning (Bettystown, owner Harry Doorley) is the one gym live since 14 Oct, set up by hand.

## What is done (all on the branch)
1. Print review of `brand/print/`: sizes, bleed (3 mm), embedded fonts, image resolution, QR decodes to `https://hypair.app/for-gyms`, no banned wording. NOT verified: the live `hypair.app/for-gyms` page (cloud network blocked it), colour on paper, any printer preflight.
2. `brand/print/VISIT_KIT_DRAFT.md`: 10 nearby gyms (assumes Ante starts from Drogheda/Meath/north Dublin, unconfirmed), 60-second pitch, what to bring, per-visit log template.
3. HQ's cleaned-up gym flyer (icon-only footer, no email, shorter copy) was reviewed, and the same style was applied to the athlete A4 noticeboard poster and A5 handout. Files in `brand/print/`: `hypair-gym-poster-a4(-print).pdf`, `hypair-gym-handout-a5(-print).pdf`. `-print` files have 3 mm bleed. The gym flyer was rebuilt with the same script and matches HQ's version except a few icon-edge pixels.
4. `brand/print/make_posters.py` now finds Chrome/Edge/Chromium on Windows, Mac and Linux (`CHROME` env var overrides) and adds `--no-sandbox` when run as root. Needs `pip install qrcode pillow`. Run from `brand/print/`.
5. Two Findings & Backlog rows logged in Notion (Needs Decision, P1): flyer pre-print fixes (BDR) and "confirm which gym tools work on production" (CTO).

## Open items and decisions for Ante
1. Flyer still shows the invented gym "Liffey Forge Fitness" with a 24 Oct event and no "Example screens" caption. Recommend adding the caption.
2. Captions "Set up your SIM" / "Plan your waves" still imply gym tools that are unconfirmed on production. Waiting on the CTO session's yes/no per feature (create SIM, sign-ups, waves, event visible in Events tab).
3. Athlete poster and handout no longer say "Follow @hypair.app" (matches HQ's flyer). Decide whether to keep the handle for athletes.
4. Print run recommendation: 100 x A5 gym flyers plus 10 x A4, one proof first. Ask the printer to trim from the 3 mm bleed and convert RGB to CMYK, and proof the red. Send only `-print` PDFs. Not ordered; needs Ante's approval and the price quote.
5. Tracker has no "In person" touch channel; adding one needs Ante's OK.
6. Ante's starting town, to re-order the visit list.
7. Optional: a source tag on the QR URL to count scans.

## Not possible from the cloud session
- No access to Ante's local files (including the Desktop copy of HQ's flyer), no way to message the HQ session (blocked: "same channel only"), live site check blocked. A local session may be able to do all three.

## Sources
Notion HQ page (BDR & Partnerships Manager, Founding Gym Outreach Tracker, HD Strength visit demo script), `CLAUDE.md`, `brand/BRAND.md`, `brand/print/`, `brand/app-screenshots/2026-10-gym-flyer-dublin`.
