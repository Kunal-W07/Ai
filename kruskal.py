# Kruskal's Algorithm with Union-Find to find Minimum Spanning Tree (MST)

# Union-Find (Disjoint Set) class
class UnionFind:
    def __init__(self, nodes):
        # Initially, each node is its own parent
        self.parent = {x: x for x in nodes}

    def find(self, x):
        # Find the root of x with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Merge two sets
        self.parent[self.find(x)] = self.find(y)

# Kruskal's algorithm implementation
def kruskal(graph):
    # Create and sort all edges by weight
    edges = sorted((w, u, v) for u in graph for v, w in graph[u])
    uf = UnionFind(graph)  # Initialize Union-Find with all nodes
    mst, total = [], 0     # MST edge list and total weight

    # Process each edge in order of increasing weight
    for w, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            total += w
    return mst, total

# --------------------------- Input Section ---------------------------
graph = {}                                  # Graph dictionary
n = int(input("Enter number of edges: "))   # Number of edges

# Read edges from user input
for _ in range(n):
    u, v, w = input("Enter edge (u v weight): ").split()
    w = int(w)
    graph.setdefault(u, []).append((v, w))  # Add edge u -> v
    graph.setdefault(v, []).append((u, w))  # Add edge v -> u (undirected)

# -------------------------- Output Section ---------------------------
mst, cost = kruskal(graph)                  # Get MST and cost

print("\nKruskal's MST:")
for u, v, w in mst:
    print(f"{u} - {v}: {w}")
print(f"Total cost: {cost}")
