'''
# Mission 13 Summary
# Problem:
#   - "The k-th largest" or "the smallest still available" can be found by
#     sorting, but that orders EVERY item when you only need one end, and
#     you'd re-sort every time an item arrives or comes back.
#
# Concept:
#   - A heap: a container that always hands you its SMALLEST item.
#       heapq.heappush(heap, x)   add                O(log n)
#       heapq.heappop(heap)       remove the smallest O(log n)
#       heap[0]                   peek at the smallest (only looks)
#   - Only heap[0] is guaranteed; heap[1] is not the 2nd smallest.
#   - Python's heap is min-only. For a max-heap, push -x; -heap[0] is the largest.
#
# How it works:
#   - K-th largest (LC 215): push each number; if len(heap) > k, pop.
#     The smallest of the k you hold gets kicked out each time, so heap[0]
#     is the smallest of the k largest = the k-th largest. Return a VALUE.
#   - Infinite set (LC 2336): self.cur stands for the whole tail
#     {cur, cur + 1, ...}. Numbers added back (num < self.cur) go in a heap,
#     plus a set to block duplicates. Pop: peek heap[0] < self.cur → heappop;
#     otherwise return cur and self.cur += 1.
#   - The check only peeks (heap[0]); only the body pops.
#   - Inside a class, copy names exactly as __init__ wrote them (self.cur).
#
# When to use it:
#   - You keep needing the smallest (or largest) of a collection that
#     changes → heap.
#   - "K-th largest / top k" → min-heap of size k.
#   - Sorted once and never changes → sort, or binary search (Mission 12).

Reach for a heap when you repeatedly need the smallest (or largest) item
of a collection that keeps changing.
  - k largest   → MIN-heap capped at k items; heap[0] is the k-th largest.
  - largest     → push -x, read -heap[0] (Python's heap is min-only).
  - heap[0] peeks; heappop removes.
'''
# LC 215 Kth Largest Element in an Array
# Given nums and k, return the k-th largest value.
# Example: nums = [3, 2, 1, 5, 6, 4], k = 2 → 5.
heap = []
for x in nums:
    heapq.heappush(heap, x)        # hold the new one
    if len(heap) > k:              # holding more than k
        heapq.heappop(heap)        # kick out the smallest
return heap[0]

'''
LC 2336 Smallest Number in Infinite Set
A set starts holding every positive integer: {1, 2, 3, 4, 5, ...}.
popSmallest() removes the smallest number in the set and returns it.
addBack(num) puts num back into the set, if it’s not already in it.
'''
import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.cur = 1                 # every number from cur up is in the set
        self.heap = []               # added-back numbers, all below cur
        self.in_heap = set()         # what's in the heap, to block duplicates

    def popSmallest(self):
        if self.heap and self.heap[0] < self.cur:   # peek: the heap's smallest is below cur
            x = heapq.heappop(self.heap)            # pop: remove it
            self.in_heap.remove(x)
            return x
        x = self.cur
        self.cur += 1                               # the tail now starts one higher
        return x

    def addBack(self, num):
        if num < self.cur and num not in self.in_heap:   # missing, and not already back
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)

