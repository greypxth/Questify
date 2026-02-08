# Store System
The Store system handles currency-based interactions such as rewards, purchases, and upgrades. It does not store player inventory or balances. It only defines rules and validation logic.

## Purpose
- Validate whether a player can afford an item
- Apply rewards or costs
- Enforce economy balance rules

## Currency
Currency is earned through:
- Level ups
- Special missions
- Boss missions
- Dungeon clears
- Rank-up rewards

Currency cannot go below zero.

## Design Rules
- Store logic never modifies inventory directly
- Prices and rewards are configuration-driven
- Store operations are atomic and reversible

The Store system acts as the economic gatekeeper of Questify.
