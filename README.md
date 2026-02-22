# Asteroids (pygame)

A classic **Asteroids-style arcade game** built with **Python** and **pygame**.  
This side-project focuses on clean structure, sprite-based architecture, and simple, readable game logic.

---

## Features

- Player-controlled ship with rotation, thrust, and shooting
- Procedurally spawning asteroids from screen edges
- Asteroids split into smaller pieces when shot
- Collision detection between:
  - player ↔ asteroid
  - shot ↔ asteroid
- Sprite group–based update and draw system
- Structured game-state and event logging (JSONL)

---

## Controls

| Key | Action |
|-----|--------|
| `W` | Thrust forward |
| `S` | Thrust backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |
| Close window | Quit |

---

## Project Structure

```
Asteroids/
├── main.py              # Game entry point and main loop
├── player.py            # Player movement, rotation, shooting
├── asteroid.py          # Asteroid behavior and splitting logic
├── asteroidfield.py     # Asteroid spawning system
├── shot.py              # Projectile behavior
├── circleshape.py       # Base class for circular game objects
├── constants.py         # Game tuning values and configuration
├── logger.py            # Game state + event logging (JSONL)
├── game_state.jsonl     # Auto-generated state snapshots
├── game_events.jsonl    # Auto-generated gameplay events
├── pyproject.toml       # Project metadata and dependencies
├── uv.lock              # Locked dependency versions
└── README.md
```

---

## Architecture Overview

### Sprite System

All game objects inherit from `CircleShape`, which provides:
- position and velocity (`pygame.Vector2`)
- radius-based collision detection
- a shared interface for `update()` and `draw()`

Sprites are organized into logical `pygame.sprite.Group`s:
- `updatable`
- `drawable`
- `asteroids`
- `shots`

This allows clean separation of logic and rendering.

---

### Asteroids

- Spawn randomly from screen edges
- Travel inward with randomized velocity and angle
- Split into two smaller asteroids when shot
- Disappear when below minimum size

---

### Player

- Rotates independently of movement
- Thrust-based movement (no instant velocity snapping)
- Shooting uses a cooldown timer
- Collision with an asteroid ends the game

---

## Logging

The game automatically logs runtime data to JSON Lines files:

### `game_state.jsonl`

- Periodic snapshots (~1 per second)
- Sprite counts and sampled positions
- Velocities, rotations, radii
- Screen size and frame number

### `game_events.jsonl`

Logs discrete events such as:
- `asteroid_shot`
- `asteroid_split`
- `player_hit`

---

## Requirements

- **Python 3.13+**
- **pygame 2.6.1**

Dependencies are defined in `pyproject.toml`.

---

## Setup & Run

Using **uv** (recommended):

```bash
uv sync
uv run python main.py
```

Or using pip:

```bash
pip install pygame
python main.py
```

---

## Current Status

Implemented:
- Core movement and shooting
- Asteroid spawning and splitting
- Collision handling
- Logging system

Not yet implemented:
- Scoring
- Lives / restart flow
- Screen wrapping
- Sound effects
- UI / HUD

---

## Goals

This project is primarily focused on:
- Writing readable, maintainable pygame code
- Understanding game loops and delta time
- Learning sprite-based architecture
- Building tooling (logging) alongside gameplay
