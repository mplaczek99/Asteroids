# Asteroids (pygame)

A small **Asteroids**-style project built with **Python 3.13** and **pygame**.

Right now it boots pygame and prints the configured screen size from `constants.py`.

## Requirements

- Python **3.13+**
- `uv` (recommended) or another way to install dependencies
- `pygame==2.6.1` (locked in `pyproject.toml` / `uv.lock`)

## Setup (uv)

From the repo root:

    uv sync

## Run

    uv run main.py

## Notes

- Screen dimensions are defined in `constants.py`
- `logger.py` exists to support Boot.dev test instrumentation
