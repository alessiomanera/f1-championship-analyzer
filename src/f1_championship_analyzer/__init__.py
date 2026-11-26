"""Formula 1 Championship and Telemetry Analyzer.

Loads Formula 1 race history from local CSV files and answers questions about
races, drivers, constructors and championship standings.
"""

from importlib.metadata import version

# Single source of truth: the version in pyproject.toml.
__version__ = version("f1-championship-analyzer")

__all__ = ["__version__"]
