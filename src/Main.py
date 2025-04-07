import time

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.adj_list = self.build_adjacency_list()

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
        adj_list = {}
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 0:
                    adj_list[(r,c)] = self.get_neighbors(r,c)
        return adj_list

    # I'm still working on this
    def print_stuff(self):
        for r in self.grid:
            print(r)

    def print_adjacency_list(self):
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")



def main():
    while True:
        print("Welcome to Maze Solver! Enter the value associated with the serach algorithm to perform that search on the maze. Enter -1 to exit: ")
        print("1. Breadth-first Search")
        print("2. Depth-first Search")
        print("3. Uniform-cost Search")
        print("4. A* Search")
        userInput = input("Enter your value: ")
        if int(userInput) == 1:
            # Start timer
            start = time.time()
            run_bfs()
            # Stop timer
            stop = time.time()
            # Calculate elapsed time
            elapsed = calculate_elapsed_time(start, stop)
            print(f"Solved maze in {elapsed} time!")
        elif int(userInput) == -1:
            break

    # Note: 0 = path, 1 = wall
    maze = [
        [0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0]
    ]
    maze1 = Maze(maze)
    # maze1.print_stuff()
    #maze1.print_adjacency_list()
    graph = maze1.adj_list
    #start_node = graph[(0,0)][0][0]
    start_node = (0,0)
    run_bfs(start_node, graph)
    print("------------------------------------------")
    run_dfs(start_node, graph)


# Note: placeholder code in this function
def run_bfs(start, graph):
    q = [start]  # Create a queue, add starting node to queue
    visited = set()

    while q:
        current = q.pop(0)  # Pop first element in queue
        if current not in visited:
            print(current)
            for neighbor in graph[current]:
                q.append(neighbor[0])
        visited.add(current)

# Note: placeholder code in this function
def run_dfs(start, graph):
    q = [start]  # Create a queue, add starting node to queue
    visited = set()

    while q:
        current = q.pop()  # Pop last element in stack
        if current not in visited:
            print(current)
            for neighbor in graph[current]:
                q.append(neighbor[0])
        visited.add(current)

# Note: placeholder code in this function
def run_UCS():
    print("running BFS")
    for i in range(300000):
        pass

# Note: placeholder code in this function
def run_A_star():
    print("running BFS")
    for i in range(400000):
        pass

def calculate_elapsed_time(start, stop):
    return stop - start

# Note: trad_bfs is traditional bfs where all nodes are explored. I want to modify bfs so that a single path from a start node and end node are displayed
def trad_bfs(start, graph):
    q = [start]  # Input start node into queue
    visited = set()  # Create a visited set

    while q:
        current = q.pop(0)  # Pop node off queue
        if current not in visited:
            for neighbor in graph[current]:
                q.append(neighbor[0])  # Note: modified this because the neighbors are a tuple (cell, weight). We want to access the cell, so we enter neighbor[0]
        visited.add(current)  # Add current node to visited set

# Note: mod_bfs is modified bfs where only a single path is explored. This single path should be the solution to the maze
def mod_bfs():
    pass

# Note: trad_dfs is traditional dfs where all nodes are explored. I want to modify dfs so that a single path from a start node and end node are displayed
def trad_dfs(start, graph):
    q = [start]  # Input start node into stack
    visited = set()  # Create a visited set

    while q:
        current = q.pop()  # Pop node off stack
        if current not in visited:
            for neighbor in graph[current]:
                q.append(neighbor[0])  # Note: modified this because the neighbors are a tuple (cell, weight). We want to access the cell, so we enter neighbor[0]
        visited.add(current)  # Add current node to visited set

# Note: mod_dfs is modified dfs where only a single path is explored. This single path should be the solution to the maze
def mod_dfs():
    pass

if __name__ == '__main__':
    main()
