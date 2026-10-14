# Mission 19 Summary
# Problem:
#   - Given [start, end] ranges, find the fewest to remove so none overlap,
#     or the fewest points that hit them all. Checking every pair is O(n²).
#
# Concept:
#   - Sort by END, then walk once, keeping ONE boundary from the past
#     (prev_end, or where the last arrow was shot).
#   - Greedy: the interval that ends earliest leaves the most room for the
#     rest. Sorting by start would keep X [1, 10] and lose Y and Z.
#   - intervals.sort(key=lambda iv: iv[1]) sorts by end.
#   - Unpack with start, end = iv (arrows straight down) before comparing.
#
# How it works:
#   - Non-overlapping (LC 435): if prev_end > start (starts before the last
#     kept one ends) → removed += 1 (a COUNT); else keep it: prev_end = end.
#     Touching is fine: 2 > 2 is False.
#   - Arrows (LC 452): if start > arrow (starts after the arrow) → arrows += 1
#     and arrow = end. Touching balloons share an arrow.
#   - The boundary changes ONLY when you keep an interval / fire an arrow.
#   - arrows = how many (count); arrow = where (position). Tag one-letter-
#     apart names before writing them.
#
# When to use it:
#   - [start, end] ranges + a question about overlaps (fewest to remove,
#     fewest points to cover, can they all fit) → sort by end, walk once.
#   - Read the tie aloud with numbers: does touching count as overlap here?

# LC 435 Non-overlapping Intervals
# Return the fewest intervals to remove so the rest don't overlap.
# Touching ([1, 2] and [2, 3]) is fine.
# Example: [[1, 2], [2, 3], [3, 4], [1, 3]] → 1
# Example: [[1, 10], [2, 3], [4, 5]] → 1

def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda iv: iv[1])     # sort by END
    removed = 0                              # a COUNT
    prev_end = float("-inf")                 # end of the last KEPT interval
    for start, end in intervals:
        if prev_end > start:                 # starts before the last kept one ends
            removed += 1                     # one more removed
        else:
            prev_end = end                   # kept: its END is the new boundary
    return removed


# LC 452 Minimum Number of Arrows to Burst Balloons
# Each balloon spans [start, end]. An arrow shot at x bursts every balloon
# with start <= x <= end. Return the fewest arrows to burst them all.
# Example: [[10, 16], [2, 8], [1, 6], [7, 12]] → 2
# Example: [[1, 2], [2, 3], [3, 4], [4, 5]] → 2

def find_min_arrow_shots(points):
    points.sort(key=lambda b: b[1])          # sort by END
    arrows = 0                               # how MANY arrows (a count)
    arrow = float("-inf")                    # WHERE the last arrow was shot
    for start, end in points:
        if start > arrow:                    # starts after the arrow: not hit
            arrows += 1                      # one more arrow
            arrow = end                      # shot at this balloon's end
    return arrows
