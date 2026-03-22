# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

HyPair is a "coming soon" landing page for a hybrid race partner matching app (HYROX, Spartan, Tryka, Athex). The entire project is a single self-contained file: `index.html`.

## Structure

Everything — HTML, CSS, and JavaScript — lives in `index.html`. There is no build step, no package manager, and no framework. Open the file directly in a browser to preview.

## Architecture

The page has two states toggled via JavaScript:
- **Waitlist state** (`#waitlist-section`): Hero with email capture form
- **Success state** (`#success-section`): Shown after form submission

### Supabase integration (not yet active)

The `joinWaitlist()` function contains a commented-out `fetch` block for posting emails to a Supabase `waitlist` table. To activate:
1. Create a Supabase project and a `waitlist` table (`id`, `email`, `created_at`)
2. Enable Row Level Security with an anon insert policy
3. Replace `SUPABASE_URL` and `SUPABASE_ANON_KEY` constants at the top of the `<script>` block
4. Uncomment the `fetch` block and remove the `setTimeout` simulation

### Design tokens

CSS custom properties are defined in `:root` — `--green`, `--gold`, `--white-*` opacity variants, etc. All colors and spacing should reference these variables.

### Fonts

Google Fonts: `Barlow Condensed` (headings, buttons) and `Barlow` (body). Loaded via `<link>` in `<head>`.
