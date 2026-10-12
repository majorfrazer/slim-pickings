# SLIM PICKINGS — Build Brief

Oct 13, 2026 · @Fraser

Build SLIM PICKINGS a single-page PWA (one index.html plus manifest.json, on Firebase Hosting) from the SLIM PICKINGS — Official (Unofficial) Press Kit tab (`docs/press-kit.md` in this repo), on the normal build: Claude Code builds in VS Code, Codex checks and cleans up, Fraser and Claude (chat) steer.

## Background and Canon

SLIM PICKINGS is a satirical DJ duo with a fixed lore; the Press Kit tab is the only source of copy, and every joke below is canon that generated copy must not contradict. The table is the lore bible: if a page, post or alt text would break a row, it is wrong.

| Topic | Canon (as the kit stands today) |
| --- | --- |
| Name | SLIM PICKINGS, two words, caps. Name origin is currently unexplained in the kit; do not invent one. |
| Members | The Captain (AJ), MAJOR, and Slim the horse (tour manager, A&R, mascot, credited on every release). |
| Home | Machu Picchu, Peru, 7,970 ft (2,430 m). |
| The claim | "Highest DJs on Earth." Disputed by a collective in La Paz (11,942 ft). The claim refers strictly to altitude. |
| Fathers | Played together in the 14th Andean Ceremonial Marching Band, tuba and snare, thirty-one years. |
| Time signature | 4/4 only, ever. Tempo 118 to 128 BPM, parade pace. |
| The arrival | 2011, by boat, with 45,000 records in the hold. How a boat reached 7,970 ft is never explained, by anyone, anywhere. |
| The Captain's past | Street tricks for coins in Cusco; bottle-cap routine banned by the council in 1999; bought wax instead of food; no paid meal since 2002. Plays rare delights only, never a request. |
| MAJOR's past | Left with a sick horse as a child, fixed it, village vet by fourteen, licence pending since 2004. Takes vet call-outs mid-set. Signature: the brass drop. |
| Rank dispute | A Captain outranks "at sea"; a Major outranks "on land." Unresolved; they share one mixer. |
| Gear | 2 x 7-inch turntables, direct drive; 1 x mixer; 1 x tuba (not plugged in); 1 x boat; 1 x horse. No CDJs. |
| Sets | One hour, then oxygen. No roof, ever. Payment in the hat. Crowds acclimatise 48 hours. |
| Label | Llama Rojo Recordings. Seven releases, 2012 to 2026, newest a 7" + digital. |
| Availability | Not Tuesdays. Tuesdays are clinic days. Bookings by DM or carrier llama (6 to 8 weeks). |
| Tone | Deadpan. Short sentences. Invented outlets, labels and venues only; never a real brand, venue or person. |

## What We're Building

A one-page, mobile-first PWA that gives a booker everything in one scroll: who they are, what they sound like, where to listen, how to book. Same shape as PopDarts (one index.html, manifest.json, service worker, Firebase Hosting), so it installs to a phone and costs nothing to run.

### Goals

- Satire intact: copy comes from the Press Kit tab verbatim; agents fix typos and change nothing else.
- Fast and cheap: static, no build step, Firebase Spark plan, Lighthouse mobile 90+ on all four categories.
- Installable: manifest, service worker, icons, offline shell.
- Bookable: a form that lands somewhere real, with a fallback that works with JavaScript off.
- Printable: the press kit as a PDF a booker can forward.

### Non-goals for v1

- No CMS, no accounts, no backend beyond the enquiry sink.
- No ticketing or shop; Bandcamp handles sales.
- No live streaming embeds until the profiles exist; placeholder tiles carry the handle until then.
- No analytics.

### Deliverables

1. `index.html`, `styles.css`, `app.js`: the site, sections per the site map below.
2. `manifest.json`, `sw.js`, icons (192, 512, maskable), favicon set, `og.png` (1200 x 630).
3. `presskit.html` print page and `assets/SLIM-PICKINGS-press-kit.pdf` rendered from it.
4. Booking form writing to Firebase Realtime Database `enquiries/`, with a `mailto:` fallback.
5. `docs/press-kit.md` (Markdown export of the Press Kit tab, canonical copy) and `docs/build-brief.md` (this file).
6. `CLAUDE.md`, `AGENTS.md`, `README.md`.
7. `firebase.json`, `.firebaserc`, `database.rules.json`.

## Site Map and Content Model

Eleven sections in one scroll, each mapped to the Press Kit heading it is ported from, so Codex can diff copy section by section. Nav is a sticky row of anchors; the altitude badge (7,970 ft) sits in it permanently.

| Section (anchor) | Press Kit source | Component and behaviour |
| --- | --- | --- |
| Hero (`#top`) | Short Bios, one-liner | Name, one-liner, altitude badge, two buttons: "Listen (1 hour, then oxygen)" and "Book (not Tuesdays)" |
| The Legend (`#legend`) | The Legend | Prose, max-width 65ch, paragraphs as in the kit |
| The Members (`#members`) | The Members | Three cards: The Captain, MAJOR, Slim; illustration slot, role line, bio, signature line |
| The Sound (`#sound`) | The Sound and the Live Show | Two columns on desktop; BPM and gear as chips; live-show list |
| Listen (`#listen`) | Socials and Music Platforms | Click-to-load facades for Mixcloud and SoundCloud; placeholder tiles showing the handle until profiles exist |
| Discography (`#releases`) | Discography | Table on desktop, stacked cards under 640px; newest first |
| Press (`#press`) | Press | Stacked quotes, attribution in small caps; no carousel |
| Rider and Tech (`#rider`) | Rider, Tech Spec and Booking | Accordion (tech spec, rider, booking terms); "Download the press kit (PDF)" button |
| Book (`#book`) | Booking | Form: name, email, venue, city, date, hat size; date picker refuses Tuesdays with the kit's line; submits to `enquiries/` |
| How-To's (`#howto`) | How-To's | Accordion, four numbered lists verbatim |
| Footer | Socials and Music Platforms | Handle row with icons; every unclaimed link carries `data-placeholder="true"` and a small "to be claimed" tag until Phase 5 |

Not on the site: the kit's "Making It Real" section (that is for us, not bookers).

## Stack and Constraints

Vanilla HTML, CSS and JavaScript on Firebase Hosting, no framework and no bundler, because that is the shape that has worked and anyone can read it in a year. Nothing below changes without PM sign-off.

- Repo: `majorfrazer/slim-pickings` (new, public). Firebase project `slim-pickings`, Spark plan, Realtime Database in `australia-southeast1` if offered, else the default.
- Files: `index.html`, `styles.css`, `app.js` (one ES module), `manifest.json`, `sw.js`, `presskit.html`, `assets/`, `docs/`. No `node_modules` committed; dev tooling runs through `npx` only (prettier, html-validate, lighthouse).
- Service worker: network-first for `index.html`, cache-first for same-origin assets, versioned cache name bumped per release.
- Fonts: one self-hosted display face under an open licence (Bebas Neue or Anton) plus the system stack for body. No third-party font requests, so the offline shell works.
- Budget: under 300 KB transferred on first load, excluding embeds. Embeds are click-to-load facades: a static tile with the artwork and a play button, the real player loads on tap.
- Database rules: `enquiries` is push-only from the client (`$id` writable only when `!data.exists()`), never readable from the client, with `.validate` requiring `name`, `email`, `venue`, `date` and a `ts`. Reads happen in the Firebase console only.
- Form fallback: with JavaScript off the form posts nowhere; the submit button becomes a `mailto:` link to the bookings address with the fields prefilled in the body.
- Accessibility: WCAG AA contrast, every accordion and the form operable by keyboard, visible focus, `prefers-reduced-motion` honoured, alt text on every illustration that is itself in canon.
- Browsers: current iOS Safari, Android Chrome, evergreen desktop. iOS install works (`apple-touch-icon`, `apple-mobile-web-app-*` metas).
- Secrets: none in the repo. The Firebase web config is public by design; `database.rules.json` does the protecting.
- Copy: `docs/press-kit.md` is canonical. The page carries the copy inline in semantic HTML (no runtime fetch); Codex diffs the two every phase.
- PDF: `presskit.html` carries a print stylesheet; Codex renders it with headless Chromium (`npx playwright` or `chrome --headless --print-to-pdf`) and commits `assets/SLIM-PICKINGS-press-kit.pdf`, under 2 MB, text selectable.

## Design Direction

A marching band's bass-drum head meets a 7-inch record sleeve at altitude: bold, flat, deadpan, dark by default because it is night on a mountain. Nothing on the page winks at the reader; the copy does that.

### Palette (CSS custom properties)

| Token | Hex | Use |
| --- | --- | --- |
| `--night` | #0B1A2B | Page background (dark, default) |
| `--snow` | #F5F1E8 | Body text on night; page background in light mode |
| `--altiplano` | #C8372D | Primary: buttons, hero accents, large text only (contrast on night is borderline for small text) |
| `--brass` | #D4A017 | Links, badges, the altitude chip, the brass drop |
| `--wool` | #E9DCC3 | Cards and panels in light mode; muted text on night |
| `--ink` | #141414 | Text in light mode |

### Type

- Display: one condensed open-licence face (Bebas Neue or Anton), self-hosted, for the name, section headings and the altitude badge.
- Body: system stack, 17px base, 1.6 line height, 65ch measure.
- Numbers and gear lines in tabular figures.

### Illustration

- No photographs of real people until supplied. Everything is flat SVG drawn in-repo: a 7-inch record, a tuba, a horse silhouette, and one boat sitting at the summit in the hero, unexplained.
- Member cards get a silhouette each: a captain's hat, a drum major's mace, a horse. Same stroke weight, same two colours.
- Icons for the socials row are inline SVG, monochrome brass.

### Motion

- One thing moves: the hero record spins slowly, pauses on tap. Everything else is static.
- Accordions animate height over 150ms. `prefers-reduced-motion` stops all of it.

### Layout

- Single column on phones, 1100px max width on desktop, two columns only for The Members and The Sound.
- Sticky nav with anchors and the altitude badge; it collapses to a menu under 640px.
- Light mode follows `prefers-color-scheme`; a manual toggle in the footer, remembered in `localStorage`.
- Micro-copy is deadpan and in canon: "Listen (1 hour, then oxygen)", "Book (not Tuesdays)", form error for a Tuesday: "Tuesdays are clinic days."

## The Normal Build

Three seats, one loop per phase, and "done" means verified box state, not a sentence saying so.

### Seats

| Seat | Who | Owns | Does not |
| --- | --- | --- | --- |
| PM | Fraser and Claude (chat) | Scope, copy, design calls, phase sign-off, merges | Write code |
| Builder | Claude Code, in VS Code | Each phase end to end on its own branch, the phase report | Change copy, stack or scope on its own |
| Checker | Codex | Validation, diffs, link and a11y checks, small fixes, the gate verdict | Redesign, reword, re-architect |

### The loop, per phase

1. PM drops the phase into Claude Code: the kickoff prompt plus any decisions since.
2. Claude Code builds on `phase/N-name`, commits in small steps, deploys a preview channel, posts the phase report.
3. Codex checks out the branch, runs the AGENTS.md checklist, fixes what is in its lane with `fix(check): ...` commits, flags the rest, posts the gate verdict.
4. PM reads both reports, clicks through the preview on a phone and a desktop, merges or sends it around again.
5. Around again.

### Rules both agents work to

- Verified box state over prose: every claim of done carries the command and its output (validator result, Lighthouse scores, preview URL, screenshot paths under `docs/screens/`). "Should work" is not a status.
- Copy is sacred: `docs/press-kit.md` is verbatim on the page. Typos are fixed and listed; anything else is a PM call.
- One branch and one PR per phase; diffs stay small enough to read in one sitting.
- Codex fixes lint, validation errors, broken links, CSS regressions, a11y defects and dead code directly; it flags design, copy, stack and scope back with the smallest decision needed.
- Never explain the boat. In code comments either.
- Phase report format, both seats: What changed / How verified (commands and results) / What's open / Gate: PASS or FAIL with reason.

## Phases and Gates

Six phases in a straight run, each closed by a gate Codex can verify from the box. No phase starts before the one before it passes.

1. **Phase 0, Scaffold** (`phase/0-scaffold`). Repo, Firebase project, `index.html` with all eleven sections and nav stubbed, `styles.css` with the palette tokens, empty `app.js` module, `manifest.json`, `sw.js`, placeholder icons, `firebase.json`, `.firebaserc`, `database.rules.json` (push-only enquiries), `README.md`, `CLAUDE.md`, `AGENTS.md`, `docs/press-kit.md`, `docs/build-brief.md`.
   Gate: preview channel URL loads; `html-validate` clean; Lighthouse reports the PWA installable; rules deployed and a client read of `enquiries` is denied.
2. **Phase 1, Content port** (`phase/1-content`). Every section carries its kit copy verbatim: Legend, Members, Sound, Discography table, Press quotes, Rider accordion, How-To lists, socials row with placeholder tags.
   Gate: Codex's copy diff against `docs/press-kit.md` shows zero unapproved differences; every heading from the site map present; all anchors resolve.
3. **Phase 2, Design pass** (`phase/2-design`). Palette, type, SVG illustrations, spinning record, altitude badge, dark and light modes, responsive layout, accordions.
   Gate: screenshots at 390px and 1280px in both modes committed under `docs/screens/phase-2/`; contrast AA on every text pair; reduced-motion verified; Lighthouse mobile 90+ on performance, accessibility, best practices and SEO.
4. **Phase 3, Listen and Book** (`phase/3-listen-book`). Click-to-load embed facades, booking form to `enquiries/`, Tuesday validation, `mailto:` fallback with JS off.
   Gate: a test enquiry appears in the Firebase console with all required fields; a client read is denied; the form works with JavaScript disabled; first-load transfer still under 300 KB.
5. **Phase 4, Press kit PDF and share assets** (`phase/4-presskit`). `presskit.html` print page, rendered PDF committed and linked, `og.png`, final favicon and icon set.
   Gate: PDF opens, under 2 MB, text selectable, every kit section present; a link-preview check shows title, description and `og.png`; icons pass the manifest audit.
6. **Phase 5, Launch** (`phase/5-launch`). Handles claimed and real links swapped in, placeholder tags removed, custom domain if bought, final Lighthouse run, tag `v1.0.0`, deploy to production.
   Gate: every link in the socials row returns 200; production URL loads on iOS Safari and Android Chrome; PM sign-off recorded in the PR.

## Acceptance Checklist (v1.0.0)

All of these are true on the production URL before the tag goes on; each one is checked by a command or a screenshot, not a sentence.

- [ ] Lighthouse mobile: performance, accessibility, best practices and SEO all 90 or above, report saved under `docs/lh/`.
- [ ] First-load transfer under 300 KB with no embeds loaded; verified in DevTools network tab, screenshot saved.
- [ ] Installs to the home screen on iOS Safari and Android Chrome; opens offline to the cached shell.
- [ ] `html-validate` and `prettier --check` clean on every HTML, CSS and JS file.
- [ ] Copy diff against `docs/press-kit.md`: zero differences beyond approved typo fixes.
- [ ] Every section from the site map present, every nav anchor lands on it, altitude badge visible at every width.
- [ ] Dark and light modes both pass AA contrast on every text and background pair.
- [ ] Keyboard only: every accordion opens, the form submits, focus is visible throughout.
- [ ] `prefers-reduced-motion`: the record does not spin, accordions do not animate.
- [ ] Booking form: a test enquiry lands in `enquiries/` with `name`, `email`, `venue`, `date`, `ts`; a Tuesday is refused with the clinic line; a client read is denied.
- [ ] JavaScript off: the form falls back to a prefilled `mailto:` link.
- [ ] Embeds load only on tap; nothing third-party loads before interaction.
- [ ] `assets/SLIM-PICKINGS-press-kit.pdf` opens, under 2 MB, text selectable, carries every kit section.
- [ ] Link preview shows title, description and `og.png` on a preview checker.
- [ ] Every link in the socials row returns 200; no `data-placeholder` tags remain.
- [ ] No secrets in the repo; `database.rules.json` deployed matches the repo copy.

## Repo Files and Kickoff Prompts

Four paste-ready blocks: two files that live in the repo root and are the contract both agents read first, and two prompts that start each seat on Phase 0. Drop `docs/press-kit.md` (Markdown export of the Press Kit tab) and `docs/build-brief.md` (this file) in before the first prompt.

### CLAUDE.md

```markdown
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
```

### AGENTS.md

```markdown
# AGENTS.md — Codex, the checker seat

You check and clean up. You do not redesign, reword copy, or change the stack.
Read CLAUDE.md and docs/build-brief.md first; confirm which phase you are checking and its gate.

## On every branch you are pointed at
1. Run and record: npx html-validate index.html presskit.html; npx prettier --check .;
   npx lighthouse <preview-url> (mobile, default settings).
2. Diff all visible copy in index.html against docs/press-kit.md, section by section.
   A difference that is not a typo fix: list it, do not change it.
3. Links: every href resolves, or carries data-placeholder="true" and the visible "to be claimed" tag.
4. Accessibility: tab through every accordion and the form; check contrast from the Lighthouse a11y audit;
   toggle prefers-reduced-motion and confirm nothing moves.
5. Database: confirm database.rules.json matches the deployed rules; attempt a client read of enquiries
   and record that it is denied.
6. Fix directly, on the same branch, as fix(check): ... commits: lint, validation errors, broken links,
   CSS regressions, a11y defects, dead code.
7. Flag back, do not fix: design choices, copy, stack, scope, anything needing a PM call.

## Report (comment on the PR)
Verified: one line per command, command -> result
Fixed: list with commit hashes
Open: list, each with the smallest decision needed
Gate: PASS or FAIL, with the reason
```

### Kickoff prompt for Claude Code (Phase 0)

```markdown
You are the builder seat on the SLIM PICKINGS site. Read CLAUDE.md and docs/build-brief.md in full before touching anything, then run Phase 0 (Scaffold) exactly as the brief describes and nothing beyond it.

Setup: repo majorfrazer/slim-pickings (create if missing), Firebase project slim-pickings on the Spark plan, branch phase/0-scaffold.

Deliver: index.html with the eleven sections and sticky nav stubbed from the site map (headings only, copy comes in Phase 1); styles.css with the palette tokens from the design direction; app.js as an empty ES module; manifest.json; sw.js (network-first index.html, cache-first same-origin assets, versioned cache); placeholder icons 192/512/maskable; firebase.json; .firebaserc; database.rules.json with enquiries push-only and unreadable; README.md.

Gate: deploy a preview channel and give me the URL; html-validate clean; Lighthouse reports the PWA installable; rules deployed and a client read of enquiries denied, with the command output shown.

End with the phase report: What changed / How verified (commands + results) / What's open / Gate. Do not start Phase 1.
```

### Kickoff prompt for Codex (Phase 0 check)

```markdown
You are the checker seat on the SLIM PICKINGS site. Read AGENTS.md, then check out branch phase/0-scaffold and run every step in AGENTS.md against the Phase 0 gate in docs/build-brief.md.

Fix what is in your lane as fix(check): commits on the same branch. Flag everything else with the smallest decision needed. Post the report in the AGENTS.md format with a PASS or FAIL on the Phase 0 gate. Do not change copy, design, stack or scope.
```

## Open Decisions

Six calls before Phase 0 starts; each has a default so nothing blocks if you just say "defaults".

| Decision | Default | Why it matters |
| --- | --- | --- |
| Repo and Firebase project names | `majorfrazer/slim-pickings`, project `slim-pickings` | Baked into `.firebaserc` and every preview URL |
| Domain | None for v1; ship on the `*.web.app` URL | A bought domain changes Phase 5 and the OG URLs |
| Enquiry sink | Realtime Database `enquiries/` with `mailto:` fallback | Formspree or mailto-only would drop the rules work from Phases 0 and 3 |
| Bookings email address | Set up on an owned domain before Phase 3 | The `mailto:` fallback and the kit's socials row both need it |
| Illustrations or photos | Illustrations only (SVG, in-repo) | Real photos change the member cards, the OG image and the PDF |
| Press Kit tab as final copy | Treat the tab as it stands today | Two spots read like accidental deletions: the Slim (the horse) heading is blank, and the social bio line lost "S. Highest DJs on Earth"; confirm or restore before `docs/press-kit.md` is exported, because Codex diffs against it |
