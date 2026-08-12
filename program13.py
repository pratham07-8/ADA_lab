# 13. Create a TSPSolver class with solve_tsp(dist_matrix: List[List[int]]) -> int taking an
# adjacency matrix and returning the minimum tour cost.

from typing import List


class TSPSolver:

    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:
        n = len(dist_matrix)

        if n == 0:
            return 0

        # dp[mask][i] = minimum cost to visit
        # all cities in mask and end at city i
        INF = float('inf')

        dp = [[INF] * n for _ in range(1 << n)]

        # Start from city 0
        dp[1][0] = 0

        # Process every possible set of visited cities
        for mask in range(1 << n):
            for u in range(n):

                if dp[mask][u] == INF:
                    continue

                # Try visiting an unvisited city
                for v in range(n):

                    if mask & (1 << v) == 0:

                        new_mask = mask | (1 << v)

                        new_cost = dp[mask][u] + dist_matrix[u][v]

                        dp[new_mask][v] = min(
                            dp[new_mask][v],
                            new_cost
                        )

        # All cities visited
        full_mask = (1 << n) - 1

        # Return to starting city (0)
        answer = INF

        for i in range(1, n):
            answer = min(
                answer,
                dp[full_mask][i] + dist_matrix[i][0]
            )

        return answer


# ---------------- EXAMPLE ----------------

dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solver = TSPSolver()

print("Minimum TSP Tour Cost:",
      solver.solve_tsp(dist_matrix))