'''
# Mission 14 Summary
# Problem:
#   - Listing every code for "23" takes two nested loops, for "2345" four.
#     The number of loops = len(digits), which isn't known while writing
#     the code.
#
# Concept:
#   - Backtracking: recursion over CHOICES. Each call is one loop level: it
#     tries every option for the current slot and calls itself for the next
#     slot. The calls form a tree; each leaf is one complete answer.
#   - Same skeleton as Mission 8's DFS: the path so far flows DOWN as an
#     argument.
#
# How it works:
#   - LC 17: dfs(i, path). i = position in digits (where); digits[i] = the
#     digit; letters[digits[i]] = its letters (inside-out, one layer per
#     line). When i == len(digits), save path. Each letter → dfs(i + 1,
#     path + ch). A string path makes a new string, so nothing to undo.
#   - LC 216: a LIST path. choose (path.append(num)), recurse
#     (dfs(num + 1, total + num)), un-choose (path.pop()), so the next num
#     takes the same slot. Starting the next pick at num + 1 keeps each
#     combination increasing and listed once.
#   - Save path[:], a copy. res.append(path) saves the list itself, and
#     every later pop changes it (LC 216 would end with [[], [], []]).
#   - n = the target; num = the number being tried. Copy the def line and
#     write what moves under each argument.
#
# When to use it:
#   - "List every combination / arrangement / way to build something,"
#     built one slot at a time → backtracking.
#   - A target (sum = n) is an extra check at the end, not the signal.
'''


# LC 17 Letter Combinations of a Phone Number
# Given a string of digits 2-9, return every letter combination the number
# could spell, using the phone keypad below. Return [] for an empty string.
# Example: digits = "23"
#   → ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

def letter_combinations(digits):
    if not digits:
        return []
    res = []
    def dfs(i, path):                  # i = position in digits (WHERE); path = letters so far
        if i == len(digits):           # every digit has a letter
            res.append(path)           # a string: safe to save as-is
            return
        for ch in letters[digits[i]]:  # i → digits[i] (the digit) → its letters
            dfs(i + 1, path + ch)      # next digit, path one letter longer
    dfs(0, "")
    return res


# LC 216 Combination Sum III
# Find every combination of k different numbers from 1 to 9 that add up to n.
# Each combination appears once ([1, 2, 6] and [2, 1, 6] are the same).
# Example: k = 3, n = 9 → [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
# Example: k = 3, n = 7 → [[1, 2, 4]]

def combination_sum3(k, n):
    res = []
    path = []                             # numbers chosen so far
    def dfs(start, total):                # start = smallest number allowed next
        if len(path) == k:                # k numbers chosen
            if total == n:                # n = the TARGET
                res.append(path[:])       # save a COPY of the combination
            return
        for num in range(start, 10):      # num = the number being tried (start .. 9)
            path.append(num)              # choose
            dfs(num + 1, total + num)     # next pick bigger; total grows by num
            path.pop()                    # un-choose: free the slot for the next num
    dfs(1, 0)
    return res
