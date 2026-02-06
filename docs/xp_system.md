# XP System
XP is the primary currency of progression in Questify. All growth starts with XP.

## XP Sources
XP is earned through actions such as:
- Daily tasks
- Workouts
- Study or skill-building sessions
- Business or deep work
- Special missions
- Boss-level challenges

Each XP source has a predefined base value stored in `config.json`.

## XP Scaling
Level progression uses an exponential growth model:
- Early levels are easy to gain
- Higher levels require significantly more XP
- XP requirements scale using a growth rate multiplier

This prevents infinite leveling without effort and keeps progression meaningful long-term.

## Daily Limits and Penalties
- A maximum daily XP cap exists to prevent burnout and abuse
- Missed days or broken streaks may apply XP penalties
- Negative XP is allowed if enabled in system settings

XP values are rounded for clarity and consistency.

XP does not directly modify stats. Stats are calculated through separate logic to maintain balance and control.
