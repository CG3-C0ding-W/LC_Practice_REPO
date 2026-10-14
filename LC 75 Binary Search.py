'''
'''
# LC 374 Guess Number Higher or Lower.
# I pick a number from 1 to n. You guess. You can’t see my number; you can only call guess(num), which returns:
# -1 if your guess is too high (my number is lower)
# 1 if your guess is too low (my number is higher)
# 0 if your guess is right
# Return my number.
# Example: n = 10, pick = 7 → return 7.
def guess_number(n):
    lo, hi = 1, n                    # candidate NUMBERS (where)
    while lo <= hi:                  # while lo is at most hi
        mid = (lo + hi) // 2
        g = guess(mid)
        if g == 0:                   # right guess
            return mid               # the number, not n
        elif g == -1:                # guess too high: the pick is lower
            hi = mid - 1             # mid is ruled out, drop it and everything above
        else:                        # guess too low: the pick is higher
            lo = mid + 1             # mid is ruled out, drop it and everything below
