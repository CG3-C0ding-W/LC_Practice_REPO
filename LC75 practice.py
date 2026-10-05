'''
Mission 1 Summary: Two Pointers

Problem: Checking every pair is O(n²).

Concept: Two pointers that each comparison moves, so every step eliminates something for good. One pass, O(n).

Two flavors:

Opposite ends (pair sum, k-sum, container)
 L →              ← R
 a comparison proves one end can't help → drop it

Same direction (subsequence, move zeroes)
 i →   (in s)
 j →   (in t)
 pointers only advance, never reset

When to use it:

Pairs in a sorted (or sortable) array, where a comparison says which end is useless → opposite ends.
Walking two sequences, or reading and writing in one array, in order → same direction.
'''

# Container with max_area
def max_area(height):
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        # 1. compute area for this pair
        max_area = min(height[l], height[r]) * (r-l)
        # 2. update best
        best = max(best, max_area)
        # 3. move the shorter line inward
        if(height[l] < height[r]):
            l += 1
        else: 
            r -= 1
    return best

# LC 392 Q: Is Subsequence s hidden inside subsequence t?
# s = "ace", t = "abcde" Correct answer: True
def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        # compare, then move the right pointer(s)
        if(s[i] == t[j]):
            i += 1
            j += 1
        else:
            j += 1
    return i == len(s)
            
            
