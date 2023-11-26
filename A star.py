import heapq

class Node:
    def __init__(self, position, parent=None, cost=0, heuristic=0):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def calculate_heuristic(current, goal):
    # Euclidean distance is a common choice for the heuristic
    return ((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2) ** 0.5

def get_neighbors(current, grid):
    neighbors = []
    row, col = current

    # Define possible movements: up, down, left, right
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in movements:
        new_row, new_col = row + move[0], col + move[1]

        # Check if the new position is within the grid boundaries
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != 1:
            neighbors.append((new_row, new_col))

    return neighbors

def astar(grid, start, goal):
    start_node = Node(start, None, 0, calculate_heuristic(start, goal))
    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        for neighbor_pos in get_neighbors(current_node.position, grid):
            if neighbor_pos in closed_set:
                continue

            cost = current_node.cost + 1
            neighbor_node = Node(neighbor_pos, current_node, cost, calculate_heuristic(neighbor_pos, goal))

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)

    return None  # No path found

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start_position = (0, 0)
goal_position = (4, 4)

path = astar(grid, start_position, goal_position)

if path:
    print("Path found:", path)
else:
    print("No path found.")
