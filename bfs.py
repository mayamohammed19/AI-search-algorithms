from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        current_node = queue.popleft()

        if current_node == goal:
            # If goal is found, you can reconstruct the path
            path = [current_node]
            while current_node != start:
                current_node = parents[current_node]
                path.insert(0, current_node)
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current_node
                queue.append(neighbor)

    return None  # No path found

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start_node = 'A'
goal_node = 'H'

parents = {}  # To store the parent of each node in the traversal

path = bfs(graph, start_node, goal_node)

if path:
    print("Path found:", path)
else:
    print("No path found.")
