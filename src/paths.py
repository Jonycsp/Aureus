from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

HISTORY_FILE = DATA_DIR / "runtime_history.csv"
DISCOVERIES_FILE = DATA_DIR / "discoveries.csv"
TELEMETRY_FILE = DATA_DIR / "telemetry.csv"

SAVES_DIR = DATA_DIR / "saves"

DOCS_DIR = PROJECT_ROOT / "docs"
RELEASES_DIR = PROJECT_ROOT / "Releases"

SAVE_FILES = [
    SAVES_DIR / "save1.json",
    SAVES_DIR / "save2.json",
    SAVES_DIR / "save3.json",
    SAVES_DIR / "save4.json",
]

AUTOSAVE_TMP = SAVES_DIR / "session.tmp"

AUTOSAVE_FILE = SAVES_DIR / "autosave.json"
CURRENT_SORT = "slot"
SORT_NAMES = {
    "slot": "Slot Number",
    "name": "Name (A–Z)",
    "modified": "Last Modified",
    "progress": "Progress",
    "discoveries": "Discoveries",
}

VERSION = "0.9"
CODENAME = "Phoenix"

FULL_VERSION = f"v{VERSION} - {CODENAME}"
