# SLIM PICKINGS

Single-page PWA for the satirical DJ duo SLIM PICKINGS: the press kit made browsable. Vanilla HTML,
CSS and JavaScript on Firebase Hosting; one Realtime Database path (`enquiries/`) for the booking form.

- Canonical copy: [docs/press-kit.md](docs/press-kit.md). Verbatim on the page; typos fixed and listed, nothing else changed.
- Everything else: [docs/build-brief.md](docs/build-brief.md). Site map, stack, design direction, phases and gates.
- Seats: [CLAUDE.md](CLAUDE.md) (builder), [AGENTS.md](AGENTS.md) (checker). Owner words: [docs/DECISIONS.md](docs/DECISIONS.md).

## Phase status

| Phase | Branch | State |
| --- | --- | --- |
| 0 Scaffold | `phase/0-scaffold` | built, awaiting the Codex check and PM merge |
| 1 Content port | `phase/1-content` | not started |
| 2 Design pass | `phase/2-design` | not started |
| 3 Listen and Book | `phase/3-listen-book` | not started |
| 4 Press kit PDF and share assets | `phase/4-presskit` | not started |
| 5 Launch | `phase/5-launch` | not started |

## Run it

No build step. Dev tooling runs through `npx`; nothing is installed into the repo.

```sh
python3 -m http.server 8080            # then open http://localhost:8080/
npx html-validate index.html           # validation (add presskit.html from Phase 4)
npx prettier --check .                 # formatting (markdown and docs/ are ignored on purpose)
npx firebase-tools hosting:channel:deploy phase-N   # preview channel
npx firebase-tools deploy --only database           # rules
```

Production deploys (`firebase deploy --only hosting`) need PM sign-off first.

## Layout

```
index.html          the page: eleven sections, sticky nav, altitude badge
styles.css          palette tokens, dark by default, light mode by preference or toggle
app.js              one ES module (Phase 0: service worker registration only)
sw.js               network-first index.html, cache-first same-origin assets, versioned cache
manifest.json       installable PWA
assets/icons/       placeholder icons until Phase 4
firebase.json       hosting (public = repo root, docs and markdown ignored) and database rules
database.rules.json enquiries: push-only from the client, never readable
docs/               press kit (canonical), build brief, kickoff prompts, decisions, Lighthouse reports
```

The boat is not explained here either.
