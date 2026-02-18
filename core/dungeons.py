import json
from pathlib import Path

CONFIG_PATH = Path("config.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def dungeon_unlocked(level: int) -> bool:
    config = load_config()
    return level >= config["dungeons"]["unlock_level"]


def calculate_dungeon_reward(base_xp: int, difficulty: str) -> int:
    multipliers = {
        "easy": 1.0,
        "normal": 1.5,
        "hard": 2.2,
        "nightmare": 3.5
    }

    if difficulty not in multipliers:
        raise ValueError("Unknown dungeon difficulty")

    return int(base_xp * multipliers[difficulty])
