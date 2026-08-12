# #3. Implement findKthLargest(nums: List[int], k: int) -> int and findMinMax(nums:
# List[int]) -> Tuple[int, int] functions accepting an unsorted array, returning the -th element
# and min-max pair.

from typing import List, Tuple


def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    return nums[k - 1]


def findMinMax(nums: List[int]) -> Tuple[int, int]:
    return min(nums), max(nums)


# Example
nums = [3, 2, 1, 5, 6, 4]

print("Kth Largest:", findKthLargest(nums, 2))
print("Min-Max:", findMinMax(nums))