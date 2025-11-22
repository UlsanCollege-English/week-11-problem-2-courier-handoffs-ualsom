# hw02/main.py
from collections import deque

def bfs_path(graph, s, t):
    """Return a shortest path (fewest edges) from s to t as a list of nodes.
    If s == t, return [s]. If s or t not in graph, return None.
    """
    if s not in graph or t not in graph:
        return None
    if s == t:
        return [s]

    visited = set()
    parent = {}
    queue = deque([s])
    visited.add(s)

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
                if neighbor == t:
                    # reconstruct path
                    path = [t]
                    while path[-1] != s:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path
    return None
