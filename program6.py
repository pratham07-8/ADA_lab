# 6. Construct a Graph class with kruskal_mst() -> List[Edge] and prim_mst() -> List[Edge]
# methods that process edge-weighted graph structures and return the MST edge set.

from dataclasses import dataclass
from typing import List


@dataclass
class Edge:
    u: int
    v: int
    weight: int


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append(Edge(u, v, weight))

    # ---------------- KRUSKAL'S ALGORITHM ----------------
    def kruskal_mst(self) -> List[Edge]:
        # Sort edges by increasing weight
        edges = sorted(self.edges, key=lambda edge: edge.weight)

        parent = list(range(self.vertices))
        rank = [0] * self.vertices

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        mst = []

        for edge in edges:
            if union(edge.u, edge.v):
                mst.append(edge)

                if len(mst) == self.vertices - 1:
                    break

        return mst

    # ---------------- PRIM'S ALGORITHM ----------------
    def prim_mst(self) -> List[Edge]:
        if self.vertices == 0:
            return []

        visited = [False] * self.vertices
        mst = []

        # Start from vertex 0
        visited[0] = True

        while len(mst) < self.vertices - 1:
            min_edge = None

            # Find minimum edge connecting
            # visited vertex to unvisited vertex
            for edge in self.edges:
                if visited[edge.u] and not visited[edge.v]:
                    if min_edge is None or edge.weight < min_edge.weight:
                        min_edge = edge

                elif visited[edge.v] and not visited[edge.u]:
                    if min_edge is None or edge.weight < min_edge.weight:
                        min_edge = edge

            if min_edge is None:
                break

            mst.append(min_edge)

            # Mark the new vertex as visited
            if visited[min_edge.u]:
                visited[min_edge.v] = True
            else:
                visited[min_edge.u] = True

        return mst


# ---------------- EXAMPLE ----------------

g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Kruskal MST:")
for edge in g.kruskal_mst():
    print(edge.u, "-", edge.v, ":", edge.weight)

print("\nPrim MST:")
for edge in g.prim_mst():
    print(edge.u, "-", edge.v, ":", edge.weight)