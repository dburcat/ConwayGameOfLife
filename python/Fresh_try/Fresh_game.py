import random
import time
import os


def create_grid(size: int) -> list[list[int]]:
    """Return a square matrix initialized with random 0/1 values."""
    return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]


def count_live_neighbors(grid: list[list[int]], row: int, col: int) -> int:
    """Count the number of black cells (1s) around a position, wrapping at edges.

    The top row is considered adjacent to the bottom row and the left column
    adjacent to the right column.  This makes the grid behave like a torus and
    ensures the upper-​left corner is connected to the bottom‑right corner.
    """
    n = len(grid)
    count = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            r = (row + dr) % n
            c = (col + dc) % n
            count += grid[r][c]
    return count


def next_generation(grid: list[list[int]]) -> list[list[int]]:
    """Compute the next state of the grid using the Game of Life rules."""
    n = len(grid)
    new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            live = grid[i][j] == 1
            neighbors = count_live_neighbors(grid, i, j)
            if live:
                # black stays black with two or three neighbors
                new[i][j] = 1 if neighbors in (2, 3) else 0
            else:
                # white becomes black with exactly three neighbors
                new[i][j] = 1 if neighbors == 3 else 0
    return new


def display(grid: list[list[int]]) -> None:
    """Print the grid to the console, clearing the screen first.

    Uses an ANSI escape sequence for portability; falls back to
    ``os.system`` if that appears to fail.  The previous version relied
    on the terminal type being set which can be omitted in some
    environments ("TERM environment variable not set" warning).
    """
    # a simple cursor‑home + erase‑rest sequence, works even if TERM is
    # missing or the shell is non‑interactive.
    print("\033[H\033[J", end="")
    for row in grid:
        print("".join("█" if cell else " " for cell in row))


from typing import Optional


def run(size: int = 50, delay: float = 0.2, max_generations: Optional[int] = None) -> None:
    """Run the simulation with an optional generation limit.

    If ``max_generations`` is ``None`` the simulation continues until
    interrupted by the user; otherwise it stops once the requested number
    of generations have been produced.
    """
    grid = create_grid(size)
    generation = 0
    while True:
        try:
            display(grid)
            print(f"Generation: {generation}")
            if max_generations is not None and generation >= max_generations:
                print("\nReached generation limit.")
                break
            grid = next_generation(grid)
            generation += 1
            time.sleep(delay)
        except KeyboardInterrupt:
            # user pressed Ctrl-C; exit the loop cleanly
            print("\nSimulation stopped.")
            break


if __name__ == "__main__":
    # default parameters; call with ``python Fresh_game.py <size> <delay> <max>``
    import sys

    args = sys.argv[1:]
    size = int(args[0]) if len(args) >= 1 else 50
    delay = float(args[1]) if len(args) >= 2 else 0.2
    max_gen = int(args[2]) if len(args) >= 3 else 500
    run(size=size, delay=delay, max_generations=max_gen)
