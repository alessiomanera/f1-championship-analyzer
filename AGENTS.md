# AGENTS.md

Shared rules for everyone working in this repository: the five team members and any coding assistant a member uses. Read this file before changing anything. Workflow details live in [CONTRIBUTING.md](CONTRIBUTING.md).

## Project

- **What:** Formula 1 Championship and Telemetry Analyzer, a Python command-line tool that loads Formula 1 history from local CSV files, models it with classes and answers questions about races, drivers, constructors and championship standings.
- **Why:** group project for Lab of Software Project Development (ET7018), Ca' Foscari University of Venice @ H-Farm, AY 2026-27. The repository is public and the professor reviews it, including the git history.
- **Team:** Alessio Manera, Simone Angelo Vasilescu, Alice Comino, Andrea Graziano Gitto, Francesco Domenico Saltarelli.

## Course requirements

The project is graded on five requirements, built in this order as the course covers each topic:

1. Use git and GitHub to set up and run the project (issues, Kanban board, branches, pull requests).
2. Provide the standard Python package structure (`src/` layout, `pyproject.toml`, PEP 8).
3. Read data with the standard library `csv` module and expose a multi-command CLI with `argparse`.
4. Structure the code in an object-oriented way (drivers, constructors, circuits, races, results, standings).
5. Provide tests for the project code.

The course asks for little code that applies each week's technique well. Prefer a small, tested, readable feature over a large one.

## Rules

- **One issue, one branch, one pull request.** Work only inside the scope of the issue you are on, and assign yourself to it so the team knows who is working on what. The split of modules between members is not decided yet; until it is, agree in the issue before changing code someone else is working on.
- **Branches:** `feature/*` and `fix/*` branches open pull requests into `testing`; `testing` merges into `main` only for a release. Nobody pushes to `main` directly (GitHub enforces it). Details in [CONTRIBUTING.md](CONTRIBUTING.md).
- **Offline data:** the program reads only the CSV files in `data/`, never a live API, so it works during the oral exam without internet. Every dataset records its source URL, download date, licence and checksum in `data/README.md`.
- **Same tools for everyone:** the project uses `uv` (Python 3.12 from `.python-version`, exact tool versions from `uv.lock`). Install with `uv sync`, add a package with `uv add`, and commit the updated `uv.lock`. Before every pull request, run `uv run ruff check .`, `uv run ruff format --check .` and `uv run pytest`; CI runs the same checks and must pass.
- **Standard library core:** loading, models, scoring and the CLI use only the Python standard library. A third-party package needs a team decision recorded in the issue first.
- **Authorship:** commits carry the real name of the member who made them, with no AI co-author trailers. Whoever commits AI-assisted code must understand it well enough to explain it at the oral exam.
- **Personal data:** never commit student IDs, email addresses, tokens or private document links.
- **Writing style:** punctuate with commas, semicolons, colons, full stops, parentheses or line breaks; never use the em dash character in any file, commit message or pull request.
- **Docs move with code:** a change that alters behaviour updates `README.md` and adds a line to `CHANGELOG.md` under `Unreleased`.
- **Shared Google Doc in sync:** whoever changes how we work updates the shared team Google Doc the same day (tabs: `REFERENCE`, `GIT WORKFLOW`, `DECISIONS`, `Team meeting brief`, `Formula 1 Project Plan`). Every new decision and the reason for it goes into `DECISIONS`. If the doc and this repository disagree, the repository wins.

## Current state

- **Goal:** deliver the five course requirements, then a visual layer for exploring race and championship trends.
- **Done:** repository, licence (GPL-3.0), collaborators, Kanban board, branch protection on `main` and `testing`, team docs (`README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `ROADMAP.md`, issue and pull request templates), package skeleton (#12/PR #13 merged into `testing`), Jolpica data (#3/PR #14, 14 tables, merged into `testing`), multi-OS CI passing on Windows, macOS, Linux, shared Google Doc tabs ("Team meeting brief" and "GIT WORKFLOW"), personal cheat sheet in `_PERSONAL/CHEAT_SHEET.md`.
- **Data source (decided 2026-11-20):** the Jolpica-F1 CSV dump (<https://github.com/jolpica/jolpica-f1>, download at <https://api.jolpi.ca/data/dumps/download/>), licensed CC BY-NC-SA 4.0. It uses Jolpica's own table layout (`formula_one_*.csv`), not the old Ergast files; links and details are in `README.md`.
- **Merged into `testing`:** PR #13 (skeleton), #14 (data), #15 (changelog for `v0.1.0`). `main` is not released yet (no tag).
- **Merge rules (2026-11-23):** `testing` accepts only squash merges, `main` only merge commits; merged branches are deleted from GitHub automatically; auto-merge is optional, off by default.
- **Tests:** each member writes the tests for their own part.
- **In progress:** issue #16, workflow docs sync (`docs/16-workflow-sync`).
- **Next:** team meeting this week: agree code layers and who does what, review the workflow together, assign issues #1 to #10, release `v0.1.0` (`testing` -> `main`, merge commit, tag).
- **Open decisions:** how the team splits the work (draft in the Google Doc); which tables and seasons to keep; visual layer framework.
- **Last updated:** 2026-11-23.
