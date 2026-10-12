// SLIM PICKINGS — app.js (one ES module).
// Phase 0: nothing here but the service worker registration. App logic arrives in Phase 3.

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('sw.js').catch(() => {
      // Offline shell unavailable; the page works without it.
    });
  });
}

export {};
