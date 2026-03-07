from typing import Dict, List, Tuple, Optional

class Graph:
    """
    Represent a directed graph with edge weights.
    """
    def __init__(self, vertices: int):
        self.V = vertices  # Number of vertices
        self.graph = []    # List to store edges (u, v, w)

    def add_edge(self, u: int, v: int, w: float):
        """
        Add a directed edge from u to v with weight w.
        """
        self.graph.append([u, v, w])

def bellman_ford(graph: Graph, src: int) -> Tuple[Optional[Dict[int, float]], Optional[Dict[int, int]]]:
    """
    Bellman-Ford algorithm to find the shortest paths from src to all other vertices.
    Supports negative weight edges and detects negative cycles.

    Returns:
        A tuple (distances, predecessors) if no negative cycle is found.
        If a negative cycle is detected, returns (None, None).
    """
    V = graph.V
    dist = {i: float('inf') for i in range(V)}
    prev = {i: None for i in range(V)}
    dist[src] = 0

    # Relax edges V-1 times
    for _ in range(V - 1):
        for u, v, w in graph.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    # Check for negative weight cycles
    for u, v, w in graph.graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            # Negative cycle detected
            return None, None

    return dist, prev

def print_path(prev: Dict[int, int], target: int):
    """
    Helper function to print the path from src to target.
    """
    if target is None:
        return
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    print(" -> ".join(map(str, reversed(path))))

if __name__ == "__main__":
    # Example 1: No negative cycle
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    source = 0
    distances, predecessors = bellman_ford(g, source)

    if distances is not None:
        print(f"Vertex distances from source {source}:")
        for i in range(g.V):
            print(f"Vertex {i}: {distances[i]}")
            print(f"Path: ", end="")
            print_path(predecessors, i)
    else:
        print("Negative cycle detected!")

    print("\n" + "="*20 + "\n")

    # Example 2: Negative cycle
    g2 = Graph(3)
    g2.add_edge(0, 1, 1)
    g2.add_edge(1, 2, -1)
    g2.add_edge(2, 0, -1)

    distances, predecessors = bellman_ford(g2, 0)
    if distances is None:
        print("Successfully detected negative cycle in Example 2.")
    else:
        print("Failed to detect negative cycle in Example 2.")
