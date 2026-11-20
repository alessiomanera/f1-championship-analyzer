# Roadmap

Every task and idea for the project, grouped by course milestone. Day-to-day status lives on the GitHub project board; this file is the overview.

## Milestone 1: git and GitHub (`v0.1.0`)

- [x] Public repository with GPL-3.0 licence and Python `.gitignore`
- [x] All five members added as collaborators
- [x] Kanban project board
- [x] Branch workflow (`feature/*` into `testing` into `main`) and protection on `main`
- [x] Team docs: `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, issue and pull request templates
- [ ] Labels and GitHub milestones for the five course requirements
- [ ] Every member merges at least one reviewed pull request

## Data source (issues #1 and #3)

- [x] Compare candidate sources and choose one: Jolpica-F1 CSV dump (<https://github.com/jolpica/jolpica-f1>)
- [x] Choose the tables and seasons to keep: 14 tables, all seasons; laps and pit stops left out for now
- [x] Download the dump from <https://api.jolpi.ca/data/dumps/download/> into `data/`
- [x] Write `data/README.md`: source URL, download date, licence, checksums, table relationships

## Milestone 2: package structure (`v0.2.0`)

- [ ] Choose the package name
- [ ] `pyproject.toml`, `src/<package>/`, `tests/`, CLI entry point
- [ ] PEP 8 check

## Milestone 3: `csv` and `argparse` (`v0.3.0`)

- [ ] CSV loader with missing values (`\N`) and type conversion
- [ ] CLI commands: standings, race, driver, compare, fastest laps

## Milestone 4: object-oriented design (`v0.4.0`)

- [ ] Domain classes: driver, constructor, circuit, race, result, standings
- [ ] Scoring rules per era, checked against the FIA Sporting Regulations, and the tie-break rule

## Milestone 5: tests (`v0.5.0`)

- [ ] Unit tests: time parsing, points, tie-breaks, missing data, CLI arguments
- [ ] Continuous integration running the tests on every pull request

## Ideas after the requirements

- Visual layer for championship progression and lap-time comparisons (framework to be chosen)
- Telemetry from a second source (lap-by-lap data, pit stops) stored as a local snapshot
