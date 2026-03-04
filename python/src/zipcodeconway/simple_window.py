import tkinter as tk


class SimpleWindow:
    """A minimal drawing window for Conway's Game of Life."""

    def __init__(self, dimension: int):
        self.enabled = True
        self.dimension = dimension
        self.box_dim = 10
        self.pixel_size = max(100, self.dimension * self.box_dim)

        try:
            self.root = tk.Tk()
            self.root.geometry(f"{self.pixel_size}x{self.pixel_size}")
            self.canvas = tk.Canvas(
                self.root,
                width=self.dimension * self.box_dim,
                height=self.dimension * self.box_dim,
                bg="white",
                highlightthickness=0,
            )
            self.canvas.pack()
            self.root.update()
        except tk.TclError:
            self.enabled = False
            self.root = None
            self.canvas = None

    def sleep(self, milliseconds: int) -> None:
        if not self.enabled:
            return
        self.root.update_idletasks()
        self.root.update()
        self.root.after(milliseconds)

    def display(self, matrix: list[list[int]], generation: int) -> None:
        if not self.enabled:
            return
        self.root.title(f"Generation: {generation:6d}")
        self.canvas.delete("all")

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                color = "black" if matrix[i][j] == 1 else "white"
                x0 = i * self.box_dim
                y0 = j * self.box_dim
                x1 = x0 + self.box_dim
                y1 = y0 + self.box_dim
                self.canvas.create_rectangle(
                    x0,
                    y0,
                    x1,
                    y1,
                    fill=color,
                    outline="black",
                )

        self.root.update_idletasks()
        self.root.update()
