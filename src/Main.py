import random
import heapq

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.adj_list = self.build_adjacency_list()

    @staticmethod
    def generate_random(rows, cols, wall_chance=0.3):
        while True:
            grid = [[0 if random.random() > wall_chance else 1 for _ in range(cols)] for _ in range(rows)]
            grid[0][0] = 0
            grid[rows - 1][cols - 1] = 0
            maze = Maze(grid)
            _, path, _ = run_bfs((0, 0), (rows - 1, cols - 1), maze.adj_list)
            if path:
                return maze

    def get_neighbors(self, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] == 0:
                neighbors.append(((r, c), 1))
        return neighbors

    def build_adjacency_list(self):
        adj_list = {}
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 0:
                    adj_list[(r, c)] = self.get_neighbors(r, c)
        return adj_list

def run_bfs(start, end, graph):
    q = [start]
    came_from = {start: None}
    visited = []

    while q:
        current = q.pop(0)
        visited.append(current)
        if current == end:
            break
        for neighbor, _ in graph.get(current, []):
            if neighbor not in came_from:
                came_from[neighbor] = current
                q.append(neighbor)

    path = reconstruct_path(came_from, end)
    return came_from, path, visited


def run_dfs(start, end, graph):
    q = [start]
    came_from = {start: None}
    visited = []

    while q:
        current = q.pop()
        visited.append(current)
        if current == end:
            break
        for neighbor, _ in graph.get(current, []):
            if neighbor not in came_from:
                came_from[neighbor] = current
                q.append(neighbor)

    path = reconstruct_path(came_from, end)
    return came_from, path, visited


def run_ucs(start, end, graph):
    pq = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited = []

    while pq:
        current_cost, current = heapq.heappop(pq)
        visited.append(current)
        if current == end:
            break
        for neighbor, weight in graph.get(current, []):
            new_cost = cost_so_far[current] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
                came_from[neighbor] = current

    path = reconstruct_path(came_from, end)
    return came_from, path, visited


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def run_a_star(start, end, graph):
    pq = [(0 + heuristic(start, end), 0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited = []

    while pq:
        _, current_cost, current = heapq.heappop(pq)
        visited.append(current)
        if current == end:
            break
        for neighbor, weight in graph.get(current, []):
            new_cost = cost_so_far[current] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, end)
                heapq.heappush(pq, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    path = reconstruct_path(came_from, end)
    return came_from, path, visited


def reconstruct_path(came_from, end):
    if end not in came_from:
        return []
    path = [end]
    while came_from[path[-1]] is not None:
        path.append(came_from[path[-1]])
    path.reverse()
    return path


def calculate_elapsed_time(start, stop):
    return stop - start
