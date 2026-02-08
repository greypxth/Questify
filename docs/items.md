# Items System

Items are structured entities that interact with multiple systems.

## Item Properties

Each item must include:
- id
- name
- type
- rarity

Optional properties may include:
- stat modifiers
- duration
- special effects

## Rarity Tiers

- Common
- Uncommon
- Rare
- Epic
- Legendary
- Mythic

Higher rarity implies:
- Stronger effects
- Rarer acquisition
- Higher store value

Items do not directly modify player state.
They emit effects that other systems process.
