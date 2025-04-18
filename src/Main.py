import time

class Maze:
    def __init__(self, grid):
        """
        Constructs a maze as a 2D array and as an adjacency list.
        2D array is used to visualize the maze, adjacency list is used to perform graph search operations over the maze.
        """
        self.grid = grid  # Stores 2D array
        self.adj_list = self.build_adjacency_list()  # Creates and stores adjacency list of 2D array

    def get_neighbors(self, row, col):
        """
        Identifies all neighbor nodes of a particular node in all directions (up, down, left, right)
        """
        # Different directions to move to in the maze
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
        neighbors = []  # Nodes are represented by coordinates of available paths. 0 = path, 1 = wall
        for dr, dc in directions:
            r, c = row + dr, col + dc  # Go in all different directions (up, down, left, right)
            # Check if the updated row and column are in the bounds of the array and that the cell is an open path
            if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] == 0:
                # Add cell if it is in bounds and contains a 0. Give all nodes an edge weight of 1
                neighbors.append(((r,c), 1))
        return neighbors  # Returns a list of all neighbors for a particular node

    def build_adjacency_list(self):
        """
        Convert the 2D array to an adjacency list

        Returns:
            An adjacency list created from the 2D array maze
        """
        adj_list = {}
        # Iterate through the 2D array to create adjacency list
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 0:  # If value of cell is 0, that is an open path
                    adj_list[(r,c)] = self.get_neighbors(r,c)  # Create a key in the adj_list. Have the value of the key be all neighbor nodes
        return adj_list

    def print_adjacency_list(self):
        """
        Prints all nodes and their neighbors
        """
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")  # Prints the node and all its neighbors



def main():
    # Note: 0 = path, 1 = wall
    maze = [
        [0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0]
    ]
    maze1 = Maze(maze)
    graph = maze1.adj_list  # Adjacency list of given 2D array
    start_node = (0,0)  # Top-left corner of maze
    end_node = (3,8)  # Bottom-right corner of maze

    # Run a loop so the user can choose which search algorithms to use
    while True:
        print("Welcome to Maze Solver! Enter the value associated with the search algorithm to perform that search on the maze. Enter -1 to exit: ")
        print("1. Breadth-first Search")
        print("2. Depth-first Search")
        print("3. Uniform-cost Search")
        print("4. A* Search")
        user_input = input("Enter your value: ")
        if int(user_input) == 1:
            # Start timer
            start = time.time()
            run_bfs(start_node, end_node, graph)
            # Stop timer
            stop = time.time()
            # Calculate elapsed time
            elapsed = calculate_elapsed_time(start, stop)
            print(f"Solved maze in {elapsed} time!")
        elif int(user_input) == 2:
            # Start timer
            start = time.time()
            run_dfs(start_node, end_node, graph)
            # Stop timer
            stop = time.time()
            elapsed = calculate_elapsed_time(start, stop)
            print(f"Solved maze in {elapsed} time!")
        elif int(user_input) == -1:
            break


def run_bfs(start, end, graph):
    """
    Runs Breadth-first search over the maze to find the exit.

    Args:
        start (Tuple of ints): The starting node to begin BFS on
        end (Tuple of ints): The ending node to stop BFS on
        graph (Dictionary): The adjacency list
    """
    q = [start]  # Input start node into queue
    came_from = {start: None}  # A dict to keep track of where each node came from
    visited = set()  # Create a visited set
    nodes_expanded = 0  # Keeps track of number of nodes expanded

    while q:
        current = q.pop(0)  # Pop node off queue
        nodes_expanded += 1
        if current == end:  # Check if current node is end of maze
            node = current
            solution_path = [end]
            while came_from[node] is not None:  # Reconstruct path from end node to start node
                solution_path.append(came_from[node])  # Append the parent node
                node = came_from[node]  # Change node to be the parent of the previous node
            solution_path.reverse()  # Reverse solution_path to get path in correct order
            print("solution path", solution_path)

        if current not in visited:
            for neighbor in graph[current]:  # Iterate through all neighbors of current node
                q.append(neighbor[0])  # We use neighbor[0] to access the individual node, not the node and edge weight
                if neighbor[0] not in visited:  # Used to prevent updating came_from dict incorrectly
                    came_from[neighbor[0]] = current  # Track the parent node for all neighbors
        visited.add(current)  # Add current node to visited set
    print("Nodes Expanded:", nodes_expanded)

def run_dfs(start, end, graph):
    """
    Runs Depth-first search over the maze to find the exit.

    Args:
        start (Tuple of ints): The starting node to begin BFS on
        end (Tuple of ints): The ending node to stop BFS on
        graph (Dictionary): The adjacency list
    """
    q = [start]  # Input start node into stack
    came_from = {start: None}  # A dict to keep track of where each node came from
    visited = set()  # Create a visited set
    nodes_expanded = 0  # Keeps track of number of nodes expanded

    while q:
        current = q.pop()  # Pop node off stack
        nodes_expanded += 1
        if current == end:  # Check if current node is end of maze
            node = current
            solution_path = [end]
            while came_from[node] is not None:  # Reconstruct path from end node to start node
                solution_path.append(came_from[node])  # Append the parent node
                node = came_from[node]  # Change node to be the parent of the previous node
            solution_path.reverse()  # Reverse solution_path to get path in correct order
            print("solution path", solution_path)

        if current not in visited:
            for neighbor in graph[current]:  # Iterate through all neighbors of current node
                q.append(neighbor[0])  # We use neighbor[0] to access the individual node, not the node and edge weight
                if neighbor[0] not in visited:  # Used to prevent updating came_from dict incorrectly
                    came_from[neighbor[0]] = current  # Track the parent node for all neighbors
        visited.add(current)  # Add current node to visited set
    print("Nodes Expanded:", nodes_expanded)

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

if __name__ == '__main__':
    main()
