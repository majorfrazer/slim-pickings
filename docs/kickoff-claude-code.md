You are the builder seat on the SLIM PICKINGS site. Read CLAUDE.md and docs/build-brief.md in full before touching anything, then run Phase 0 (Scaffold) exactly as the brief describes and nothing beyond it.

Setup: repo majorfrazer/slim-pickings (create if missing), Firebase project slim-pickings on the Spark plan, branch phase/0-scaffold.

Deliver: index.html with the eleven sections and sticky nav stubbed from the site map (headings only, copy comes in Phase 1); styles.css with the palette tokens from the design direction; app.js as an empty ES module; manifest.json; sw.js (network-first index.html, cache-first same-origin assets, versioned cache); placeholder icons 192/512/maskable; firebase.json; .firebaserc; database.rules.json with enquiries push-only and unreadable; README.md.

Gate: deploy a preview channel and give me the URL; html-validate clean; Lighthouse reports the PWA installable; rules deployed and a client read of enquiries denied, with the command output shown.

End with the phase report: What changed / How verified (commands + results) / What's open / Gate. Do not start Phase 1.
