# Falariand campaign

- `GM_LEDGER.md` — private GM world state: rules of play, NPCs, clocks, Evander's state, log, secrets, open continuity issues.
- `maps/world_map.webp` — the full source world map (2000x1000, equirectangular, 0.18° per px). `maps/` also holds regional crops of the Falariand coast (`falariand_strip_annotated.webp` has realm labels; see open issues in the ledger).
- `tools/` — area estimators for the source world map (equirectangular, 0.18° per px). Pixel ranges are hard-coded to `maps/world_map.webp` (convert to PNG first); they do not apply to the crops.
  - `python3 tools/zones.py <map.png> 9556` — area of west/crown/east land zones.
  - `python3 tools/areas.py <map.png> 9556` — connected land regions between borders.
  - `python3 tools/island.py <map.png>` — area of Gravesmere and its distance from Wadun.
