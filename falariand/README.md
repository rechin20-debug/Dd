# Falariand campaign

- `GM_LEDGER.md` — private GM world state: rules of play, NPCs, clocks, Evander's state, log, secrets, open continuity issues.
- `maps/` — regional crops of the Falariand coast (`falariand_strip_annotated.webp` has realm labels; see open issues in the ledger).
- `tools/` — area estimators for the source world map (equirectangular, 0.18° per px). Pixel ranges are hard-coded to the full source map, which is not in this repo; they do not apply to the crops in `maps/`.
  - `python3 tools/zones.py <map.png> 9556` — area of west/crown/east land zones.
  - `python3 tools/areas.py <map.png> 9556` — connected land regions between borders.
