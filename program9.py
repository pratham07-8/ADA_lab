# 9. Implement knapsack_01(weights: List[int], values: List[int], capacity: int) -> int
# utilizing 2D/1D DP methods that accept item properties and return maximum value.

from typing import List


def knapsack_01_2d(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)

    # dp[i][w] = maximum value using first i items
    # with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for w in range(capacity + 1):

            # Don't take the item
            dp[i][w] = dp[i - 1][w]

            # Take the item if it fits
            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

    return dp[n][capacity]


# Example
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Maximum Value:", knapsack_01_2d(weights, values, capacity))