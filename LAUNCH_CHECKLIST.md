# HyPair — Pre-Launch Checklist

Items that require credentials, external services, or manual steps outside the codebase.

---

## Priority 1 — Must-have before App Store submission

### Apple Team ID
- [ ] Go to [developer.apple.com](https://developer.apple.com) → Account → Membership
- [ ] Copy **Team ID** (10-char string, e.g. `AB12CD34EF`)
- [ ] Paste into `eas.json` → `"appleTeamId": "YOUR_TEAM_ID"`

### notification-icon.png
- [ ] Create a **96×96 PNG** — white icon on a **transparent background**
- [ ] Save as `assets/notification-icon.png`
- [ ] Already referenced in `app.json` under `expo.notification.icon` — just drop the file in

### Privacy Policy + Terms of Service
- [ ] Write or generate at [termly.io](https://termly.io) or [getterms.io](https://getterms.io)
- [ ] Publish at `hypair.app/privacy` and `hypair.app/terms`
- [ ] Update the hardcoded URLs in `app/(tabs)/settings.tsx` (search for `privacy` and `terms`)

### Email SMTP (Resend — recommended)
- [ ] Sign up at [resend.com](https://resend.com) → verify `hypair.app` domain → copy API key
- [ ] Supabase Dashboard → Authentication → Email Templates → SMTP Settings
- [ ] Enable Custom SMTP:
  - Host: `smtp.resend.com` · Port: `465`
  - Username: `resend` · Password: your Resend API key
  - Sender: `noreply@hypair.app`
- [ ] Send a test email to confirm delivery

### Push Notifications Edge Function
- [ ] Supabase Dashboard → Edge Functions → New function: `send-push`
- [ ] Function reads `profile_tokens` for target user and calls Expo Push API:
  ```
  POST https://exp.host/--/api/v2/push/send
  { to: token, title: "...", body: "...", data: { chatId } }
  ```
- [ ] Wire as Database Webhook: Dashboard → Database → Webhooks → on `INSERT` in `messages` → call `send-push`
- [ ] No API key needed — Expo push is free and keyless for standard notifications

### delete_own_account RPC
- [ ] Supabase Dashboard → Edge Functions → create `delete-account` function
- [ ] Function calls `supabase.auth.admin.deleteUser(userId)` using service role key
- [ ] Add `SUPABASE_SERVICE_ROLE_KEY` as an Edge Function secret in the Dashboard
- [ ] In `app/(tabs)/settings.tsx`, update `void supabase.rpc('delete_own_account')` to call the Edge Function instead
- [ ] *(Alternative: test if `GRANT EXECUTE ON FUNCTION delete_own_account() TO authenticated;` works on your Supabase plan)*

---

## Priority 2 — Nice-to-have before launch

### Sentry DSN
- [ ] Go to [sentry.io](https://sentry.io) → New Project → React Native
- [ ] Copy DSN from Project Settings → Client Keys
- [ ] Set in `.env` / EAS secrets: `EXPO_PUBLIC_SENTRY_DSN=https://xxxx@sentry.io/yyyy`
- [ ] App already calls `initSentry()` in `app/_layout.tsx` — activates automatically once env var is set

### Analytics (PostHog — recommended)
- [ ] Sign up at [posthog.com](https://posthog.com) → new project → copy API key + host
- [ ] `npx expo install posthog-react-native`
- [ ] Wrap app in `PostHogProvider` in `app/_layout.tsx`
- [ ] Add `EXPO_PUBLIC_POSTHOG_KEY` to env
- [ ] Key events to capture:
  - `sign_up`, `onboarding_complete`, `event_registered`
  - `partner_request_sent`, `match_confirmed`, `pairing_cancelled`

### pg_cron (Supabase)
- [ ] Supabase Dashboard → Database → Extensions → search `pg_cron` → Enable
- [ ] Use case: schedule auto-close of expired lock-in requests (48h window)

### Supabase Storage CDN
- [ ] Supabase Dashboard → Storage → `avatars` bucket → Edit → confirm **Public bucket** is ON
- [ ] Enable **Smart CDN** if on Pro plan (serves images from edge nodes)
- [ ] Free tier serves directly from Supabase Storage — acceptable for beta

---

## Priority 3 — Post-launch

### Content Moderation (AWS Rekognition)
- [ ] AWS Console → IAM → create user with `AmazonRekognitionFullAccess` → copy Access Key + Secret
- [ ] Supabase Dashboard → Edge Functions → create `moderate-avatar`
- [ ] Function calls Rekognition `DetectModerationLabels` on upload, returns pass/fail
- [ ] Wire as Storage webhook: Dashboard → Storage → Hooks → on `INSERT` in `avatars` → call function
- [ ] If flagged: `UPDATE profiles SET status = 'flagged'` to hide from partner search

### Rate Limiting (Upstash Redis)
- [ ] Sign up at [upstash.com](https://upstash.com) → Create Database → copy REST URL + REST Token
- [ ] Add to EAS secrets: `UPSTASH_REDIS_REST_URL` + `UPSTASH_REDIS_REST_TOKEN`
- [ ] Add `@upstash/ratelimit` to `send-push` Edge Function
- [ ] Suggested limits: 10 messages/user/minute · 5 connect requests/user/hour
