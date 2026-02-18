def validate_item(item: dict) -> bool:
    required_keys = {"id", "name", "type", "rarity"}

    return required_keys.issubset(item.keys())


def item_effect(item_type: str) -> dict:
    """
    Returns effect metadata.
    """
    effects = {
        "consumable": {"temporary_boost": True},
        "equipment": {"permanent_boost": True},
        "key_item": {"quest_related": True}
    }

    return effects.get(item_type, {})
