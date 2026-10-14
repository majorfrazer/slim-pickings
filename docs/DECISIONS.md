# DECISIONS — the owner's words on this project, one dated line each

**Rules.** Fraser's words verbatim where the wording is load-bearing. Dated with AEST time and UTC in brackets,
taken from the message timestamp where one exists; where only the session clock is available, the row says so.
Nothing is removed; a superseded line is struck, not deleted. Decisions that cross projects (spend, working mode,
security) are banked in the Alf-E KNOWLEDGE `OWNER_DECISIONS.md` and point here (PM seat ruling, 7 Oct 2026).
This is a side project under Alf-E owner rows 24 and 25: one seat, no fan-out, yields to Alf-E and S11.

| # | Date | Decision | Where it came from |
|---|---|---|---|
| 1 | 13 Oct 2026 | **The Press Kit tab is canon and `docs/press-kit.md` is its export.** Fraser's edits of 13 Oct stand: 45,000 records (was 4,000); 2 x 7-inch turntables; one shared mixer (the rank dispute); sets run 1 hour then oxygen (was 45 min); bottle-cap ban 1999; no paid meal since 2002; the name-origin paragraph deleted, so the name is deliberately unexplained; newest release a 7" + digital. | The chat summary of 13 Oct 2026 (Claude chat, PM seat), pasted to Claude Code by Fraser with the starter files |
| 2 | 13 Oct 2026 | **"Restore"**: the blank Slim (the horse) heading and the social bio's "S. Highest DJs on Earth" were accidental deletions; both were pulled back from doc history before the export. | Same chat summary ("you said restore") |
| 3 | 13 Oct 2026 | **The build brief of 13 Oct is the contract**: one-page PWA on Firebase Hosting, Spark plan, vanilla stack, the normal build (PM = Fraser and Claude chat; builder = Claude Code; checker = Codex), six phases with gates. | `docs/build-brief.md`, delivered with the starter files |
| 4 | 14 Oct 2026, early morning AEST, session clock, not a message timestamp | *"continue!"* — after the Phase 0 report. Read by the builder as the PM's word to start Phase 1 before the Codex check of Phase 0 has run; Phase 1 is built on `phase/1-content`, stacked on `phase/0-scaffold`, so either phase can still be sent round. | Chat with Claude Code |

## Assumed by the builder seat on 13 Oct 2026, not decided

The brief's six Open Decisions each carry a default and the chat summary says *"Defaults" settles them*; Fraser has not
yet said the word. Phase 0 ran on the defaults below because the kickoff prompt bakes the first and third in. A row
above is added only in Fraser's own words.

| Ref | Open decision | Taken as | Where it bit in Phase 0 |
|---|---|---|---|
| A1 | Repo and Firebase project names | `majorfrazer/slim-pickings` (public), Firebase project `slim-pickings` | Both created with exactly those names; `.firebaserc` and every preview URL carry them |
| A2 | Domain | None for v1; `*.web.app` | Nothing yet (Phase 5) |
| A3 | Enquiry sink | Realtime Database `enquiries/` with `mailto:` fallback | `database.rules.json` written and deployed; default instance `slim-pickings-default-rtdb` in `us-central1` (the brief's "else the default": `australia-southeast1` is not offered for RTDB) |
| A4 | Bookings email address | Set up on an owned domain before Phase 3 | Nothing yet |
| A5 | Illustrations or photos | Illustrations only (SVG, in-repo) | Placeholder icons are a flat record, no photos |
| A6 | Press Kit tab as final copy | The tab as exported, restores included (row 2) | `docs/press-kit.md` committed verbatim on `main` |
