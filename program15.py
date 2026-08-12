# 15. Build a GraphBacktracker class featuring graph_coloring(m: int) -> List[int] and
# hamiltonian_cycle() -> List[int] methods returning vertex-color mappings and valid path
# cycles.

from typing import List


class GraphBacktracker:
    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.n = len(graph)

    # ---------------- GRAPH COLORING ----------------
    def graph_coloring(self, m: int) -> List[int]:
        color = [0] * self.n

        def is_safe(vertex, c):
            for i in range(self.n):
                if self.graph[vertex][i] == 1 and color[i] == c:
                    return False
            return True

        def backtrack(vertex):
            if vertex == self.n:
                return True

            for c in range(1, m + 1):
                if is_safe(vertex, c):
                    color[vertex] = c

                    if backtrack(vertex + 1):
                        return True

                    color[vertex] = 0

            return False

        if backtrack(0):
            return color

        return []


    # ---------------- HAMILTONIAN CYCLE ----------------
    def hamiltonian_cycle(self) -> List[int]:
        path = [-1] * self.n

        # Start from vertex 0
        path[0] = 0

        def is_safe(vertex, position):
            # Must be connected to previous vertex
            if self.graph[path[position - 1]][vertex] == 0:
                return False

            # Vertex must not already be in the path
            if vertex in path:
                return False

            return True

        def backtrack(position):
            # All vertices are included
            if position == self.n:
                # Check if last vertex connects to first
                return self.graph[path[-1]][path[0]] == 1

            for vertex in range(1, self.n):
                if is_safe(vertex, position):
                    path[position] = vertex

                    if backtrack(position + 1):
                        return True

                    path[position] = -1

            return False

        if backtrack(1):
            # Add starting vertex to show complete cycle
            return path + [path[0]]

        return []


# ---------------- EXAMPLE ----------------

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

g = GraphBacktracker(graph)

# Graph Coloring
m = 3
colors = g.graph_coloring(m)

print("Vertex Colors:", colors)

# Hamiltonian Cycle
cycle = g.hamiltonian_cycle()

print("Hamiltonian Cycle:", cycle)