from task1 import create_graph
from collections import deque

# Рекурсивна реалізація DFS (пошуку в глибину)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# Реалізація BFS (пошуку в ширину)
def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])
    return visited

# Точка входу
if __name__ == "__main__":
    G = create_graph()
    start_node = 'A'

    print("DFS шлях з", start_node, ":", dfs(G, start_node))
    print("BFS шлях з", start_node, ":", bfs(G, start_node))