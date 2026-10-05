'''
Mission 3 Summary: Prefix Sum

Problem: Range-sum questions that jump around can't use a sliding window, and re-adding each range is O(n) per question.

Concept: Build a running total once (the odometer). Then any range is one subtraction.

 prefix = [0, 3, 4, 8, 9, 14, 23]      prefix[i] = reading at the START of day i
 sum of idx l..r = prefix[r + 1] − prefix[l]

Two ways you used it:

Build it: Highest Altitude: altitude = altitude + g, track the max.
Split a total: Pivot Index: right = total − left − nums[i], with left as a running total. Check first, then add.

When to use it: repeated sums over ranges, or anything comparing "everything before i" with "everything after i."
'''

# LC 1732: Find the Highest Altitude
# gain = [-5, 1, 5, 0, -7]
# altitudes: 0, -5, -4, 1, 1, -6   → answer: 1
def largest_altitude(gain):
    altitude = 0      # start at 0
    best = 0          # 0 counts: the start is a point too
    for g in gain:
        altitude = altitude + g
        best = max(best, altitude)
    return best

# LC 724: Find Pivot Index
def pivot_index(nums):
    total = sum(nums)
    left = 0
    for i in range(len(nums)):
        # 1. compute right
        right = total - left - nums[i]
        # 2. if left == right, return i
        if (left == right):
            return i
        # 3. add nums[i] to left
        left += nums[i]
    return -1