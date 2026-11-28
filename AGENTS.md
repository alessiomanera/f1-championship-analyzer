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
- **Same tools for everyone:** the project uses `uv` (Python 3.12 from `.python-version`, exact tool versions from `uv.lock`). Sync with `uv sync --locked` after pulling or switching branches (never use `pip` inside `.venv`), add packages with `uv add --dev <pkg>` (dev/scripts/tests) or `uv add <pkg>` (runtime in `src/`), and commit both `pyproject.toml` and `uv.lock`. Before every pull request, run `uv run ruff check .`, `uv run ruff format --check .` and `uv run pytest`; CI runs the same checks and must pass.
- **Core vs third-party packages:** core loading (`csv`), models, scoring and the CLI (`argparse`) prefer the Python standard library. When a task needs a third-party package, any member may add it with `uv add --dev <pkg>` (scripts, data prep, tests) or `uv add <pkg>` (runtime in `src/`), committing both `pyproject.toml` and `uv.lock` and noting the reason in the PR and `DECISIONS`.
- **Authorship:** commits carry the real name of the member who made them, with no AI co-author trailers.
- **Personal data:** never commit student IDs, email addresses, tokens or private document links.
- **Writing style:** punctuate with commas, semicolons, colons, full stops, parentheses or line breaks; never use the em dash character in any file, commit message or pull request.
- **English only:** write all code, comments, docstrings, CLI text, documentation, issues, pull requests and commit messages in English.
- **Docs move with code:** a change that alters behaviour updates `README.md` and adds a line to `CHANGELOG.md` under `Unreleased`.
- **Shared Google Doc in sync:** whoever changes how we work updates the shared team Google Doc the same day (main tabs: `REFERENCE`, `STEPS TO FOLLOW`, `DECISIONS`, `Team meeting brief`, `Formula 1 Project Plan`). Every new decision and the reason for it goes into `DECISIONS`. If the doc and this repository disagree, the repository wins.

## Coding assistants

We use coding assistants as tutors, not as substitutes: the point of this project is to learn git, GitHub and Python ourselves.

- **Explain, do not do:** an assistant explains which command or approach to use, why, and what it will do. The member types and runs every command (`git`, `gh`, `uv`) and writes their own code.
- **No actions on a member's behalf:** an assistant does not commit, push, merge, open or review pull requests, and does not write a member's module. It may explain, show short examples and review code the member wrote.
- **Trivial exceptions:** an assistant may do a very small, mechanical task itself (for example fixing a typo in a document) only after the member confirms it.
- **Understand what you commit:** every member can explain every line they commit, at the oral exam too.

## Where things live

- **How we work, step by step:** [CONTRIBUTING.md](CONTRIBUTING.md) (setup, branches, pull requests, reviews, releases, commit style).
- **What the project is and how to use it:** [README.md](README.md).
- **What is planned:** [ROADMAP.md](ROADMAP.md).
- **What has changed:** [CHANGELOG.md](CHANGELOG.md).
- **Who is doing what right now:** the GitHub project board.
