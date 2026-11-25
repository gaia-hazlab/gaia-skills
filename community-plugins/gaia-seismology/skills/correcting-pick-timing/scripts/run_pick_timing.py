#!/usr/bin/env python3
"""Run the bundled pick_timing package: python run_pick_timing.py <command> [options] (see --help)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pick_timing.cli import main  # noqa: E402

sys.exit(main())
