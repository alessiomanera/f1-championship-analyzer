# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/): each course milestone merged into `main` gets a minor version (`v0.1.0` for milestone 1, `v0.2.0` for milestone 2, and so on).

## [Unreleased]

### Added

- Jolpica-F1 data in `data/` (#1, #3): 14 tables from the 2026-11-02 dump, with provenance, licence, checksums and a table guide in `data/README.md`.
- Team documentation: `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `ROADMAP.md` and this changelog.
- Issue and pull request templates in `.github/`.
- `.gitattributes` to keep line endings consistent across Windows, macOS and Linux.
- Branch protection on `main` and `testing`: changes arrive only through reviewed pull requests.
- Data source chosen and documented in `README.md`: the Jolpica-F1 CSV dump (CC BY-NC-SA 4.0).

### Removed

- The initial package skeleton and dataset, removed from `main` so that each module is built by its owner through reviewed pull requests, starting from a documented data source.
