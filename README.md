# Asteroids (pygame)

A small **Asteroids**-style project built with **Python 3.13** and **pygame**.

Right now it boots pygame and prints the configured screen size from `constants.py`.

## Requirements

- Python **3.13+**
- `uv` (recommended) or another way to install dependencies
- `pygame==2.6.1` (locked in `pyproject.toml` / `uv.lock`)

## Project layout

- `main.py` — entry point
- `constants.py` — shared constants (screen width and height)
- `pyproject.toml` — project metadata and dependencies
- `uv.lock` — locked dependency versions

## Setup (uv)

From the repo root:

    uv sync

## Run

    uv run main.py

You should see output similar to:

- Starting Asteroids with pygame version: ...
- Screen width: 1280
- Screen height: 720

## Notes

- Screen dimensions are defined in `constants.py`:
  - `SCREEN_WIDTH = 1280`
  - `SCREEN_HEIGHT = 720`

