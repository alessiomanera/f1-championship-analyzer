# Contributing

How the team works in this repository. The shared rules are in [AGENTS.md](AGENTS.md).

## Setup

Clone with the HTTPS URL (the H-Farm network may block SSH):

```bash
git clone https://github.com/alessiomanera/f1-championship-analyzer.git
cd f1-championship-analyzer
git switch testing
```

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) once per laptop, then set up the project:

```bash
uv sync                 # installs Python 3.12, the package and the pinned tools into .venv
uv run f1cli --help     # check that it works
```

`uv` reads `.python-version` and `uv.lock`, so every laptop and CI use exactly the same Python, `pytest` and `ruff` versions. Open the folder in VS Code and accept the recommended extensions (GitHub Pull Requests, Python, Ruff).

## Checks before every pull request

```bash
uv run ruff check .          # PEP 8 and common errors
uv run ruff format --check . # formatting (run without --check to fix it)
uv run pytest                # tests
```

CI runs the same three checks on Windows, macOS and Linux for every pull request; a red check blocks the merge.

To add a package: `uv add <name>` (or `uv add --dev <name>` for a development tool), then commit both `pyproject.toml` and `uv.lock`. The core code stays standard library only (see [AGENTS.md](AGENTS.md)).

## Branches

| Branch | Purpose | Who writes to it |
| --- | --- | --- |
| `main` | Stable version, updated only by a release, what the professor reviews | Pull request from `testing` only, at least 1 approval, merge commit |
| `testing` | Integration branch where finished features meet | Pull requests from feature branches, at least 1 approval, squash merge |
| `feature/<issue>-<short-name>` | One issue's work, e.g. `feature/4-csv-loader` | The member assigned to the issue |
| `fix/<issue>-<short-name>` | A bug fix, e.g. `fix/9-null-lap-time` | The member assigned to the issue |
| `docs/<issue>-<short-name>` | Documentation only | Anyone |

`main` and `testing` are never deleted.

## Workflow for one issue

1. Pick an issue on the project board, assign yourself and move it to **In Progress**.
2. Start from an up-to-date `testing`:
   ```bash
   git switch testing
   git pull
   git switch -c feature/4-csv-loader
   ```
3. Commit small steps (see the commit style below) and push your branch:
   ```bash
   git push -u origin feature/4-csv-loader
   ```
4. Open a pull request with **base: `testing`** (GitHub suggests `main` by default: change it). Fill in the template and write `Refs #4`.
5. Move the card to **In Review** and ask a teammate to review. Address the comments with new commits; a new push cancels earlier approvals, so the reviewer approves the final version.
6. After at least one approval and green CI, the author clicks **Squash and merge** (the only merge method `testing` accepts). GitHub then deletes the branch on GitHub by itself. Move the issue to **Done** and close it by hand: GitHub closes issues automatically only for merges into `main`.
   Auto-merge is optional and off by default: **Enable auto-merge** on a pull request merges it by itself as soon as it has its approval and green CI.
7. Clean up your laptop:
   ```bash
   git switch testing
   git pull
   git fetch --prune                  # forget branches deleted on GitHub
   git branch -D feature/4-csv-loader
   ```
   The capital `-D` is needed because a squash merge creates a new commit on `testing`, so git cannot see that your branch's own commits were merged and the safe `-d` refuses. Never keep working on a branch after it was merged: start a new one from `testing`.

If `testing` moved on while you worked, update your branch before asking for review:

```bash
git switch testing && git pull
git switch feature/4-csv-loader
git merge testing
```

## Releases

When `testing` holds a stable set of finished work (usually one or more course requirements), one member opens a pull request from `testing` into `main`:

1. In that pull request, rename the `CHANGELOG.md` section `Unreleased` to the new version and date, and set the same version in `pyproject.toml`.
2. After approval and green CI, merge it with **Create a merge commit** (the only merge method `main` accepts). GitHub does not delete `testing` afterwards: the branch rules forbid deleting `main` and `testing`.
3. Tag the merge commit on `main` (`git tag v0.1.0 && git push origin v0.1.0`).

Each release gets the next minor version: `v0.1.0`, `v0.2.0`, and so on, up to `v1.0.0` for the final submission.

## Commit style

Use [Conventional Commits](https://www.conventionalcommits.org/): a type, a short summary in the imperative, and the issue number.

```text
feat(loader): read races.csv into Race objects (#4)
fix(scoring): drop fastest-lap point from 2025 (#12)
test(cli): reject years before 1950 (#15)
docs: explain the data licence (#3)
```

Types: `feat`, `fix`, `test`, `docs`, `refactor`, `chore`. Commits carry your own name and email, with no AI co-author lines.

## Code style

- PEP 8, with a docstring on every public module, class and function.
- Type hints on function signatures.
- Core code uses only the Python standard library (see [AGENTS.md](AGENTS.md)).
- Every pull request that changes behaviour adds or updates tests and a line in `CHANGELOG.md`.
