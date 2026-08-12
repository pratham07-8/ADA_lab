#10. Implement longestCommonSubsequence(text1: str, text2: str) -> int and
# minDistance(word1: str, word2: str) -> int functions accepting input strings and returning
# optimal length/edit operation counts.

from typing import Tuple


def longestCommonSubsequence(text1: str, text2: str) -> int:
    m = len(text1)
    n = len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def minDistance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],       # Insert
                    dp[i - 1][j],       # Delete
                    dp[i - 1][j - 1]    # Replace
                )

    return dp[m][n]


# Main program
text1 = input("Enter first string for LCS: ")
text2 = input("Enter second string for LCS: ")

print("LCS Length:", longestCommonSubsequence(text1, text2))


word1 = input("\nEnter first word for Edit Distance: ")
word2 = input("Enter second word for Edit Distance: ")

print("Minimum Edit Distance:", minDistance(word1, word2))