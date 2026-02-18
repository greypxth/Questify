def create_item(
    item_id: str,
    name: str,
    item_type: str,
    rarity: str,
    effects: dict = None
) -> dict:
    return {
        "id": item_id,
        "name": name,
        "type": item_type,
        "rarity": rarity,
        "effects": effects or {}
    }


def is_valid_item(item: dict) -> bool:
    required_keys = {"id", "name", "type", "rarity"}
    return required_keys.issubset(item.keys())


def rarity_multiplier(rarity: str) -> float:
    table = {
        "common": 1.0,
        "uncommon": 1.2,
        "rare": 1.5,
        "epic": 2.0,
        "legendary": 3.0,
        "mythic": 5.0
    }

    if rarity not in table:
        raise ValueError("Unknown item rarity")

    return table[rarity]
