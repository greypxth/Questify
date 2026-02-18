import json
from pathlib import Path

CONFIG_PATH = Path("config.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def can_afford(cost: int, balance: int) -> bool:
    return balance >= cost


def apply_transaction(balance: int, delta: int) -> int:
    """
    Delta can be positive (reward) or negative (cost).
    """
    return max(0, balance + delta)
