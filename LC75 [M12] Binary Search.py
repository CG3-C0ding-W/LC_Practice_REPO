'''
# Mission 12 Summary
# Problem:
#   - Finding a target by scanning checks every item: O(n). In a BST each
#     compare threw away a whole subtree; a sorted list or a range of numbers
#     has the same order but no arrows.
#
# Concept:
#   - Binary search: keep a range lo..hi of candidates that could still be
#     the answer. Check the middle, throw away the half the check rules out.
#     O(log n): 1,000,000 candidates → about 20 checks.
#   - lo, hi, mid are WHERE (indexes, guesses, speeds); nums[mid] is WHAT.
#
# How it works:
#   - Target search (LC 374): while lo <= hi (a 1-item range is still
#     checked). Found → return mid. Otherwise mid is ruled out:
#     too high → hi = mid - 1; too low → lo = mid + 1.
#     guess() returns -1 when YOUR guess (mid) is too high.
#   - First True (LC 875): the check flips once, F F F T T T.
#     True → hi = mid (mid might be the answer, keep it);
#     False → lo = mid + 1. while lo < hi; return lo, not mid
#     (mid still holds the last checked speed, which may be too slow).
#   - Koko's hours per pile round UP: math.ceil(p / mid).
#
# When to use it:
#   - A sorted list and a target → target search.
#   - "Smallest / first value that works," where everything bigger also
#     works (faster never hurts, later versions stay bad) → binary search
#     on the answer range, first-True template.
#   - Test: can mid itself be the answer after the check? No → mid ± 1.
#     Yes → hi = mid.
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

'''
LC 875 Koko Eating Bananas
Koko has piles of bananas, piles[i] bananas in pile i. She picks an eating speed k (bananas per hour). 
Each hour she chooses one pile and eats k bananas from it. If the pile has fewer than k, 
she eats them all and doesn’t touch another pile that hour.
Return the smallest speed k that lets her finish every pile within h hours.
Example: piles = [4, 9, 13], h = 7 → 5.
'''
import math

def min_eating_speed(piles, h):
    lo, hi = 1, max(piles)               # candidate SPEEDS (where)
    while lo < hi:                       # while more than one speed is left
        mid = (lo + hi) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / mid)  # this pile's hours, rounded UP
        if hours <= h:                   # the total hours are at most h
            hi = mid                     # mid finishes: keep it in the range
        else:
            lo = mid + 1                 # too slow: drop it and everything below
    return lo                            # the one speed left (not mid)
