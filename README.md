# Xiaomin Zhong — personal academic homepage

Single-page personal site for Dr Xiaomin (Billy) Zhong, health data epidemiologist
at the University of Oxford. Plain HTML and CSS, no build step, served by GitHub Pages.

Its main job is to be the authoritative anchor page for the name "Xiaomin Zhong" so
search engines can recognise one person and merge the scattered profiles (Google
Scholar, LinkedIn, ResearchGate, the Oxford department page) into a single entity.
That is what the `schema.org` `Person` block with `sameAs` links in `index.html` does.

## Files
- `index.html` — the whole site (markup, styles, a little JS), with SEO + Open Graph + JSON-LD
- `assets/og.png` — social share card (1200x630)
- `assets/make_og.py` — regenerates the share card
- `.nojekyll` — tells GitHub Pages to serve files as-is

## Deploy (GitHub Pages, root site)
Lives at the user-root repo `BillyZhongUOM.github.io`, served at
`https://billyzhonguom.github.io/`.

```bash
git add -A && git commit -m "..." && git push
```

Pages rebuilds in 1 to 3 minutes on push to `main`.

## Editing notes
- **Photo:** the headshot is `assets/portrait.jpg` (square, ~720px, sourced from Billy's
  `Billyacademic.jpg`). To change it, replace that file with another square image, then
  re-run `python3 assets/make_og.py` to refresh the share card.
- **Update the canonical URL:** if the site moves to a custom domain, change `SITE_URL`
  in the three marked places in `index.html` (canonical, og:url, JSON-LD url).
- **Add ORCID:** once an ORCID iD exists, add its URL to the `sameAs` array in the
  JSON-LD and add a profile link card.
- **Citation metrics** in the hero card are a manual snapshot from Google Scholar; update
  the numbers and the "Source ... June 2026" note when they drift.
- Regenerate the share card after copy or branding changes: `python3 assets/make_og.py`.
