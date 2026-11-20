# Contributing

How the team works in this repository. The shared rules are in [AGENTS.md](AGENTS.md).

## Setup

Clone with the HTTPS URL (the H-Farm network may block SSH):

```bash
git clone https://github.com/alessiomanera/f1-championship-analyzer.git
cd f1-championship-analyzer
git switch testing
```

## Branches

| Branch | Purpose | Who writes to it |
| --- | --- | --- |
| `main` | Stable version, one merge per course milestone, what the professor reviews | Pull request from `testing` only, 1 approval |
| `testing` | Integration branch where finished features meet | Pull requests from feature branches, 1 approval |
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
5. Move the card to **In Review** and ask a teammate to review. Address the comments with new commits.
6. After one approval, the author merges with **Squash and merge** and deletes the feature branch. Move the issue to **Done** and close it by hand: GitHub closes issues automatically only for merges into `main`.

If `testing` moved on while you worked, update your branch before asking for review:

```bash
git switch testing && git pull
git switch feature/4-csv-loader
git merge testing
```

## Milestone releases

When a course milestone is complete on `testing`, one member opens a pull request from `testing` into `main`. After approval it is merged with a merge commit, tagged (`v0.1.0` for milestone 1, `v0.2.0` for milestone 2, and so on) and the `CHANGELOG.md` section `Unreleased` is renamed to that version.

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
