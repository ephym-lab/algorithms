from typing import List, Tuple

class DisjointSetUnion:
    """
    Disjoint Set Union (DSU) or Union-Find data structure.
    Used for detecting cycles in a graph and managing connected components.
    """
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        """
        Find the representative of the set containing element i,
        with path compression.
        """
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        """
        Union the sets containing elements i and j,
        using union by rank. Returns True if a union occurred,
        False if they were already in the same set.
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

def kruskal_algorithm(vertices: int, edges: List[Tuple[int, int, float]]) -> List[Tuple[int, int, float]]:
    """
    Kruskal's algorithm for finding the Minimum Spanning Tree (MST).
    
    Args:
        vertices: Number of vertices in the graph.
        edges: A list of tuples (u, v, weight) representing edges.
        
    Returns:
        A list of tuples (u, v, weight) representing the edges in the MST.
    """
    # 1. Sort edges based on their weight
    sorted_edges = sorted(edges, key=lambda item: item[2])
    
    dsu = DisjointSetUnion(vertices)
    mst = []
    
    for u, v, weight in sorted_edges:
        # 2. If u and v are not in the same component, add to MST
        if dsu.union(u, v):
            mst.append((u, v, weight))
            
        # 3. Stop if we have V-1 edges (optimization)
        if len(mst) == vertices - 1:
            break
            
    return mst

if __name__ == "__main__":
    # Example Graph
    # Vertices are 0, 1, 2, 3
    num_vertices = 4
    # Edges: (u, v, weight)
    graph_edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    mst_edges = kruskal_algorithm(num_vertices, graph_edges)
    
    print("Edges in the Minimum Spanning Tree:")
    total_weight = 0
    for u, v, weight in mst_edges:
        print(f"{u} -- {v} == {weight}")
        total_weight += weight
        
    print(f"\nTotal weight of Minimum Spanning Tree: {total_weight}")
