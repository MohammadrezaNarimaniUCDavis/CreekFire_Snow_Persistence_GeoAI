"""Run the public replication entrypoints in order."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STEPS = [
    ROOT / "src" / "analysis" / "31_recompute_baci.py",
    ROOT / "src" / "analysis" / "32_summarize_metrics.py",
    ROOT / "src" / "manuscript" / "50_make_tables.py",
]


def main() -> int:
    for step in STEPS:
        print(f"\n=== {step.name} ===")
        proc = subprocess.run([sys.executable, str(step)], cwd=ROOT)
        if proc.returncode != 0:
            return proc.returncode
    print("\nPipeline complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
