
import tkinter as tk
from tkinter import PhotoImage, Label, Toplevel
from Main import Maze, run_bfs, run_dfs, run_ucs, run_a_star, calculate_elapsed_time
import time
import random

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Maze Solver")

        self.cell_size = 40
        self.rows = 4
        self.cols = 9

        # Maze and state
        self.grid = []
        self.maze = None
        self.graph = None
        self.start_node = (0, 0)
        self.end_node = (3, 8)

        # UI elements
        self.canvas = tk.Canvas(self.root, width=self.cols * self.cell_size, height=self.rows * self.cell_size, bg="#ececec", bd=0, highlightthickness=0)
        self.canvas.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        tk.Button(self.buttons_frame, text="Breadth-First Search", command=lambda: self.animate(run_bfs, "BFS")).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Depth-First Search", command=lambda: self.animate(run_dfs, "DFS")).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Uniform Cost Search", command=lambda: self.animate(run_ucs, "UCS")).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="A* Search", command=lambda: self.animate(run_a_star, "A*")).pack(side=tk.LEFT, padx=5)

        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        tk.Button(control_frame, text="🔁 Reset", command=self.reset_maze).pack(side=tk.LEFT, padx=10)
        tk.Button(control_frame, text="🎲 Random Maze", command=self.generate_random_maze).pack(side=tk.LEFT, padx=10)
        tk.Button(control_frame, text="🧪 Compare All", command=self.compare_all).pack(side=tk.LEFT, padx=10)

        self.status_label = Label(self.root, text="", font=("Helvetica", 12), bg="#f0f0f0", pady=5)
        self.status_label.pack()

        self.robot_icon = PhotoImage(file="icons/start_heart.png").subsample(2, 2)  # placeholder for robot
        self.generate_default_maze()

    def generate_default_maze(self):
        self.grid = [
            [0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0]
        ]
        self.rebuild_graph()

    def rebuild_graph(self):
        self.maze = Maze(self.grid)
        self.graph = self.maze.adj_list
        self.start_node = (0, 0)
        self.end_node = (3, 8)
        self.draw_maze()

    def draw_maze(self):
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                fill_color = "#ffffff" if self.grid[r][c] == 0 else "#1e1e1e"
                self.canvas.create_rectangle(x1+2, y1+2, x2-2, y2-2, fill=fill_color, outline="#d3d3d3", width=2)

        self.place_label(self.start_node, "START")
        self.place_label(self.end_node, "END")

    def place_label(self, pos, text):
        x, y = pos[1] * self.cell_size, pos[0] * self.cell_size
        self.canvas.create_text(
            x + self.cell_size // 2,
            y + self.cell_size // 2,
            text=text,
            font=("Arial", 10, "bold"),
            fill="red" if text == "START" else "magenta"
        )

    def animate(self, search_function, name):
        self.draw_maze()
        start = time.time()
        came_from, path, visited = search_function(self.start_node, self.end_node, self.graph)
        end = time.time()
        elapsed = calculate_elapsed_time(start, end)
        visited_count = len(set(visited))
        self.status_label.config(text=f"{name} completed in {elapsed:.4f} seconds. Path length: {len(path)} | Visited: {visited_count}")
        self.root.after(500, lambda: self.animate_path(path))

    def animate_path(self, path):
        for i, node in enumerate(path):
            self.root.after(i * 300, lambda n=node: self.place_robot(n))

    def place_robot(self, pos):
        x, y = pos[1] * self.cell_size, pos[0] * self.cell_size
        self.canvas.create_image(
            x + self.cell_size // 2,
            y + self.cell_size // 2,
            image=self.robot_icon,
            anchor=tk.CENTER
        )

    def reset_maze(self):
        self.rebuild_graph()
        self.status_label.config(text="")

    def generate_random_maze(self):
        self.grid = [[0 if random.random() > 0.3 else 1 for _ in range(self.cols)] for _ in range(self.rows)]
        self.grid[0][0] = 0
        self.grid[3][8] = 0
        self.rebuild_graph()

    def compare_all(self):
        compare_win = Toplevel(self.root)
        compare_win.title("🧪 Side-by-Side Comparison")

        methods = [("BFS", run_bfs), ("DFS", run_dfs), ("UCS", run_ucs), ("A*", run_a_star)]

        for i, (name, func) in enumerate(methods):
            canvas = tk.Canvas(compare_win, width=self.cols * 25, height=self.rows * 25, bg="white")
            canvas.grid(row=0, column=i)
            came_from, path, visited = func(self.start_node, self.end_node, self.graph)
            for r in range(self.rows):
                for c in range(self.cols):
                    x1, y1 = c*25, r*25
                    x2, y2 = x1+25, y1+25
                    color = "#fff" if self.grid[r][c] == 0 else "#000"
                    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
            for node in visited:
                r, c = node
                canvas.create_rectangle(c*25+5, r*25+5, c*25+20, r*25+20, fill="green", outline="")
            for node in path:
                r, c = node
                canvas.create_rectangle(c*25+8, r*25+8, c*25+17, r*25+17, fill="blue", outline="")
            canvas.create_text(5, 5, text=name, anchor="nw", font=("Arial", 10, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()
