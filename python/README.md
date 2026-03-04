# Python Conway's Game of Life Lab

This folder contains a Python version of the same lab from `java/src`.

## Graphics library choice

Use `tkinter` for the display window.

- It ships with standard Python on macOS, Windows, and most Linux installs.
- No extra package install is required for a beginner-friendly starter lab.
- It is enough to draw a 2D cell grid and animate generations.

## Structure

- `src/zipcodeconway/conway_game_of_life.py` - simulation starter class
- `src/zipcodeconway/simple_window.py` - simple display helper using `tkinter`
- `tests/test_conway_game_of_life.py` - two starter tests equivalent to Java tests

## Run

From this `python/` folder:

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

Run the visual simulation starter:

```bash
PYTHONPATH=src python -m zipcodeconway.conway_game_of_life
```

## Lab expectations

This starter is intentionally scaffolded at about the same level as the Java version:

- core methods are present,
- method signatures and flow are set,
- comments/docstrings describe what to implement,
- students complete the actual game logic.
