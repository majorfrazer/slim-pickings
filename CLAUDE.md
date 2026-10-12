# CLAUDE.md — SLIM PICKINGS site

## What this is
Single-page PWA for the satirical DJ duo SLIM PICKINGS. The press kit made browsable.
Canonical copy: docs/press-kit.md. Everything else: docs/build-brief.md. Read both before touching anything.

## Stack (no changes without PM sign-off)
- Vanilla HTML/CSS/JS: index.html, styles.css, app.js (one ES module), manifest.json, sw.js, presskit.html.
- No framework, no bundler, no runtime npm deps, no node_modules committed. Dev tooling via npx only.
- Firebase Hosting + Realtime Database (enquiries only). Rules in database.rules.json.

## Working rules
1. Copy from docs/press-kit.md is verbatim on the page. Fix typos and list them; change nothing else.
2. One branch per phase (phase/0-scaffold, phase/1-content, ...), one PR per phase, small commits.
3. Every "done" is verified: paste the command and its output in the phase report and the PR.
4. Budget: under 300 KB first load excluding embeds. Embeds are click-to-load facades.
5. Accessibility: WCAG AA contrast, keyboard-operable accordions and form, prefers-reduced-motion honoured.
6. No secrets in the repo. Firebase web config is public; database.rules.json does the protecting.
7. Never explain the boat.

## Commands (firebase-tools installed globally once: npm i -g firebase-tools)
- Serve locally:    firebase serve  (or: python3 -m http.server 8080)
- Validate:         npx html-validate index.html presskit.html
- Format check:     npx prettier --check .
- Lighthouse:       npx lighthouse <url> --output html --output-path docs/lh/phase-N.html
- Preview deploy:   firebase hosting:channel:deploy phase-N
- Rules deploy:     firebase deploy --only database
- Production:       firebase deploy --only hosting   (PM sign-off first)

## Phase report format
What changed / How verified (commands + results) / What's open / Gate: PASS or FAIL with reason
