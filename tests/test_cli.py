"""Tests for the command-line entry point of the package skeleton."""

import subprocess
import sys
from pathlib import Path

import pytest

from f1_championship_analyzer import __version__
from f1_championship_analyzer.cli import build_parser, main


def test_version_flag_prints_package_version(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])

    assert exit_info.value.code == 0
    assert capsys.readouterr().out.strip() == f"f1cli {__version__}"


def test_no_arguments_prints_help_and_succeeds(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main([])

    assert exit_code == 0
    assert "usage: f1cli" in capsys.readouterr().out


def test_unknown_option_exits_with_usage_error() -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--not-an-option"])

    assert exit_info.value.code == 2


def test_parser_uses_cli_name() -> None:
    assert build_parser().prog == "f1cli"


def test_package_runs_as_module() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "f1_championship_analyzer", "--version"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == f"f1cli {__version__}"


def test_root_main_runs_as_script() -> None:
    root_main = Path(__file__).resolve().parents[1] / "main.py"
    result = subprocess.run(
        [sys.executable, str(root_main), "--version"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == f"f1cli {__version__}"
