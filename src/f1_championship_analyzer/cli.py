"""Command-line interface for the ``f1cli`` command.

The skeleton only offers ``--help`` and ``--version``; each feature adds its own
subcommand to :func:`build_parser` in its own pull request.
"""

import argparse
from collections.abc import Sequence

from f1_championship_analyzer import __version__


def build_parser() -> argparse.ArgumentParser:
    """Create the top-level argument parser for ``f1cli``."""
    parser = argparse.ArgumentParser(
        prog="f1cli",
        description="Analyse Formula 1 championships from local CSV data.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command line and return the process exit code.

    Args:
        argv: Arguments without the program name; ``None`` reads ``sys.argv``.
    """
    parser = build_parser()
    parser.parse_args(argv)
    parser.print_help()
    return 0
