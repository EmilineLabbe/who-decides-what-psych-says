"""Put notebooks/ on the import path so the helper modules can be imported by name."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "notebooks"))
