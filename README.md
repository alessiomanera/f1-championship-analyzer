# Formula 1 Championship and Telemetry Analyzer

A Python command-line tool that loads Formula 1 race history from local CSV files, models it with classes and answers questions about races, drivers, constructors and championship standings.

Group project for **Lab of Software Project Development (ET7018)**, Ca' Foscari University of Venice @ H-Farm, academic year 2026-27.

## Team

- Alessio Manera
- Simone Angelo Vasilescu
- Alice Comino
- Andrea Graziano Gitto
- Francesco Domenico Saltarelli

## Status

Planning phase: the repository, team workflow and project board are set up and the data source is chosen; the dataset download and the package skeleton come next. Progress is tracked on the GitHub project board and in [ROADMAP.md](ROADMAP.md).

## Course requirements

| # | Requirement | Status |
| --- | --- | --- |
| 1 | git and GitHub: issues, Kanban board, branches, pull requests | In progress |
| 2 | Standard Python package structure | Not started |
| 3 | `csv` data loading and `argparse` CLI | Not started |
| 4 | Object-oriented design | Not started |
| 5 | Tests | Not started |

## Data

The tool will read relational CSV files stored in `data/`, so it runs fully offline. The data comes from **[Jolpica-F1](https://github.com/jolpica/jolpica-f1)**, the open-source successor to the Ergast Motor Racing database, which covers every championship season from 1950, with lap times and pit stops for recent seasons.

| Resource | Link |
| --- | --- |
| Project | <https://github.com/jolpica/jolpica-f1> |
| CSV dump download (metadata, URLs, SHA-256 hashes) | <https://api.jolpi.ca/data/dumps/download/> |
| Dump documentation | <https://github.com/jolpica/jolpica-f1/blob/main/docs/database_dumps.md> |
| Database schema | <https://dbdocs.io/jolpica/jolpica-f1> |
| Terms of use and licence | <https://github.com/jolpica/jolpica-f1/blob/main/TERMS.md> |

The Jolpica data is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) and free for non-commercial use. When the files are added, `data/README.md` will record the download date, the dump's SHA-256 hash and the tables used.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch workflow, commit style and review process, and [AGENTS.md](AGENTS.md) for the shared project rules.

## License

The source code is licensed under the GNU General Public License v3.0; see [LICENSE](LICENSE). Third-party data in `data/` keeps its own licence, stated in `data/README.md`.
