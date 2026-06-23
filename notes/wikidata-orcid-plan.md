# Wikidata item + ORCID plan for Xiaomin (Billy) Zhong

Goal: build a search-engine identity for the name "Xiaomin Zhong" so Google can
recognise one entity and, over time, surface a knowledge panel. The live personal
site is the anchor; ORCID and a Wikidata item are the next two signals.

Status as of 2026-06-23:
- Personal site LIVE at https://billyzhonguom.github.io/ (repo BillyZhongUOM.github.io).
- Billy HAS his own ORCID: **0000-0002-3448-6702** (confirmed his: University of Oxford,
  Department of Population Health from Nov 2023, plus his real papers). Now added to the
  site `sameAs` and profile card.
- Billy has NO Wikidata item yet; no Wikidata item uses his ORCID either (checked).

## Wikidata search result (de-duplication done 2026-06-23)
The name already maps to other people, which is the core disambiguation problem:
- **Q102291863** "Xiaomin Zhong" - "Ph.D. University of Connecticut 2004". Different person.
- **Q91266654** "Xiaomin Zhong" - bot stub from ORCID 0000-0002-3416-114X, which belongs to
  a Xiaomin Zhong at **Sun Yat-sen University, Guangzhou, China**. Different person.
- Conclusion: Billy needs a NEW item, with a description that clearly distinguishes him.

## Honest caveats (read before creating)
- Wikidata is far more permissive than Wikipedia, but a thin, self-authored biography can
  still be nominated for deletion. The defence is identifier-rich, sourced statements, not
  promotional prose. With a Google Scholar author ID, an employer, an official website and
  (soon) an ORCID, a researcher item is normally accepted and kept.
- A Google knowledge panel is NOT guaranteed and NOT instant. Wikidata enables it; Google
  decides. In the near term the live site plus consolidated, cross-linked profiles do most
  of the disambiguation work.

## Step 1 - ORCID (DONE: 0000-0002-3448-6702)
Billy already has an ORCID, and it is already added to the site. Optional tidy-up Billy
can do on orcid.org when convenient (the record currently lists employment + works but no
education):
- Add education: PhD Health Informatics and MSc Health Data Science, University of
  Manchester; BSc, Peking University.
- Add also-known-as "Billy Zhong"; keep visibility public.

## Step 2 - Wikidata item (Billy logs in; Claude drives via Chrome MCP)
Needs a logged-in Wikimedia account. Create the item, then add statements. Use the
autocomplete to pick the correct target entity for each value (do not paste guessed Q-ids).

- **Label (en):** Xiaomin Zhong
- **Also known as:** Billy Zhong; Xiaomin (Billy) Zhong
- **Description (en):** health data epidemiologist at the University of Oxford
  (distinguishes from the Sun Yat-sen and Connecticut namesakes)

Statements (each sourced where noted):
- instance of (P31) -> human
- sex or gender (P21) -> male  [Billy to confirm]
- occupation (P106) -> epidemiologist; researcher
- employer (P108) -> University of Oxford   [ref: NDPH profile URL]
- educated at (P69) -> University of Manchester; Peking University
- academic degree (P512) -> Doctor of Philosophy  [qualifier on P69 Manchester]
- field of work (P101) -> epidemiology; health data science
- Google Scholar author ID (P1960) -> rSH7qsgAAAAJ   [strong, verifiable anchor]
- official website (P856) -> https://billyzhonguom.github.io/
- ORCID iD (P496) -> 0000-0002-3448-6702

Reference for sourced statements: reference URL
https://www.ndph.ox.ac.uk/team/xiaomin-zhong , retrieved 2026-06-23.

Verifiable anchors already in hand:
- Google Scholar: https://scholar.google.com/citations?user=rSH7qsgAAAAJ (168 citations, h-index 8)
- Oxford profile: https://www.ndph.ox.ac.uk/team/xiaomin-zhong
- ResearchGate: https://www.researchgate.net/profile/Xiaomin-Zhong-4
- LinkedIn: https://www.linkedin.com/in/xiaomin-zhong-2a5aa2231/

## Step 3 - close the loop
- Add ORCID to site `sameAs` + a profile link card; redeploy.
- Confirm every profile (Scholar, ORCID, LinkedIn, ResearchGate, NDPH) uses the same name
  form and links back to the site, so the identity is consistent across the web.
