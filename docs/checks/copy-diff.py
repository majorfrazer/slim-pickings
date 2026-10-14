#!/usr/bin/env python3
"""Copy diff for the SLIM PICKINGS page.

Compares every visible text block in index.html with every text block in docs/press-kit.md
(paragraphs, list items, table cells, headings), after whitespace normalisation, and prints:
  - kit blocks that are not on the page (omissions)
  - page blocks that are not in the kit (additions)
  - anchors: every href="#id" and aria-labelledby that has no matching id
  - headings: the site-map section headings that are missing
Standard library only. Usage: python3 docs/checks/copy-diff.py [index.html] [docs/press-kit.md]
Exit code 0 always; the lists are the result, the PM decides what is approved.
"""
import re, sys
from html.parser import HTMLParser

INDEX = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
KIT = sys.argv[2] if len(sys.argv) > 2 else 'docs/press-kit.md'
BLOCK = {'p', 'li', 'h1', 'h2', 'h3', 'h4', 'td', 'th', 'figcaption', 'summary', 'title', 'caption'}
SITE_MAP_HEADINGS = ['The Legend', 'The Members', 'The Sound', 'Listen', 'Discography', 'Press', 'Rider and Tech', 'Book', "How-To's"]

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks, self.ids, self.hrefs, self.labelledby, self.headings = [], set(), [], [], []
        self._buf, self._depth, self._skip = [], 0, 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'a' and a.get('href', '').startswith('#'): self.hrefs.append(a['href'][1:])
        if 'aria-labelledby' in a: self.labelledby.append(a['aria-labelledby'])
        if tag in ('script', 'style'): self._skip += 1
        if tag in BLOCK:
            if self._depth: self._flush()
            self._depth += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self._skip -= 1
        if tag in BLOCK and self._depth:
            self._depth -= 1
            if tag in ('h1', 'h2', 'h3'): self.headings.append(norm(''.join(self._buf)))
            self._flush()
    def handle_data(self, data):
        if self._skip: return
        if self._depth: self._buf.append(data)
    def _flush(self):
        t = norm(''.join(self._buf)); self._buf = []
        if t: self.blocks.append(t)

def kit_blocks(md):
    out = []
    for line in md.splitlines():
        line = line.rstrip()
        if not line or set(line) <= set('|-: '): continue
        if line.startswith('|'):
            for cell in line.strip('|').split('|'): out.append(norm(cell))
            continue
        line = re.sub(r'^#+\s*', '', line)
        line = re.sub(r'^(- \[ \] |- |\d+\. )', '', line)
        line = line.replace('**', '').replace('`', '')
        out.append(norm(line))
    return [b for b in out if b]

page = Page(); page.feed(open(INDEX, encoding='utf-8').read())
kit = kit_blocks(open(KIT, encoding='utf-8').read())
page_set, kit_set = set(page.blocks), set(kit)

def contained(block, haystack_blocks):
    """A kit block counts as present if it equals a page block or sits inside one (e.g. a quote inside a figure)."""
    return block in haystack_blocks or any(block in h for h in haystack_blocks)

omissions = [b for b in kit if not contained(b, page_set)]
# attribution lines: the kit writes '"quote" — Outlet' on one line; the page splits quote and outlet
def covered_by_split(b):
    if ' — ' not in b: return False
    q, src = b.rsplit(' — ', 1)
    return q in page_set and ('— ' + src) in page_set
omissions = [b for b in omissions if not covered_by_split(b)]
additions = [b for b in page.blocks if not any(b == k or b in k or (k in b and len(k) > 20) for k in kit_set)]

print(f'page blocks: {len(page.blocks)} · kit blocks: {len(kit)}')
print(f'\nKIT BLOCKS NOT ON THE PAGE ({len(omissions)}):')
for b in omissions: print('  -', b)
print(f'\nPAGE BLOCKS NOT IN THE KIT ({len(additions)}):')
for b in additions: print('  +', b)
bad = [h for h in page.hrefs if h not in page.ids] + [l for l in page.labelledby if l not in page.ids]
print(f'\nANCHORS: {len(page.hrefs)} in-page hrefs, {len(page.labelledby)} aria-labelledby; unresolved: {bad or "none"}')
missing = [h for h in SITE_MAP_HEADINGS if h not in page.headings]
print(f'SITE-MAP HEADINGS: {len(SITE_MAP_HEADINGS) - len(missing)}/{len(SITE_MAP_HEADINGS)} present; missing: {missing or "none"}')
