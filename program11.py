# 11. Implement lengthOfLIS(nums: List[int]) -> int function accepting an integer array and
# returning the length of the longest strictly increasing subsequence.

from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)

    # dp[i] = length of LIS ending at index i
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]

print("Length of LIS:", lengthOfLIS(nums))