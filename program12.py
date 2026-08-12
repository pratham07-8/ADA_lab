# 12. Implement floyd_warshall(graph: List[List[int]]) -> List[List[int]] and
# optimal_bst(keys: List[int], freq: List[int]) -> int accepting distance/frequency
# matrices and returning shortest path or cost matrices.

from typing import List


def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)

    # Make a copy so the original graph is not modified
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return dist


def optimal_bst(keys: List[int], freq: List[int]) -> int:
    n = len(keys)

    if n == 0:
        return 0

    # dp[i][j] = minimum cost of optimal BST
    # containing keys from i to j
    dp = [[0] * n for _ in range(n)]

    # Prefix sums for frequency calculation
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + freq[i]

    def frequency_sum(i, j):
        return prefix[j + 1] - prefix[i]

    # One key
    for i in range(n):
        dp[i][i] = freq[i]

    # Consider chains of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            dp[i][j] = float('inf')

            total_freq = frequency_sum(i, j)

            # Try every key as root
            for r in range(i, j + 1):

                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0

                cost = left + right + total_freq

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# ---------------- EXAMPLE ----------------

# Floyd-Warshall
INF = float('inf')

graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

print("Floyd-Warshall Shortest Paths:")

result = floyd_warshall(graph)

for row in result:
    print(row)


# Optimal BST
keys = [10, 12, 20]
freq = [34, 8, 50]

print("\nOptimal BST Cost:")
print(optimal_bst(keys, freq))