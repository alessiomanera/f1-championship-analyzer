# Roadmap

Every task and idea for the project, grouped by course requirement. Day-to-day status lives on the GitHub project board; this file is the overview.

## Requirement 1: git and GitHub

- [x] Public repository with GPL-3.0 licence and Python `.gitignore`
- [x] All five members added as collaborators
- [x] Kanban project board
- [x] Branch workflow (`feature/*` into `testing` into `main`) and protection on `main`
- [x] Team docs: `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, issue and pull request templates
- [x] Labels and GitHub milestones for the five course requirements
- [x] Merge methods enforced per branch (squash into `testing`, merge commit into `main`) and merged branches deleted automatically
- [ ] Agree code layers and who does what (team meeting)
- [ ] First release `v0.1.0` from `testing` into `main`, tagged
- [ ] Every member merges at least one reviewed pull request
- [ ] Every member reviews at least one teammate's pull request

## Data source (issues #1 and #3)

- [x] Compare candidate sources and choose one: Jolpica-F1 CSV dump (<https://github.com/jolpica/jolpica-f1>)
- [x] Choose the tables and seasons to keep: 14 tables, all seasons; laps and pit stops left out for now
- [x] Download the dump from <https://api.jolpi.ca/data/dumps/download/> into `data/`
- [x] Write `data/README.md`: source URL, download date, licence, checksums, table relationships

## Requirement 2: package structure

- [x] Choose the package name (`f1_championship_analyzer`)
- [x] `pyproject.toml`, `src/f1_championship_analyzer/`, `tests/`, `f1cli` entry point
- [x] PEP 8 check (`ruff`) and shared tool versions (`uv.lock`)

## Requirement 3: `csv` and `argparse`

- [ ] CSV loader with missing values (empty fields) and type conversion
- [ ] CLI commands: standings, race, driver, compare, fastest laps

## Requirement 4: object-oriented design

- [ ] Domain classes: driver, constructor, circuit, race, result, standings
- [ ] Scoring rules per era, checked against the FIA Sporting Regulations, and the tie-break rule

## Requirement 5: tests

- [ ] Unit tests: time parsing, points, tie-breaks, missing data, CLI arguments (each member writes the tests for their own part)
- [x] Continuous integration running the tests on every pull request

## Ideas after the requirements

- Visual layer for championship progression and lap-time comparisons (framework to be chosen)
- Telemetry from a second source (lap-by-lap data, pit stops) stored as a local snapshot
