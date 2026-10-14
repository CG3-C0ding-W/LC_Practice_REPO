'''
# Mission 16 Summary
# Problem:
#   - Some answers depend on TWO positions at once: a row and a column, or
#     how far into each of two strings. A 1D dp line can't hold that.
#
# Concept:
#   - 2D DP: dp[r][c] (or dp[i][j]) holds the answer for that pair of
#     positions. Fill top to bottom, left to right, so the cells you read
#     (up, left, diagonal) are already filled.
#   - Build it with dp = [[0] * cols for _ in range(rows)], never
#     [[0] * cols] * rows (every row would be the SAME list, like
#     res.append(path) in Mission 14).
#   - Sizes (m, n, len(...)) go in range(...); positions (r, c, i, j) go
#     inside [ ]. Tag each before using it as an index.
#
# How it works:
#   - Unique Paths (LC 62): dp[r][c] = number of routes to (r, c).
#     The last move came from above or the left:
#     dp[r][c] = dp[r - 1][c] + dp[r][c - 1]. First row and column = 1.
#     m rows → positions 0..m-1: return dp[m - 1][n - 1].
#   - Longest Common Subsequence (LC 1143): dp[i][j] = answer for the first
#     i letters of text1 and the first j of text2. Extra row/column of 0s
#     for "0 letters," so dp has (m + 1) × (n + 1) slots: return dp[m][n].
#     Compare the last LETTERS, text1[i - 1] == text2[j - 1] (not i == j):
#       same      → dp[i - 1][j - 1] + 1          (diagonal + 1)
#       different → max(dp[i - 1][j], dp[i][j - 1])   (up, left)
#     Read the "same?" column first, then pick the rule.
#   - After writing a line, check every loop name letter for letter
#     against its for line (i, not I).
#
# When to use it:
#   - Routes / cheapest path on a grid moving right and down → 2D DP over
#     cells.
#   - Two strings or sequences compared piece by piece (common
#     subsequence, edits) → 2D DP over (letters of one, letters of the other).
'''

# LC 62 Unique Paths
# A robot starts at the top-left of an m × n grid (m rows, n columns) and
# moves only right or down. Return the number of different routes to the
# bottom-right cell.
# Example: m = 3, n = 3 → 6
# Example: m = 3, n = 7 → 28

def unique_paths(m, n):                      # m, n = SIZES (rows, columns)
    dp = [[1] * n for _ in range(m)]         # first row and column stay 1
    for r in range(1, m):                    # r, c = POSITIONS
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]   # above + left
    return dp[m - 1][n - 1]                  # bottom-right: rows 0..m-1, columns 0..n-1


# LC 1143 Longest Common Subsequence
# A subsequence keeps some letters of a string in their original order,
# possibly skipping some ("ace" is a subsequence of "abcde"). Return the
# length of the longest subsequence text1 and text2 share (0 if none).
# Example: text1 = "abcde", text2 = "ace" → 3
# Example: text1 = "abc", text2 = "bxc" → 2

def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)                  # SIZES
    dp = [[0] * (n + 1) for _ in range(m + 1)]     # row 0, column 0: empty string → 0
    for i in range(1, m + 1):                      # i, j = how many letters
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:       # the last LETTERS are the same
                dp[i][j] = dp[i - 1][j - 1] + 1    # diagonal + 1
            else:
                dp[i][j] = max(dp[i - 1][j],       # up: drop text1's last letter
                               dp[i][j - 1])       # left: drop text2's last letter
    return dp[m][n]                                # all of both strings
