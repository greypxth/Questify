import json
from pathlib import Path

CONFIG_PATH = Path("config.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def calculate_xp(action_type: str, multiplier: float = 1.0) -> int:
    """
    Returns XP for a completed action.
    """
    config = load_config()
    xp_table = config["xp"]

    if action_type not in xp_table:
        raise ValueError(f"Unknown XP action: {action_type}")

    base_xp = xp_table[action_type]
    xp = int(base_xp * multiplier)

    return xp


def apply_daily_cap(xp_gained: int, xp_today: int) -> int:
    """
    Enforces max daily XP limit.
    """
    config = load_config()
    cap = config["system"]["max_daily_xp"]

    if xp_today + xp_gained > cap:
        return max(0, cap - xp_today)

    return xp_gained


def apply_penalty(penalty_type: str) -> int:
    """
    Applies penalties like missed days.
    """
    config = load_config()
    penalties = config["xp"]

    if penalty_type not in penalties:
        raise ValueError(f"Unknown penalty: {penalty_type}")

    return penalties[penalty_type]
