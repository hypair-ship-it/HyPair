# Thursday 15 Oct 2026 feature post: ticket filter

Two visuals, in this order (Instagram carousel of 2, 4:5):
1. ticket-registration.mp4 (6 s loop, 1080x1350, H.264): "Got a ticket? Say so." The join sheet with the "I have a ticket for this event" box switching on. Same thing as ticket-registration.gif (720x900, for the Facebook Page or anywhere a GIF works) and the two still frames reg-frame-off.png / reg-frame-on.png.
2. slide2-partner-filter.png (= ticket-filter.png): "Ticket or no ticket. Filter for both." Find a Partner with the Has Ticket filter on.
Source screens: HYROX Manchester as a sandbox demo athlete; the stale countdown pill was blanked; nothing was saved in the app while shooting.
Post on: Instagram (hypair.app) and the Facebook Page. Not in groups.

## Instagram caption (end with "link in bio")

Got your ticket already? Or still deciding? 🎟️

In Find a Partner you can filter athletes by ticket status: Has Ticket or No Ticket. Mark your own ticket on your entry too, so the right people find you.

Free on the App Store and Google Play. Link in bio.

## Facebook Page caption (same, with the link)

Got your ticket already? Or still deciding? 🎟️

In Find a Partner you can filter athletes by ticket status: Has Ticket or No Ticket. Mark your own ticket on your entry too, so the right people find you.

Free on the App Store and Google Play: https://hypair.app

## Notes
- Accurate to the app: the Find a Partner screen has an All / Has Ticket / No Ticket toggle, and the entry page has an "Add ticket" button.
- Demo athletes only (sandbox), not real people. No claim that real athletes are signed up.
- Reuse the 8 Oct Match score template (features/2026-10-08-match-score/match-score-london.html).

## Light-theme, playful version (15 Oct, Ante asked for light theme and "a bit of fun")
Cream background (#EDE7E3), H app icon, gold highlighter on the second headline line, tilted stickers. App screens are the real light theme (sandbox demo athletes).
1. ticket-registration-light.mp4 (7 s loop, 1080x1350, H.264) - "Got a ticket? Say so." with the box ticking; the sticker flips from "Not yet? Fine too" to "Ticket in hand". Also ticket-registration-light.gif (720x900) and stills light-slide1-off.png / light-slide1-on.png.
2. slide2-partner-filter-light.png - "Ticket in hand? Or still looking?" with stickers "Has ticket" and "No ticket? Filter that too".
Rebuild: python3 build_light.py (needs light-reg-off-clean.png, light-reg-on-clean.png, light-filter-has.png in this folder).
The dark versions (ticket-registration.mp4/.gif, slide2-partner-filter.png) are kept as an alternative.

## Final direction (15 Oct, Ante): dark app screens on a plain cream background, no stickers, no highlighter
Use these for the post:
1. ticket-registration-mixed.mp4 (7 s loop, 1080x1350, H.264) - "Got a ticket? Say so." Stills: mix-slide1-off.png / mix-slide1-on.png. GIF: ticket-registration-mixed.gif (720x900).
2. mix-slide2.png - "Ticket or no ticket. Filter for both."
Rebuild: python3 build_mixed.py
The light-theme "playful" set (light-*.png, ticket-registration-light.*) and the all-dark set are kept as alternatives.

## FINAL captions (15 Oct, with Ante's added hint). Images: ticket-registration-mixed.mp4 then mix-slide2.png

Instagram:

Got your ticket but no one to race with? 🎟️

In Find a Partner you can filter for athletes who don't have a ticket yet. No ticket yourself? See who already has theirs and start the conversation.

Tick "I have a ticket" on your entry so other athletes can find you by ticket status.

Free on the App Store and Google Play. Link in bio.

Facebook Page: same text, last line "Free on the App Store and Google Play: https://hypair.app"

Wording note: the post does NOT say that having a partner with a ticket gets you into the race. Entry rules differ by event (each athlete or each team may need a ticket) and we have not checked them, so the text only says you can see who has one and start the conversation.
