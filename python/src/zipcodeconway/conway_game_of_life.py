from zipcodeconway.simple_window import SimpleWindow


class ConwayGameOfLife:
    """Starter scaffold for Conway's Game of Life lab."""

    def __init__(self, dimension: int, start_matrix: list[list[int]] | None = None):
        self.dimension = dimension
        self.display_window = SimpleWindow(dimension)

        if start_matrix is None:
            self.current_generation = self.create_random_start(dimension)
        else:
            self.current_generation = start_matrix

        self.next_generation = [[0 for _ in range(dimension)] for _ in range(dimension)]

    def create_random_start(self, dimension: int) -> list[list[int]]:
        """
        Contains the logic for the starting scenario.
        Which cells are alive or dead in generation 0.
        Allocates and returns the starting matrix of size 'dimension'.
        """
        return [[0]]

    def simulate(self, max_generations: int) -> list[list[int]]:
        """
        Simulate Conway's Game of Life for max_generations and return final matrix.

        Starter flow:
        - display current generation
        - compute each next cell using is_alive(...)
        - copy next_generation into current_generation and clear next_generation
        - sleep briefly so animation can be seen
        """
        return [[0]]

    def copy_and_zero_out(self, next_matrix: list[list[int]], current_matrix: list[list[int]]) -> None:
        """
        Copy all values from next_matrix to current_matrix,
        then set all values in next_matrix to 0.
        """
        pass

    def is_alive(self, row: int, col: int, world: list[list[int]]) -> int:
        """
        Calculate if the cell at row,col should be alive in the next generation.

        Game rules:
        - Any live cell with fewer than two live neighbours dies.
        - Any live cell with more than three live neighbours dies.
        - Any live cell with two or three live neighbours lives.
        - Any dead cell with exactly three live neighbours becomes alive.

        Use wraparound edges: top/bottom and left/right connect.
        """
        return 0


def main() -> None:
    sim = ConwayGameOfLife(50)
    sim.simulate(50)


if __name__ == "__main__":
    main()
