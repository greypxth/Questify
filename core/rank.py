import json
from pathlib import Path

CONFIG_PATH = Path("config.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def get_rank_from_level(level: int) -> str:
    """
    Determines rank based on level.
    """
    config = load_config()
    ranks = config["ranks"]

    current_rank = "E"

    for rank, (min_lvl, max_lvl) in ranks.items():
        if level >= min_lvl and (max_lvl == -1 or level <= max_lvl):
            current_rank = rank

    return current_rank


def check_rank_up(old_level: int, new_level: int) -> bool:
    """
    Returns True if rank changes between levels.
    """
    return get_rank_from_level(old_level) != get_rank_from_level(new_level)
