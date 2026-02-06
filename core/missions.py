import json
from pathlib import Path

CONFIG_PATH = Path("config.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def can_accept_mission(mission_type: str, completed_today: int, completed_week: int) -> bool:
    config = load_config()
    missions = config["missions"]

    if mission_type == "daily":
        return completed_today < missions["daily_limit"]

    if mission_type == "special":
        return completed_week < missions["special_limit_per_week"]

    if mission_type == "boss":
        return True

    raise ValueError("Unknown mission type")


def mission_xp(mission_type: str) -> int:
    config = load_config()
    xp_table = config["xp"]

    if mission_type == "daily":
        return xp_table["daily_task"]

    if mission_type == "special":
        return xp_table["special_mission"]

    if mission_type == "boss":
        return xp_table["boss_mission"]

    raise ValueError("Unknown mission type")
