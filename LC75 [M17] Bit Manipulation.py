'''
# Mission 17 Summary
# Problem:
#   - Find the one number without a pair, with no extra memory (no set or
#     dict, unlike Mission 4). Count the 1 bits of every number 0..n without
#     converting each one to a string.
#
# Concept:
#   - Numbers are stored as bits; each column is worth double the one to
#     its right (4 2 1: 101 = 4 + 1 = 5). Add only columns holding a 1.
#   - Bitwise operators work one column at a time:
#       a ^ b    XOR: 1 where the bits DIFFER (not "power"; that's **)
#       a & b    AND: 1 only where both are 1
#       x >> 1   drop the last bit → a smaller number (x // 2)
#       x & 1    the last bit itself → 0 or 1 (1 if odd)
#   - XOR facts: a ^ a = 0 (a pair vanishes completely), a ^ 0 = a, and the
#     order doesn't matter.
#
# How it works:
#   - Single Number (LC 136): result = 0; XOR in every number. Pairs cancel
#     to 0; the single one is left. Return the NUMBER.
#   - Counting Bits (LC 338): dropping the last bit leaves a number already
#     counted: dp[i] = dp[i >> 1] + (i & 1).
#       row 7: 2 + 1 → dp[3] + (7 & 1) → dp[i >> 1] + (i & 1)
#     dp[i >> 1] is a COUNT; i >> 1 is a number. Brackets around (i & 1):
#     + runs before >> and &. Return the whole list, dp.
#   - Read a last bit with an arrow under it before writing it.
#
# When to use it:
#   - The problem is about the bits of numbers (counting 1s, last bit,
#     flipping) → & 1, >> 1, often with DP.
#   - Things come in pairs that should cancel, with no extra memory → XOR
#     everything (Single Number, Missing Number).
'''

# LC 136 Single Number
# Every number in nums appears twice except one. Return that one, using
# no extra memory.
# Example: nums = [4, 1, 2, 1, 2] → 4
# Example: nums = [7, 3, 7] → 3

def single_number(nums):
    result = 0                 # a ^ 0 = a
    for x in nums:
        result ^= x            # same as result = result ^ x; pairs cancel to 0
    return result              # the NUMBER left over, not its index


# LC 338 Counting Bits
# Given n, return a list ans of length n + 1 where ans[i] is the number of
# 1 bits in i.
# Example: n = 2 → [0, 1, 1]
# Example: n = 5 → [0, 1, 1, 2, 1, 2]

def count_bits(n):
    dp = [0] * (n + 1)                    # dp[i] = number of 1s in i; dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)      # 1s in i without its last bit, plus that bit
    return dp                             # the whole list, length n + 1
