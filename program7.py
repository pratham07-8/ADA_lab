# 7. Build a ShortestPath class containing dijkstra(src: int) -> List[int] and
# bellman_ford(src: int) -> List[int] methods taking a starting node and returning distance
# arrays (or error status for negative cycles).

from typing import List
import heapq


class ShortestPath:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append((u, v, weight))

    # ---------------- DIJKSTRA ----------------
    def dijkstra(self, src: int) -> List[int]:
        INF = float('inf')

        # Create adjacency list
        graph = [[] for _ in range(self.vertices)]

        for u, v, weight in self.edges:
            if weight < 0:
                raise ValueError("Dijkstra cannot handle negative weights")

            graph[u].append((v, weight))

        distance = [INF] * self.vertices
        distance[src] = 0

        # Priority queue: (distance, vertex)
        pq = [(0, src)]

        while pq:
            current_distance, u = heapq.heappop(pq)

            if current_distance > distance[u]:
                continue

            for v, weight in graph[u]:
                new_distance = current_distance + weight

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    heapq.heappush(pq, (new_distance, v))

        return distance

    # ---------------- BELLMAN-FORD ----------------
    def bellman_ford(self, src: int) -> List[int]:
        INF = float('inf')

        distance = [INF] * self.vertices
        distance[src] = 0

        # Relax all edges V-1 times
        for _ in range(self.vertices - 1):
            updated = False

            for u, v, weight in self.edges:
                if distance[u] != INF and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    updated = True

            # Stop early if no update occurred
            if not updated:
                break

        # Check for negative weight cycle
        for u, v, weight in self.edges:
            if distance[u] != INF and distance[u] + weight < distance[v]:
                raise ValueError("Negative weight cycle detected")

        return distance


# ---------------- EXAMPLE ----------------

g = ShortestPath(5)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)

print("Dijkstra:")
print(g.dijkstra(0))

print("\nBellman-Ford:")
print(g.bellman_ford(0))