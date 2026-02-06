import json
from pathlib import Path

CONFIG_PATH = Path("config.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def calculate_stat_gain(stat_name: str, xp_gained: int, daily_stat_gain: int) -> int:
    """
    Returns stat points gained from XP.
    """
    config = load_config()
    stats_config = config["stats"]

    if stat_name not in stats_config:
        raise ValueError(f"Unknown stat: {stat_name}")

    multiplier = stats_config[stat_name]["xp_multiplier"]
    max_gain = stats_config[stat_name]["max_daily_gain"]

    raw_gain = int(xp_gained * multiplier / 100)
    remaining = max_gain - daily_stat_gain

    return max(0, min(raw_gain, remaining))
