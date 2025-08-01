import json
from pathlib import Path
from typing import Any


CONFIG_DIR = Path.cwd()
CONFIG_FILE = CONFIG_DIR / "config.json"
DEFAULT_DB_DIR = Path.cwd() 

def load_config(config_path: Path = CONFIG_FILE):
    if not config_path.exists():
        return {"database_dir": str(DEFAULT_DB_DIR)}
    with open(config_path, "r") as file:
        return json.load(file)
    
def save_config(config: dict[str, Any]):
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)
