// Asks Chrome itself (DevTools protocol) whether the preview is installable, and whether the service worker controls the page.
const { chromium } = require('playwright-core');
const url = process.argv[2];
(async () => {
  const ctx = await chromium.launchPersistentContext(require('path').join(__dirname, 'profile'), { channel: 'chrome', headless: true });
  const browser = ctx.browser() || { version: () => 'persistent-context', close: () => ctx.close() };
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'load' });
  await page.waitForFunction(async () => (await navigator.serviceWorker.getRegistrations()).some(r => r.active), null, { timeout: 20000 }).catch(() => {});
  await page.waitForTimeout(1500);
  const sw = await page.evaluate(async () => {
    const regs = await navigator.serviceWorker.getRegistrations();
    const keys = await caches.keys();
    const cache = keys.length ? await caches.open(keys[0]) : null;
    const cached = cache ? (await cache.keys()).map(r => new URL(r.url).pathname) : [];
    return { registrations: regs.map(r => ({ scope: r.scope, state: r.active && r.active.state })), controller: !!navigator.serviceWorker.controller, caches: keys, cached };
  });
  const cdp = await ctx.newCDPSession(page);
  const manifest = await cdp.send('Page.getAppManifest');
  const inst = await cdp.send('Page.getInstallabilityErrors');
  // Reload once so the page is controlled, then go offline and reload: does the shell still render?
  await page.reload({ waitUntil: 'load' });
  const controlled = await page.evaluate(() => !!navigator.serviceWorker.controller);
  await ctx.setOffline(true);
  let offline = { ok: false, title: null };
  try { await page.reload({ waitUntil: 'load' }); offline = { ok: true, title: await page.title() }; } catch (e) { offline = { ok: false, error: e.message.split('\n')[0] }; }
  await ctx.setOffline(false);
  console.log(JSON.stringify({ chrome: browser.version(), manifestUrl: manifest.url, manifestErrors: manifest.errors, installabilityErrors: inst.installabilityErrors, serviceWorker: sw, controlledAfterReload: controlled, offlineReload: offline }, null, 2));
  await ctx.close();
})().catch(e => { console.error('FAILED:', e.message); process.exit(1); });
