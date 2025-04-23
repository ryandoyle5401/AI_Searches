import time
import heapq

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
        print("\nWelcome to Maze Solver! Choose an algorithm (-1 to exit):")
        print("1. Breadth-first Search")
        print("2. Depth-first Search")
        print("3. Uniform-cost Search")
        print("4. A* Search")
        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_input == -1:
            # Exit condition
            print("Exiting Maze Solver.")
            break

        elif user_input in [1, 2, 3, 4]:
            start_time = time.time()
            if user_input == 1:
                run_bfs(start_node, end_node, graph)
            elif user_input == 2:
                run_dfs(start_node, end_node, graph)
            elif user_input == 3:
                run_UCS(start_node, end_node, graph)
            elif user_input == 4:
                run_A_star(start_node, end_node, graph)
            end_time = time.time()
            print(f"Solved maze in {calculate_elapsed_time(start_time, end_time)} seconds!")
        else:
            print("Invalid choice. Try again.")


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

# Uniform-Cost Search (UCS)
def run_UCS(start, end, graph):
    """
    Implements Uniform-cost Search to find the shortest path from start to end.

    Args:
        start: starting node (tuple)
        end: destination node (tuple)
        graph: adjacency list representing the maze

    UCS expands the node with the lowest path cost at each step.
    """
    frontier = [(0, start)]  # Priority queue with (cost, node)
    came_from = {start: None}  # Tracks the path
    cost_so_far = {start: 0}  # Stores cost to reach each node
    nodes_expanded = 0

    while frontier:
        current_cost, current = heapq.heappop(frontier)  # Get node with lowest cost
        nodes_expanded += 1

        if current == end:
            path = reconstruct_path(came_from, start, end)
            print("Solution path", path)
            break

        for neighbor, weight in graph[current]:
            new_cost = current_cost + weight  # Calculate cost to neighbor
            # If it's a new node or cheaper path found, update records
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor))  # Add neighbor to frontier
                came_from[neighbor] = current  # Track path

    print("Nodes Expanded:", nodes_expanded)

def heuristic(a, b):
    """Manhattan distance heuristic"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* Search
def run_A_star(start, end, graph):
    """
    Implements A* Search algorithm using Manhattan distance as heuristic.

    Args:
        start: starting node (tuple)
        end: destination node (tuple)
        graph: adjacency list representing the maze

    A* = UCS + heuristic to prioritize promising paths.
    """
    # Priority queue holds (f_score, cost_so_far, node)
    frontier = [(heuristic(start, end), 0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    nodes_expanded = 0

    while frontier:
        _, current_cost, current = heapq.heappop(frontier)  # Node with lowest f_score
        nodes_expanded += 1

        if current == end:
            path = reconstruct_path(came_from, start, end)
            print("Solution path", path)
            break

        for neighbor, weight in graph[current]:
            new_cost = current_cost + weight
            # Update path if neighbor is unvisited or a better path is found
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, end)  # f = g + h
                heapq.heappush(frontier, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    print("Nodes Expanded:", nodes_expanded)

def reconstruct_path(came_from, start, end):
    node = end
    path = [end]
    while node != start:
        node = came_from[node]
        path.append(node)
    path.reverse()
    return path

def calculate_elapsed_time(start, stop):
    return stop - start

if __name__ == '__main__':
    main()
