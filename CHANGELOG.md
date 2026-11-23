# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/): each release merged into `main` gets the next minor version (`v0.1.0`, `v0.2.0`, and so on, up to `v1.0.0` for the final submission).

## [Unreleased]

### Changed

- Merge rules enforced by GitHub (#16): `testing` accepts only squash merges and `main` only merge commits; merged branches are deleted from GitHub automatically. `CONTRIBUTING.md` explains the local clean-up after a squash merge and the optional auto-merge.
- `AGENTS.md` (#16): new "Coding assistants" rules (assistants explain, members type every command and write their own code); the project status section is replaced by a "Where things live" list pointing to `CONTRIBUTING.md`, `README.md`, `ROADMAP.md`, `CHANGELOG.md` and the project board.

## [0.1.0] - 2026-11-20

### Added

- Jolpica-F1 data in `data/` (#1, #3): 14 tables from the 2026-11-02 dump, with provenance, licence, checksums and a table guide in `data/README.md`.
- Team documentation: `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `ROADMAP.md` and this changelog.
- Issue and pull request templates in `.github/`.
- `.gitattributes` to keep line endings consistent across Windows, macOS and Linux.
- Branch protection on `main` and `testing`: changes arrive only through reviewed pull requests.
- Data source chosen and documented in `README.md`: the Jolpica-F1 CSV dump (CC BY-NC-SA 4.0).
- Package skeleton (#12): `src/` layout with the `f1_championship_analyzer` package, the `f1cli` command (`--help`, `--version`, `python -m` support) and its tests.
- Shared tooling: Python 3.12 pinned in `.python-version`, `uv` with a committed `uv.lock`, exact versions of `pytest` and `ruff` (PEP 8 checks and formatting).
- CI workflow running lint, formatting and tests on Windows, macOS and Linux for every pull request.
- Shared VS Code settings and recommended extensions in `.vscode/`.
