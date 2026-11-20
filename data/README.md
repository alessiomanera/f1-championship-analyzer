# Data

Formula 1 data from **[Jolpica-F1](https://github.com/jolpica/jolpica-f1)**, the open-source successor to the Ergast Motor Racing database. The program reads only these local files, so it works offline.

## Provenance

| Item | Value |
| --- | --- |
| Source | Jolpica-F1 CSV database dump, free tier (published 14 days after upload) |
| Download page | <https://api.jolpi.ca/data/dumps/download/> |
| File downloaded | <https://api.jolpi.ca/data/dumps/download/delayed/?dump_type=csv> |
| Dump uploaded by Jolpica | 2026-11-02 20:02 UTC |
| Downloaded | 2026-11-20 |
| SHA-256 of the zip | `36e2099ca949e7438f3898f49cbf66ff0f93c752e067b18020affa5dd6e19925` (matches the hash Jolpica publishes) |
| Schema documentation | <https://dbdocs.io/jolpica/jolpica-f1> |
| Coverage | Race results for every season from 1950 to 2026; the 2026 season up to round 19 (Mexico City Grand Prix, 1 November 2026) |

## Licence

The data is © Jolpica-F1 contributors, licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) ([terms](https://github.com/jolpica/jolpica-f1/blob/main/TERMS.md)). It is used here for a non-commercial university project. **Changes:** only a subset of the dump's tables is included (below); the files themselves are unmodified. This licence covers the files in `data/`; the source code is under GPL-3.0 (see `LICENSE`).

## Files

The 14 files below are copied byte for byte from the dump; `.gitattributes` stops git from changing their line endings, so the checksums stay valid.

| File | Rows | SHA-256 |
| --- | --- | --- |
| `formula_one_championshipadjustment.csv` | 3 | `035bd369d5799081bf89cbe68db7015e454b383caf63cc9b4e3b20be0713b96f` |
| `formula_one_championshipsystem.csv` | 11 | `d41e396699a8d45c85a020da4642434b6a16754326a5723d240b8478af676a9c` |
| `formula_one_circuit.csv` | 78 | `df17d7c6dac3c00dbba3f0cbe6942e9f939feb9d1f37e691d40cef85776f821a` |
| `formula_one_driver.csv` | 884 | `5ad0a9ca7dddc563e11d01e8b3725d3cd7803bdd6e3a3a6d1c96c11abbdead72` |
| `formula_one_driverchampionship.csv` | 36965 | `54a8663120645c150e416750a21c4286c1f8ab66b1b5ea75300d99ac2976fe28` |
| `formula_one_pointsystem.csv` | 24 | `cccae2ec71f73d91e45a1da87bad9c6fb220fc67744e7d1ee40a06412100c89d` |
| `formula_one_round.csv` | 1173 | `1a843144e851e61ef01f9164129f0ec48dd5802092ac74404107560e353c6154` |
| `formula_one_roundentry.csv` | 27740 | `dd151049f97fdfb0e90c17f9414ff3f2c7c416dad2c0975e11dc7268c31b2f0f` |
| `formula_one_season.csv` | 77 | `8105785c76e4e8bc87198b22ba7210de56a05dc633ce0f754ba6c2a67b594c12` |
| `formula_one_session.csv` | 5130 | `82ec374f200d093e881553d58f61f2de7216c05315b1eeee0b338392fe1e6015` |
| `formula_one_sessionentry.csv` | 52121 | `86ef541430d94420eb3b1315da6fe8f8d802c712b50783bed8b2293f6768bcf3` |
| `formula_one_team.csv` | 214 | `1ba1e7a567d6f326d249a07d15b861ecc15a0b0ad465d9790b47959adc7c1b9a` |
| `formula_one_teamchampionship.csv` | 14623 | `cb25f9136c20571566a8a672a5bf7a5a08cb2245d076e1c2514d598d9f08c827` |
| `formula_one_teamdriver.csv` | 3633 | `e6d5741421de2c24f2738400ad6033eb876087c327a870936efccf592102e1a9` |

**Left out:** `formula_one_lap.csv` (37 MB, lap times from 1994) and `formula_one_pitstop.csv` (pit stops from 2011), until a feature needs them; `formula_one_penalty.csv` and `formula_one_baseteam.csv` are empty in this dump.

## How the tables connect

Every table has an integer `id`; a column ending in `_id` points to the `id` of another table.

```text
season ──< round ──< session ──< sessionentry >── roundentry >── teamdriver >── driver
  │          │                                                        │
  │          └── circuit                                              └── team
  └── championshipsystem

session ── pointsystem          driverchampionship / teamchampionship: standings after each round
```

Read `A ──< B` as "one A has many B". To get one race result:

1. `session` row with `type = R` (the race) belongs to a `round` (the Grand Prix), which belongs to a `season`.
2. Each `sessionentry` of that session is one car's result: `position`, `grid`, `points`, `laps_completed`, `time`, `status`.
3. `sessionentry.round_entry_id` → `roundentry` (car number) → `teamdriver` → `driver` and `team`.

`driverchampionship` and `teamchampionship` hold Jolpica's own standings after every round: useful for checking our standings calculation in tests.

## Value formats

| What | How it appears | Example |
| --- | --- | --- |
| Missing value | Empty field | `1,,driver_NNme7ruE,...` |
| Boolean | `t` or `f` | `is_classified = t` |
| Duration | `HH:MM:SS.fff` | `02:13:23.6` (race time), `00:01:16.29` (lap) |
| Date / timestamp | ISO 8601 | `1950-05-13`, `1950-05-13 00:00:00+00:00` |
| Line endings | Windows (`\r\n`) | open files with `newline=""`, as the `csv` module docs advise |

`session.type` codes (from Jolpica's source): `R` race, `SR` sprint race, `Q1` `Q2` `Q3` qualifying parts, `QB` best qualifying time, `QA` aggregate qualifying, `QO` qualifying order, `SQ1` `SQ2` `SQ3` sprint qualifying, `FP1` `FP2` `FP3` practice, `PQ` pre-qualifying.

`sessionentry.status` codes: `0` finished, `1` finished laps behind the leader, `10` accident or collision, `11` mechanical or other retirement, `20` disqualified, `30` did not start, `40` did not qualify, `41` did not pre-qualify. The `detail` column holds the text reason (for example `Engine`).

## Updating the data

Download the newer dump from the download page, check its SHA-256 against the published `file_hash`, replace the same 14 files, and update the provenance and checksum tables above in the same pull request.
