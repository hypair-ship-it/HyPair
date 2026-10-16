# B2C social planner: events and weekly rhythm

Created 2 Oct 2026. Athlete-facing only (gyms are the B2B session's). Website copy is not in here.
Source for events: the app's events table (production) checked against hyrox.com/find-my-race and tryka.fit on 2 Oct 2026.

## Ground rules (decided 1-2 Oct)
- Event pushes happen in Facebook groups. Own channels (Instagram, Facebook Page) get Thursday feature posts only.
- No upcoming-races roundups, no explainers, no Story polls or question stickers (too few followers to answer).
- No outreach to individual users. Grow the number of athletes per race instead.
- US/Canada copy never mentions Tryka. Canada is paused (AthleteField), so Toronto, Vancouver and Ottawa are out.
- Never claim real athletes are signed up when they are not. Screens are from the staging build with sandbox demo profiles.
- No "5K", no arrow on buttons, no gym pricing or founding-gym offer, nothing dating-like.
- Tryka formats (confirmed by Natalia, 9 Oct): full TRYKA = TRYKA 800, the other is TRYKA 500. The app's 500/800 format names are correct; copy says "Tryka 500" / "Tryka 800" (or "full Tryka").

## The three moments (reworked 2 Oct, approved by Ante)
Each one is a different kind of post, so a group never sees the same thing twice. Posts in the same group are at least 10-14 days apart.
1. **On sale: a partner thread.** A community post, not an ad. "HYROX {city} partner thread: drop your division, pace, goal and where you are based."
   The app link goes in the first comment, not in the post. The people who comment are the supply, and they are easier to match in the app.
   Trigger: the event's button on hyrox.com/find-my-race flips from FIND OUT MORE to BUY TICKETS (Tryka: tryka.fit announces the series).
2. **Mid-countdown (about 3 weeks out): "Partner dropped out?"** The relatable problem post, with the carousel slide and a fresh Find a Partner screenshot.
3. **Final week (6-7 days out): last-minute.** The Boston pattern, 4 slides.

Rules: never claim real athletes are signed up when they are not. If a group removes a post, stop posting there and only comment.
Text for every moment is in `posts/_moments/moments.md`. The first thread (Tampa) is in `posts/_moments/tampa-moment1-thread.md`.

Every event folder (brand/social/posts/events/<city>/) has a `post-text.txt` with the group, who to post as, the time, the images and the text to copy.

## Event plan (rebuilt 9 Oct)
- Moment 1 wording changed 12 Oct (Natalia): "Got your ticket?" assumed everyone has a ticket. New wording: "Ready to race but no doubles partner yet?" (images: "Ready to race? Need a partner?"). Applied to the unposted events (Melbourne, Chicago, Manchester, Glasgow, Phoenix), the generator `_templates/moments/make_moment1.py`, `moments.md` and the Tryka Birmingham slide. Already-posted events keep their old wording.


Cadence (CMO session, 9 Oct): the closer the race, the more often. Roughly 3 weeks apart far out, 2 weeks apart at 6-8 weeks, 10 days at 2-4 weeks, weekly in the final 2 weeks. A different angle each time, never the same text twice in a group, 10 days minimum between posts in one group. Dates marked (proposed) need Ante's go-ahead. Details of each post (group, who to post as, time, images, text) are in `posts/events/<city>/post-text.txt`.

| Event | Race | Done | Next post | Then | Group |
|---|---|---|---|---|---|
| HYROX Boston | 8-11 Oct | moment 3 on 2 Oct | none | | HYROX Boston 2026 |
| Tryka Series 2 Race 1, Dublin | 30 Oct-1 Nov | moment 1 on 30 Sep, moment 2 on 9 Oct (carousel, see post log) | Fri 23 Oct, moment 3 | | Tryka Ireland |
| HYROX Nashville | 9-13 Dec | moment 1 on 11 Oct (Natalia, time not recorded) | Wed 18 Nov, moment 2 | Wed 2 Dec | HYROX Nashville Athletes & Ticket Exchange 2026 (11.7K, groups/1542652697112148). The old HYROX NASHVILLE 2026 group (2661878954183327) was renamed "HYROX Community Tickets Resale (Buy&Sell) Moderated" and is not used. |
| HYROX Melbourne | 9-13 Dec | moment 1 submitted 12 Oct but NOT approved by the group admins, so not live (Natalia, 12 Oct) | Do not repost. Comment on real partner requests only (e.g. the women's doubles request in the group). If still not approved after a few days, treat the group as a no-go | Wed 18 Nov, Wed 2 Dec | HYROX Melbourne 2026 |
| HYROX Chicago | 11 Feb 2027 | moment 1 on 13 Oct | about Tue 3 Nov, moment 2 | about Tue 3 Nov, then every 2 weeks | see post-text.txt |
| HYROX Manchester | 20 Jan 2027 | moment 1 on 13 Oct (text only) | about Tue 3 Nov, moment 2 | about Tue 3 Nov, then every 2 weeks | see post-text.txt |
| HYROX Glasgow | 10 Mar 2027 | moment 1 on 14 Oct | about Wed 4 Nov, moment 2 | about Wed 4 Nov, then every 2 weeks | see post-text.txt |
| HYROX Phoenix | 25-28 Feb 2027 | | Wed 14 Oct, 8:30pm Irish, moment 1 | about Wed 4 Nov, then every 2 weeks | see post-text.txt |
| HYROX Tampa | 22-25 Oct | moments 1+2 on 2 Oct | Thu 15 Oct, 5:30pm Irish, moment 3 | none | Hybrid Fitness Tampa |
| HYROX London | 2-6 Dec | moment 1 on 4 Oct | Thu 15 Oct, women's angle (proposed) | Mon 26 Oct thread, Fri 6 Nov pace and goal, Wed 25 Nov last-minute (all proposed) | HYROX London ExCeL 2026 |
| HYROX Birmingham | 27 Oct-1 Nov | moment 1 on 29 Sep, moment 2 on 6 Oct, women's and mixed angle on 16 Oct | Mon 26 Oct last call (proposed) | Mon 26 Oct last call (proposed) | HYROX Birmingham 2026 |
| HYROX Dublin | 11-15 Nov | moment 1 on 30 Sep | Wed 21 Oct, moment 2 | Wed 4 Nov | HYROX Dublin 2026 |
| HYROX Denver | 12-15 Nov | moment 1 on 2 Oct | Thu 22 Oct, moment 2 | Thu 5 Nov | Hyrox Denver 2026 |
| HYROX Dallas | 18-22 Nov | moment 1 on 2 Oct | Wed 28 Oct, moment 2 | Wed 11 Nov | HYROX DALLAS 2026 |
| HYROX Johannesburg | 26-29 Nov | moment 1 on 2 Oct | Thu 5 Nov, moment 2 | Thu 19 Nov | Hyrox Johannesburg 2026 |
| HYROX Anaheim | 3-6 Dec | moment 1 on 4 Oct | Thu 12 Nov, moment 2 | Thu 26 Nov | HYROX Anaheim 2026 |

Thursday features (Instagram and Facebook Page): 15 Oct Nearby events, 22 Oct "It's a match", 29 Oct Chat and notifications. Wednesdays: 20 minutes commenting on real "need a partner" posts.
Superseded: the table that used to be here listed Nashville and Melbourne as posted on Sat 3 Oct. They were not posted; screens were reshot on 9 Oct (61d) but the CMO text-led image is the one to use.


### HYROX Ireland Sim & Gym Events (group 1516520836482042), added 10 Oct
Public, 1.0K members, created 4 May 2026, HyPair is a member. Admin: Maura Ahern. Rules: gyms and coaches post their sims for free in the format location / date / type / price / sign-up link; no training advice, no general questions, no spam; not official race ticket sales. Plan: alternate weekly, athlete statement post one week and gym post the next. Never a question or partner thread here. Never say HyPair lists sims (production has none). Gym posts: no pricing, no founding-gym offer, link hypair.app/for-gyms only. Gym week 1 posted 10 Oct (image `posts/gyms/2026-10-10-sim-week/sim-week.png`). Next: athlete week around Sat 17 Oct (two options drafted 14 Oct in `posts/gyms/2026-10-17-sim-group-athlete/post-text.txt`, waiting for Ante's pick), then gym week around 24 Oct. If removed, stop posting there and only comment. Check views and whether the admin reacts.

### Proposal for Ante, 10 Oct (Natalia): list every HYROX/Tryka event in the app, even outside the English-speaking region
Trigger: a "Who will be in Geneva?" post in a HYROX group on 10 Oct. HYROX Geneva is not in the app (checked in production). Idea: list all events, and people outside the main region can still see them and find partners. Open questions for Ante and the Engineering session: (1) how the Events tab filter treats non-English regions today, which I have not checked; (2) who adds events (rows in the production events table, owned by Engineering); (3) copy never promises matches in places with no athletes yet. Canada stays paused (AthleteField). Nothing changed in the app.

### Later (January onwards): act when the ticket button flips
On sale now: Manchester (20 Jan), Chicago (11 Feb), Glasgow (10 Mar), Tryka Birmingham Winter (13 Feb, NEC, tickets on tryka.fit). Corrected 9 Oct: Tryka Dublin Winter (29 Jan), Spring (1-3 Apr), Summer (26-30 Jun) and Autumn (29-31 Oct 2027) show "Details Coming Soon" on tryka.fit, so they are NOT on sale and moment 1 waits for the announcement. Tryka app check 9 Oct: all 7 events on tryka.fit are in the app with matching names, dates and venues; the app also keeps London Race 5 (5-6 Sep, past).
Not yet on sale: Phoenix, Las Vegas, Miami Beach, Cape Town, Brisbane, Houston, Atlanta, San Diego, Portland, Cardiff; New York date not announced.
Not in the app yet: HYROX Auckland (4-7 Feb, on sale).
Check the find-my-race page once a week (already part of the weekly race calendar refresh on the CMO page) and trigger moment 1 when a button flips.

### PROPOSED 7 Oct: extra posts for London and Birmingham (needs Ante's go-ahead, nothing is scheduled)
Why: sign-ups follow posts. Birmingham moment 2 (6 Oct 14:30) brought 2 real athletes within about 5 hours; London moment 1 (4 Oct) brought 1 that night. Ante's read: London and Birmingham are where people are actively looking. No new groups could be found, so the extra posts go into the groups we already use, with a different angle each time.
Safeguards unchanged: never the same text twice in a group, 10 to 14 days between posts in the same group, if a post is removed stop there and only comment. No running distances in the copy, no dating framing, never claim real athletes are signed up when they are not.
Real pools for one event and format (our four accounts excluded, 7 Oct): London Doubles 2 men + 2 women, London Mixed 2 men + 0 women, Birmingham Doubles 2 men + 1 woman. Every woman who enters unlocks women's Doubles and Mixed pairs.

| Event and group | Date (UK time, 12:30) | Days since last post in that group | Angle |
|---|---|---|---|
| Birmingham, HYROX Birmingham 2026 | Fri 16 Oct | 10 (after 6 Oct) | 1. Women's angle |
| Birmingham, same group | Mon 26 Oct | 10 | 4. Last call, race starts the next day (replaces the old Tue 20 Oct moment 3, which was only 4 days after the 16 Oct post) |
| London, HYROX London ExCel 2026 | Thu 15 Oct | 11 (after 4 Oct) | 1. Women's angle |
| London, same group | Mon 26 Oct | 11 | 2. Partner thread (pace, goal, where you are based; app link in the first comment) |
| London, same group | Fri 6 Nov | 11 | 3. Pace and goal ("find someone who wants the same day you do") |
| London, same group | Wed 25 Nov | 19 | 4. Last-minute, final week (replaces the old Wed 11 Nov and Wed 25 Nov moments 2 and 3) |

Birmingham stops at two extra posts because only 3 weeks remain and the gap rule leaves room for nothing else before the race. London is the long runway (8 weeks), so it gets four.
Not used: HYROX London 2026 (the March-event group) gets no more posts. Option if Ante wants more reach: Hyrox London Community (5.1K, quiet, never posted in) could carry the women's angle on its own schedule with different wording.
Assets: each post needs fresh screenshots taken the day before so the countdown is right. The women's angle can reuse the Find a Partner screen filtered to women; no Tryka, no "5K".
Draft copy, for Ante to edit:
- Women's angle (London): "Looking for a women's doubles partner for HYROX London (2-6 Dec)? Or a woman to race mixed doubles with? HyPair matches you by pace and goal with athletes entering the same race. Free to download: https://hypair.app"
- Partner thread (London): "HYROX London (2-6 Dec) partner thread. Drop your division, your usual running pace, your goal and where you are based. Easier to find your match here than to keep asking around." App link in the first comment.
- Pace and goal (London): "Not everyone races HYROX for a PB. Some want a fast one, some want a good day out. Find someone who wants the same day you do. HyPair matches you by pace and goal for the race you entered. Free to download: https://hypair.app"
- Last call (Birmingham): "HYROX Birmingham starts tomorrow. Still looking for a doubles partner, or did yours drop out? HyPair matches you by pace and goal with athletes entering the same event. Free to download: https://hypair.app"
- Angle 5, proposed 7 Oct by Natalia (not scheduled): "Struggling to find a partner? Go to a local sim." Local gym sim events are a great way to meet like-minded people and see if you are a match, which is what HyPair is for. CAUTION: production has zero sim events listed (checked 7 Oct, `events.is_sim = true` returns nothing), so the copy must NOT say HyPair lists sims near you. It can recommend the idea as advice and then point to HyPair for matching by pace and goal. Fits a Wednesday comment better than a standalone post.
Open for Ante: OK on the dates, OK on 4 posts for London and 2 for Birmingham, and whether to use Hyrox London Community.

## Posting timeline from 8 Oct (PROPOSED by the CMO session, dates need Ante's OK)
Times are what Ante sets on the clock. Irish time is 5 hours ahead of Eastern (US) until 1 Nov. Gap rule: at least 10 days between posts in the same group, except the last two weeks before a race where 7-9 is proposed below (needs OK).
| Day | Irish time | What | Where | Assets |
|---|---|---|---|---|
| Thu 8 Oct | 12:30 | Match score feature post | Instagram, then Facebook Page | features/2026-10-08-match-score/match-score-london.png |
| Fri 9 Oct | 12:30 | Tryka Series 2 Race 1 (Dublin), moment 2: "Partner dropped out?" (3 real athletes entered) | Tryka Ireland, POSTED ~13:00 | events/dublin-series2/ |
| Mon 12 Oct | 15:00 (10:00 ET) | Boston after-race "You did it" carousel | HYROX Boston 2026 | events/boston/post-race/ |
| Mon 12 Oct | 17:30 (12:30 ET) | Tampa extra post, partner thread (race is 10 days away; 10 days after the 2 Oct post) | Hybrid Fitness Tampa | new text, app link in first comment |
| Mon 12 Oct | open | Tryka Grand Finale (Lisbon, 10 Oct) after-race podium carousel | HyPair own channels (Instagram and Facebook Page), not a group: Tryka does not allow posting, only comments (Natalia, 12 Oct). Tag @tryka.fit. One-off exception to the Thursday-features-only rule | events/tryka-grand-finale-lisbon/post-race/ |
| Thu 15 Oct | 12:30 | Feature post: nearby events and location filter | Instagram, Facebook Page | to build |
| Thu 15 Oct | 12:30 | London women's and mixed angle (11 days after 4 Oct), APPROVED 14 Oct | HYROX London ExCel 2026 | events/london/post-text-womens.txt, png-export/london-womens-mixed.png |
| Fri 16 Oct | 12:30 | Birmingham women's and mixed angle (10 days after 6 Oct), text and image READY 16 Oct, waiting for Ante's OK | HYROX Birmingham 2026 | posts/events/birmingham/post-text-womens.txt, png-export/birmingham-womens-mixed.png |
| Wed 21 Oct | 17:30 (12:30 ET) | Tampa last call, "starts tomorrow" (replaces the old Thu 15 Oct moment 3) | Hybrid Fitness Tampa | new text |
| Sat 10 Oct | 18:30 (12:30 CT) | Nashville moment 1 | HYROX NASHVILLE 2026 | events/nashville/ |
| Sun 11 Oct | 07:00 (17:00 Melbourne) | Melbourne moment 1 | HYROX Melbourne 2026 | events/melbourne/ |
| Tue 13 Oct | 12:30 | Manchester moment 1 | HYROX MANCHESTER 2027 (258 members) | events/manchester/ |
| Tue 13 Oct | 18:30 (12:30 CT) | Chicago moment 1 (2 real athletes already entered) | HYROX Chicago 2027 (2.6K) | events/chicago/ |
| Wed 14 Oct | 12:30 | Glasgow moment 1 (1 real athlete entered) | Hyrox Scotland Community (12K), check its rules | events/glasgow/ |
| Wed 14 Oct | 20:30 (12:30 Arizona) | Phoenix moment 1 | HYROX Phoenix 2027 (281) or Hyrox Arizona (1.5K) | events/phoenix/ |
Groups for Manchester, Chicago, Phoenix and Glasgow were found on 9 Oct by searching Facebook; none joined yet. Join and read the rules first.

### Tryka official Facebook page (added 9 Oct)
The official TRYKA Facebook page posts the series announcements (e.g. "BIRMINGHAM, GET READY", pre-sale 17 Sep, posted 15 Sep). Ante wants HyPair to comment on them as the HyPair Page. This is a comment, not a group post, so the gap rule does not apply, but promotional comments can be deleted: keep it short, never repeat it, and comment on the newest on-sale or race-week post rather than an old one (the Birmingham pre-sale post is three weeks old and gets almost no views).
Draft (Birmingham): "Racing Tryka Birmingham (13-14 Feb) and need a partner? HyPair matches you by pace and goal with athletes entering the same event. Free to download: https://hypair.app"
Draft (Series 2, Ireland): "Racing Tryka Series 2 Race 1 in Dublin (30 Oct-1 Nov) and need a partner? HyPair matches you by pace and goal with athletes entering the same event. Free to download: https://hypair.app"
Ireland and UK only: never mention Tryka in US or Canada copy. Log every comment in the post log with the date and which post it was on.

### Cadence rule: post more often the closer the race (Ante, 9 Oct)
| Time to race | Gap between posts in one group |
|---|---|
| More than 12 weeks | about 3 weeks (moment 1, then a light refresh) |
| 6 to 12 weeks | about 2 weeks |
| 2 to 6 weeks | about 10 days |
| Final 2 weeks | weekly, plus a last call the day before |
Always a different angle and text each time; if a post is removed, stop in that group and only comment.

Thu 15 Oct feature post (Instagram and Page): ticket filter ("Ticket or no ticket. Filter for both."), image and captions in `posts/features/2026-10-15-ticket-filter/`, drafted 15 Oct, waiting for Ante to post. Race styles ("Which one are you?", Agent Drafts Ref 39) waits until the race styles are in the app profile (Ante, 14 Oct); the Nearby events image is not built.
After-race carousel for any event: `python3 brand/social/posts/_templates/post-race/make_post_race.py race <folder> "HYROX <City>" "<dates>"` (use `podium` for Tryka). Post on the Monday after the event.

## Weekly rhythm (small team, about 2 hours a week)
| Day | What |
|---|---|
| Daily, 5 min | Answer comments and DMs on own channels. The partner-reply check task runs every two days by itself. |
| Monday | Group posts for the week (moment 1 or moment 3). Best time is lunchtime in the event's time zone. |
| Wednesday | 20 minutes commenting on real "need a partner" posts in groups (extra to the planned posts). |
| Thursday | Feature post on Instagram and the Facebook Page. Features only. |
| Friday, 30 min | Refresh the race calendar, review Agent Drafts, log last week's posts in the table below. |

### Thursday feature posts (proposed, needs your OK and a fresh app screenshot each)
| Date | Feature |
|---|---|
| 8 Oct | Match score: see compatibility before you commit |
| 15 Oct | Nearby events and the location filter |
| 22 Oct | "It's a match" lock-in |
| 29 Oct | Chat and notifications (say "on iPhone" unless Android push is confirmed) |

## Post log (fill in after every post)
| Date and time | Event | Moment | Group or channel | Views | Reactions | Comments | App sign-ups for that event in the next 7 days |
|---|---|---|---|---|---|---|---|
| 29 Sep 16:42 | HYROX Birmingham | 1 | HYROX Birmingham 2026 | 1,648 | 100 | 2 | 1 |
| 30 Sep 12:15 | Tryka Series 2 Race 1 | 1 | Tryka Ireland | 101 | 7 | 0 | 2 |
| 9 Oct ~13:00 | Tryka Series 2 Race 1 | 2 | Tryka Ireland (3-slide carousel: Find a Partner, It's a match, chat; 9 days after moment 1; exact time approximate, posted by Ante after 12:50; library time 13:06) | 83 | 3 (eng.) | 0 | |
| 10 Oct (time not noted) | HYROX UK and Ireland (Birmingham, Dublin, London, Manchester, Glasgow) | comment | Instagram comment as hypair.app on the @hyroxuk post "HYROX 26/27 SEASON - FINAL TICKETS REMAINING" (draft B: names the five races, "link in bio"). One comment only, no replies to individual commenters. If @hyroxuk deletes it, leave it. | | | | |
| 30 Sep 15:04 | HYROX Dublin | 1 | HYROX Dublin 2026 | 11 | 0 | 0 | 0 |
| 2 Oct ~18:30 | HYROX Dallas | 1 | HYROX DALLAS 2026 (approved and live, but only 2 views by 3 Oct); Hyrox Dallas (Buying & Selling) Verified Tickets 2026 (still pending admin approval); HYROX DALLAS 2026 TICKETS EXCHANGE (no longer in the library) | 7 + 3 (two groups) | 1 (eng.) | 0 | |
| 2 Oct ~19:30 | HYROX Johannesburg | 1 | Hyrox Johannesburg 2026 (still pending admin approval on 11 Oct; written off 12 Oct, no more checks) | 2 | 0 | 0 | |
| 2 Oct ~19:15 | HYROX Denver | 1 | Hyrox Denver 2026 (approved 22:19 on 2 Oct) | 354 | 17 (eng.) | 0 | |
| 2 Oct ~19:00 | HYROX Tampa | 1+2 | Hybrid Fitness Tampa (posted; not in the Page library). HYROX Tampa 2026 copy at 18:53: 278 views, 18 eng., 0 comments | 280 (HYROX Tampa 2026 copy, 12 Oct) | 18 (eng.) | 0 | |
| 11 Oct ~07:00 | HYROX Melbourne | 1 | HYROX Melbourne 2026 (same wording as Nashville; still pending admin approval on 12 Oct; gone from the Page library on 13 Oct, probably declined) | 0 (pending) | 0 | 0 | |
| 6 Oct 14:30 | HYROX Birmingham | 2 | HYROX Birmingham 2026 (3-slide carousel: Find a Partner, It's a match, chat) | 820 | 53 (eng.) | 1 | 2 real athletes signed up within about 5 hours of the post, both entered Birmingham (figure from Ante via the CMO session, 7 Oct) |
| 15 Oct ~12:30 | HYROX London | extra (women's and mixed angle) | HYROX London ExCel 2026 (posted by Ante; image london-womens-mixed.png, text in events/london/post-text-womens.txt; exact time approximate). Shan B. (UK) signed up and entered Birmingham Doubles at 13:25 the same day, not London | | | | |
| 16 Oct ~12:30 | HYROX Birmingham | extra (women's and mixed angle) | HYROX Birmingham 2026 (posted by Natalia as HyPair; one image birmingham-womens-mixed.png; 10 days after the 6 Oct post) | | | | |
| 14 Oct ~14:00 | HYROX Glasgow | 1 | Hyrox Scotland Community (posted by Natalia, 2 images with real app screens, new "Ready to race" wording; group is quiet, about 13 posts a month) | | | | |
| 14 Oct | Question post "Where would you race next?" (market research, not an event post) | n/a | HYROX (Official Community, 327.5K members; posted by Natalia as herself; approved by the admins 14 Oct; map image, see posts/features/2026-10-14-where-next/; exact wording and which map version not recorded) | | | | |
| 13 Oct | HYROX Manchester | 1 | HYROX MANCHESTER 2027 (posted by Natalia about 14:00 Irish, text only, new "Ready to race" wording; screens (slide 2) to be added as a comment) | | | | |
| 13 Oct ~18:30 | HYROX Chicago | 1 | HYROX Chicago 2027 (posted by Natalia, 2 images with real app screens, new "Ready to race" wording) | | | | |
| 11 Oct | HYROX Nashville | 1 | HYROX Nashville Athletes & Ticket Exchange 2026 (joined 11 Oct; posted by Natalia, time not recorded; wording as post-text.txt; library time 07:45 Irish) | 23 | 4 (eng.) | 0 | |
| 10 Oct | Tryka Grand Finale Lisbon (comment, not a post) | extra comment | TRYKA official Page post "AND WE'RE OFF" (posted by Natalia as HyPair, wording not recorded; supportive comment, no link, no image) | | | | |
| 10 Oct | Gym week 1 (B2B angle) | n/a | HYROX Ireland Sim & Gym Events (public, 1.0K members, admin Maura Ahern; posted by Natalia, time not recorded; no admin OK asked first; library time 12:25; still live on 11 Oct, no comments, no reactions) | 51 | 6 (eng.) | 0 | |
| 4 Oct ~20:35 | HYROX Anaheim | 1 | HYROX Anaheim 2026 (posted, emoji version at 20:35; a second, plain copy at 20:37 also live) | 27 + 7 | 2 (eng.) | 0 | |
| 4 Oct ~08:40 | HYROX London | 1 | HYROX London ExCel 2026 and HYROX London 2026 (the March-event group), both posted 09:16, emoji version; the link had square brackets and needs editing | ExCeL 56, March group 177 | 6 + 6 (eng.) | 0 | 1 London athlete signed up that night (4 Oct), per Ante via the CMO session |
| 2 Oct ~18:45 | HYROX Boston | 3 | HYROX Boston 2026 (posted as HyPair). Private HYROX Boston: skipped for now (Ante, 2 Oct). Library time 18:40; HWPO hub copy 18:42 | 1,207 (HWPO 120) | 75 (eng.) | 3 | |
| 7 Oct 19:57 | HYROX Boston | race-week | HYROX Boston 2026 ("Boston race weekend is almost here"), plus HWPO HYROX BOSTON TICKETS & RACE HUB 2026 at 19:59 | 363 (HWPO 164) | 6 (eng.) | 0 | |
| 8 Oct 16:06 | Feature post (match score) | n/a | HyPair Facebook Page feed ("Not every partner is the right partner") | 3 | 0 | 0 | |

Sign-ups are real external users only (not staff, not test or demo accounts, not the store reviewers), totals as of 2 Oct, not a 7-day count. An earlier version of this table counted staff and test accounts and overstated them (4, 3, 1).

After three or four events, compare the moments and keep the one that brings in the most sign-ups.

### First views check, 2 Oct evening (from the Facebook Page content library, which only lists posts made as HyPair)
| Posted (Irish) | Event | Group | Views | Engagement |
|---|---|---|---|---|
| 18:29 | Dallas | HYROX DALLAS 2026 TICKETS EXCHANGE | 5 | 0 |
| 18:30 | Dallas | HYROX DALLAS 2026 | 2 | 0 |
| 18:31 | Dallas | Hyrox Dallas (Buying & Selling) Verified Tickets 2026 | 2 | 0 |
| 18:40 | Boston | HYROX Boston 2026 | 85 (37 viewers) | 0 |
| 18:41 | Boston | HYROX BOSTON TICKETS EXCHANGE 2026 | 16 | 0 |
| 18:42 | Boston | HWPO HYROX BOSTON TICKETS & RACE HUB 2026 | 7 | 0 |
| 18:53 | Tampa | HYROX Tampa 2026 | 83 | 5 |
| 18:54 | Tampa | HYROX Tampa 2026 (second copy, one minute later) | 1 | 0 |
| about 19:30 | Johannesburg | Hyrox Johannesburg 2026 | 0 (pending approval) | 0 |
Denver and Hybrid Fitness Tampa do not appear in the Page library (posted from a personal profile, or not posted as HyPair).

### Second views check, 3 Oct morning (Page library)
| Posted (Irish, 2 Oct) | Event | Group | Views | Viewers | Engagement | Note |
|---|---|---|---|---|---|---|
| 18:40 | Boston | HYROX Boston 2026 | 393 | 233 | 25 | Best so far |
| 18:53 | Tampa | HYROX Tampa 2026 | 207 | 101 | 8 | Duplicate copy at 18:54 has 1 view |
| 22:19 (approved) | Denver | Hyrox Denver 2026 | 136 | 52 | 4 | Live |
| 18:42 | Boston | HWPO HYROX BOSTON TICKETS & RACE HUB 2026 | 12 | 6 | 0 | |
| 18:30 | Dallas | HYROX DALLAS 2026 | 2 | 2 | 0 | Confirmed by Ante: approved and live, just low reach |
| 18:31 | Dallas | Hyrox Dallas (Buying & Selling) Verified Tickets 2026 | 2 | 1 | 0 | Probably still awaiting approval |
| about 19:30 | Johannesburg | Hyrox Johannesburg 2026 | 1 | 1 | 0 | Still pending |
| 18:41 and 18:29 | Boston and Dallas | the two TICKETS EXCHANGE groups | | | | No longer listed in the library (were there last night). Check in the groups before concluding they were removed. |

### Views check, 11 Oct (run on the morning of 12 Oct, Page library, last 28 days)
| Posted (Irish) | Group | Text starts | Views | Viewers | Engagement | Comments |
|---|---|---|---|---|---|---|
| 11 Oct (pending) | HYROX Melbourne 2026 | "HYROX Melbourne is on!" | 0 | 0 | 0 | 0 |
| 11 Oct 07:45 | HYROX Nashville Athletes & Ticket Exchange 2026 | "HYROX Nashville is on!" | 49 | 15 | 8 | 0 |
| 10 Oct 12:25 | HYROX Ireland Sim & Gym Events | "Running a HYROX-style sim or open day?" | 72 | 43 | 9 | 0 |
| 9 Oct 13:06 | Tryka Ireland | "Partner dropped out? ... Tryka Series 2 Race 1" | 115 | 55 | 5 | 0 |
| 8 Oct 16:06 | HyPair Page feed | "Not every partner is the right partner." | 3 | 3 | 0 | 0 |
| 7 Oct 19:59 | HWPO HYROX BOSTON TICKETS & RACE HUB 2026 | "Boston race weekend is almost here." | 165 | 60 | 0 | 0 |
| 7 Oct 19:57 | HYROX Boston 2026 | "Boston race weekend is almost here." | 368 | 235 | 6 | 0 |
| 6 Oct 14:30 | HYROX Birmingham 2026 | "Partner dropped out? ... HYROX Birmingham" | 822 | 503 | 53 | 1 |
| 4 Oct 20:37 | HYROX Anaheim 2026 (plain copy) | "HYROX Anaheim is on!" | 7 | 3 | 2 | 0 |
| 4 Oct 20:35 | HYROX Anaheim 2026 (emoji copy) | "HYROX Anaheim is on!" | 27 | 13 | 0 | 0 |
| 4 Oct 09:16 | HYROX LONDON EXCEL 2026 | "HYROX London is on!" | 59 | 26 | 6 | 0 |
| 4 Oct 09:16 | HYROX London 2026 | "HYROX London is on!" | 181 | 87 | 6 | 0 |
| 2 Oct 22:19 | Hyrox Denver 2026 | "HYROX Denver is on" | 354 | 153 | 17 | 0 |
| 2 Oct (pending) | Hyrox Johannesburg 2026 | "HYROX Johannesburg is on" | 2 | 1 | 0 | 0 |
| 2 Oct 18:53 | HYROX Tampa 2026 | "HYROX Tampa is on" | 280 | 129 | 18 | 0 |

Older 2 Oct rows (Boston moment 3, Dallas) did not render in the library this time; the figures in the Post log stand. The gym post is still live in HYROX Ireland Sim & Gym Events (found via group search, image intact). It has no reactions and no comments, so Maura Ahern has not commented. The library's 9 engagements are probably clicks, not visible reactions. Nothing was posted or commented.

Read: the "partner dropped out" carousel in a big, race-specific group is still the clear winner (Birmingham: 822 views, 53 engagements, 1 comment, and the only post tied to sign-ups this week). Big US race groups come next (Boston race-week 368, Denver 354, Tampa 280). The "is on!" launch angle in smaller or newer groups is flat (Anaheim 34 across two copies, London ExCeL 59, Nashville 49 on day one, though 8 engagements from 15 viewers is a good rate). The gym post reached 43 people in a 1.0K-member group, with clicks but no visible response, so it's alive but quiet; give it a week before reading anything into it. No post looks removed. Melbourne and Johannesburg are still pending admin approval (Johannesburg for ten days now, so treat it as dead). The Page feed post (3 views) confirms the Page itself has no audience yet; groups are where the reach is.

New real sign-ups since 1 Oct: Theresa (Boston, 2 Oct 20:12 Irish, onboarded, entered HYROX Boston Doubles, about 90 minutes after the Boston post in HYROX Boston 2026; the source is not proven) and one person who has not finished onboarding (3 Oct 02:17). Real users: 16, onboarded 9.

### Views check, 11 Oct (re-run on 13 Oct, Page library, last 28 days: 15 Sep-13 Oct)
| Posted (Irish) | Group | Text starts | Views | Viewers | Engagement | Comments | Change since 12 Oct |
|---|---|---|---|---|---|---|---|
| 11 Oct | HYROX Melbourne 2026 | "HYROX Melbourne is on!" | | | | | Not in the library any more |
| 11 Oct 07:45 | HYROX Nashville Athletes & Ticket Exchange 2026 | "HYROX Nashville is on!" | 94 | 31 | 8 | 0 | +45 views |
| 10 Oct 12:25 | HYROX Ireland Sim & Gym Events | "Running a HYROX-style sim or open day?" | 101 | 61 | 9 | 0 | +29 views |
| 9 Oct 13:06 | Tryka Ireland | "Partner dropped out? ... Tryka Series 2 Race 1" | 141 | 68 | 7 | 0 | +26 views |
| 8 Oct 16:06 | HyPair Page feed | "Not every partner is the right partner." | 3 | 3 | 0 | 0 | none |
| 7 Oct 19:59 | HWPO HYROX BOSTON TICKETS & RACE HUB 2026 | "Boston race weekend is almost here." | 165 | 60 | 0 | 0 | none |
| 7 Oct 19:57 | HYROX Boston 2026 | "Boston race weekend is almost here." | 370 | 236 | 6 | 0 | +2 |
| 6 Oct 14:30 | HYROX Birmingham 2026 | "Partner dropped out? ... HYROX Birmingham" | 828 | 506 | 53 | 1 | +6 |
| 4 Oct 20:37 | HYROX Anaheim 2026 (plain copy) | "HYROX Anaheim is on!" | 7 | 3 | 2 | 0 | none |
| 4 Oct 20:35 | HYROX Anaheim 2026 (emoji copy) | "HYROX Anaheim is on!" | 27 | 13 | 0 | 0 | none |
| 4 Oct 09:16 | HYROX LONDON EXCEL 2026 | "HYROX London is on!" | 61 | 27 | 6 | 0 | +2 |
| 4 Oct 09:16 | HYROX London 2026 | "HYROX London is on!" | 186 | 89 | 6 | 0 | +5 |
| 2 Oct 22:19 | Hyrox Denver 2026 | "HYROX Denver is on" | 356 | 155 | 17 | 0 | +2 |
| 2 Oct (pending) | Hyrox Johannesburg 2026 | "HYROX Johannesburg is on" | 3 | 1 | 0 | 0 | still pending |
| 2 Oct 18:53 | HYROX Tampa 2026 | "HYROX Tampa is on" | 280 | 129 | 18 | 0 | none |
| 2 Oct 18:42 | HWPO HYROX BOSTON TICKETS & RACE HUB 2026 | "Racing HYROX Boston (8–11 Oct)" | 120 | 60 | 0 | 0 | |
| 2 Oct 18:40 | HYROX Boston 2026 | "Racing HYROX Boston (8–11 Oct)" | 1,207 | 690 | 75 | 3 | |
| 2 Oct 18:31 | Hyrox Dallas (Buying & Selling) Verified Tickets 2026 | "HYROX Dallas is on" | 3 | 1 | 0 | 0 | |
| 2 Oct 18:30 | HYROX DALLAS 2026 | "HYROX Dallas is on" | 7 | 2 | 1 | 0 | |
| 30 Sep 12:15 | Tryka Ireland | "Series 2 Race 1 — RDS Dublin" | 283 | 121 | 12 | 0 | Post log still says 101 (an early reading) |

The gym post is still live in HYROX Ireland Sim & Gym Events (found via group search on 13 Oct, image intact). No reactions and no comments, so Maura Ahern has not commented. Nothing was posted, commented or changed.

Read: the 10 Oct gym post is alive and still growing (101 views from 61 people in a 1.0K-member group, 9 clicks), but there's no visible response, and that's what matters for B2B. Nashville picked up the most since yesterday (+45) and has the best engagement rate of the "is on!" posts (8 from 31 viewers). Tryka moment 2 (141) is now about half of Tryka moment 1 (283), so the second post in the same small group gets less. "Partner dropped out" in a big race group is still the best angle (Birmingham 828, Boston moment 3 1,207). Everything older than a week has stopped growing. Melbourne has disappeared from the library, so it was most likely declined by the group admin. Johannesburg is still pending after eleven days, so it's dead. Nothing else looks removed.

## Real users (how we count)
"Real external user" = anyone in production who is not one of the four accounts that are ours (Natalia, Ante, the Apple reviewer, the Google reviewer) and not a QA, demo or test account. Standing rule from Ante: every sign-up count in this file and on the Notion planner page uses this definition.
"Onboarded" = profile complete (`profiles.profile_complete = true`). "Entered a race" = at least one row in `user_events`.
Run `real-users.sql` (in this folder) against production for the live list. The named snapshot is on the Notion page "Social planner: when to post what"; names are not kept in the repo.

Snapshot 7 Oct 2026 (from Ante via the CMO session): 23 real athletes, 15 finished onboarding. Not yet re-pulled here; run `real-users.sql` for the named list.
Snapshot 2 Oct 2026: 14 real users. 8 onboarded, 6 not. 6 of the 8 onboarded have entered a race; the other 2 have not entered any yet.
Re-engagement email (24h after signup): 9 people nudged so far. 3 finished onboarding within about an hour of it (first race entries 2 min, 4 min and 62 min after the email); 6 did not (Bernard came back on 28 Sep but has not finished). Timing is a strong hint, not proof. Last-sign-in is unreliable (silent session refresh), so race-entry times are used instead.

### Nudge test log (email only vs email + push)
The re-engagement nudge goes out 24-48h after signup to anyone with an unfinished profile, at :15 past the hour.
**Email only (19 Sep to 1 Oct, 9 people):** 3 finished onboarding within about an hour (2 min, 4 min, 62 min after the email), 6 did not.
**Email + push:** the push companion was added on 3 Oct (code 12:34, deployed 12:37 Irish time). It goes to anyone with a push token: "Your HyPair profile is waiting. Setting up takes about a minute, tap to pick up where you left off." Push needs notifications allowed, and Android push delivery is not confirmed.
First test case: the user who signed up on 3 Oct at 02:17 (not onboarded); nudge due about 02:15 on 4 Oct. Record below.
| Nudged (Irish) | Had a push token | Finished onboarding? | How long after |
|---|---|---|---|
| 4 Oct ~02:15 (signed up 3 Oct 02:17) | to check | to check | |
Keep the two groups separate when comparing. One case proves nothing; wait for 5 to 10.
