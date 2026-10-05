'''
Mission 2 Summary: Sliding Window

Problem: Measuring every contiguous chunk from scratch is O(n·k).

Concept: Keep a running tally of one window, and update only the edges as it moves. O(n).

Two flavors:

Fixed size (max average, max vowels)
  for i in range(k, n):
      window += add(nums[i]) - remove(nums[i - k])

Variable size (max consecutive ones, delete one element)
  for right in range(n):
      add nums[right]
      while window is illegal:
          remove nums[left]; left += 1
      record right - left + 1

When to use it: 
    - contiguous / consecutive / subarray / substring. A given length → fixed window. 
    - "Longest/shortest such that…" → variable window, where the "such that" is your legality rule.
'''

# LC 643 Q: Maximum Average Subarray I
# nums: [1, 12, -5, -6, 50, 3] k = 4
# expected output: 12.75
def find_the_max_average(nums,k):
    window = sum(nums[:k])
    max_avg_subarray = sum(nums[:k])/k
    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        curr_subarray = window/k
        if(curr_subarray > max_avg_subarray):
            max_avg_subarray = curr_subarray
    return max_avg_subarray

# LC 1456: Max Vowels in a Substring of Given Length
# s = "abciiidef", k = 3
# answer: 3   ("iii")
def find_the_max_vowels_in_a_substring(s,k):
    vowels = "aeiou"
    window = sum(x in vowels for x in s[:k])
    max_v_substring = window
    for i in range(k, len(s)):
        window += (s[i] in vowels) - (s[i - k] in vowels)
        if(window > max_v_substring):
            max_v_substring = window
    return max_v_substring

# LC 1004 (Max Consecutive Ones III)
# nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
# expected output: 6
def longest_ones(nums, k):
    left = 0
    zeros = 0
    best = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            # what leaves the window, and what changes?
            if (nums[left] == 0):
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

#LC 1493, Longest Subarray of 1's After Deleting One Element):
def longest_subarray(nums):
    return longest_ones(nums, 1) - 1