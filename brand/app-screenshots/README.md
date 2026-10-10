# App screenshots for store listings and marketing

Not served by the website (that is `web/assets/screenshots/`, which holds only real-app pictures used on
the site). Everything here is for store listings, social posts, decks and similar.

Each folder is one capture session, named `YYYY-MM-<purpose>`:

| Folder | What it holds |
|---|---|
| `originals/` | Full-size PNGs straight from the iPhone 17 Pro Simulator (1206x2622). Use these for the App Store and for anything else that is not Google Play. |
| `play-store/` | The eight JPEGs uploaded to Google Play, numbered in upload order (1206x2387, trimmed to Google's 2:1 limit, no transparency). |
| `play-store-extras/` | Two spare Play-ready pictures. |

## Where the data comes from
Every picture is the HyPair Staging app on the SANDBOX database with made-up demo accounts, never production
and never a real athlete. The people are invented; their profile photos are free Pexels stock portraits of
strangers (credits in `HyPairApp/scripts/screenshot-seed-avatars/CREDITS.md`). The app code, the demo seed
(`HyPairApp/scripts/screenshot-seed.sh`) and the capture guide (`HyPairApp/docs/play-store-screenshot-guide.md`)
live in the HyPairApp repo. Re-run the seed before any new capture session.

## Rules
- Do not use these on the website as proof of real users, and do not present the people as real members.
- A new session gets its own folder; do not overwrite an old one.
