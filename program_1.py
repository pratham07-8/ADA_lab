from typing import List

# 1. Binary Search
def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# 2. Power Function
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0

    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0

    while n > 0:
        if n % 2 == 1:
            result *= x

        x *= x
        n //= 2

    return result


# Main program
nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

index = search(nums, target)
print("Target index:", index)

x = float(input("\nEnter base x: "))
n = int(input("Enter exponent n: "))

result = myPow(x, n)
print("Power:", result)