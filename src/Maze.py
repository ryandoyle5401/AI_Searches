import json

class Maze:
    def __init__(self, grid):
        """
            Note: this is the structure of the adjacency list:
            ((row, col), edge_weight)
        """
        self.grid = grid  # Grid is the 2D array representing the maze
        self.adj_list = self.build_adjacency_list()  # Converts 2D array to adjacency list

    def get_neighbors(self, row, col):
        # Different directions to move to in the maze
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
        neighbors = []  # Nodes are represented by coordinates of available paths. 0 = path, 1 = wall
        for dr, dc in directions:
            r, c = row + dr, col + dc
            # Check if the updated row and column are in the bounds of the array and that the cell is an open path
            if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] == 0:
                # Add cell if it is in bounds and contains a 0. Give it an edge weight of 1
                neighbors.append(((r,c), 1))
        return neighbors

    def build_adjacency_list(self):
        """
            Iterates through the 2D array and converts it to an adjacency list.
        """
        adj_list = {}
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 0:
                    adj_list[(r,c)] = self.get_neighbors(r,c)
        return adj_list

    def print_adjacency_list(self):
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")

def load_maze(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data["maze"]
