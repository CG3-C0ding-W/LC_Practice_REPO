# Mission 5 Summary
# Problem: 
#   - Each new item has to cancel, match, or combine with the 
#     most recent pending item (stars, asteroids, brackets). 
#   - Then: for each item, find the nearest warmer or bigger 
#     item without rescanning, which would be O(n²).
# 
# Concept: 
#   - A stack (the backspace key: every add and delete at the same end). 
#   - A monotonic stack is a stack kept sorted: the new item pops everything it beats, then is pushed.
# 
# How it works: 
#   - The stack holds items still waiting for an answer. When a new item beats the top, 
#     the top gets its answer (Daily Temperatures: answer[j] = i - j) or hands over its 
#     receipt (Stock Span: span += s). A while loop# , because one item can beat several.
# 
# When to use it: 
#   - “For each item, the nearest item to the left or right that’s greater (or smaller)” → monotonic stack. 
#   - “Each item interacts with the most recent pending one” → plain stack.

# LC 2390: Removing Stars From a String. You're given a string s of lowercase letters and *. 
# Each * removes itself and the closest non-star character to its left. 
# Return the string after all stars are processed. 
#   - (Every * is guaranteed to have a letter to remove.)
def remove_stars(s):
    stack = []
    for ch in s:
        if ch == "*":
            stack.pop()     # 1. backspace
        else:
            stack.append(ch)     # 2. type ch
    return "".join(stack)    # glue the list back into a string

# # LC 735: Asteroid Collision
# You're given a list of integers representing asteroids in a row.
# The size is the absolute value; the sign is the direction: positive moves right →, negative moves left ←.
# All move at the same speed. When two meet, the smaller one explodes; if they're the same size, both explode.
# Two asteroids moving the same direction never meet. And a left-mover on the left with a right-mover on the right ([-5, 10]) drift apart, so they never meet either.
# asteroids 	Output
# [5, 10, -5]	[5, 10] (−5 hits 10 and explodes)
# [8, -8]	    [] (equal, both explode)
def asteroid_collision(asteroids):
    stack = []
    for a in asteroids:
        alive = True
        while alive and a < 0 and stack and stack[-1] > 0:
            if stack[-1] < -a:
                stack.pop() # 1. top is smaller: top explodes, a keeps going
            elif stack[-1] == -a:
                stack.pop()
                alive = False          # 2. same size: both explode
            else:
                alive = False          # 3. top is bigger: a explodes
        if alive:
            stack.append(a)
    return stack

# LC 394: Decode String
# 
# An encoded string uses the rule k[text], meaning repeat text exactly k times. Brackets can be nested. k is always a positive integer, and the input is always valid.
# 
#    Input	          Output
# "3[a]2[bc]"	    "aaabcbc"
# "3[a2[c]]"	    "accaccacc"
# "2[abc]3[cd]ef"	"abcabccdcdcdef"
def decode_string(s):
    stack = []
    cur = ""
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((cur, num))   # pause this level
            cur = ""
            num = 0
        elif ch == "]":
            prev, k = stack.pop()      # resume the level we paused
            cur = prev + cur * k
        else:
            cur += ch
    return cur

# LC 379: Daily Temperatures
# Given a list temps of daily temperatures, return a list answer where answer[i] is how many days you wait after day i to get a warmer day. 
# If no warmer day ever comes, answer[i] = 0. 
# Ex.
# idx:    0   1   2   3   4   5   6   7
# temps: 73  74  75  71  69  72  76  73
# answer: 1   1   4   2   1   1   0   0

def daily_temperatures(temps):
    answer = [0] * len(temps)     # 0 = "never answered" (days 6, 7)
    stack = []                    # INDEXES of days still waiting
    for i in range(len(temps)):
        while stack and temps[stack[-1]] < temps[i]:  # top check column
            j = stack.pop()         # popped column: which day
            answer[j] = i - j   # popped column: how long it waited
        stack.append(i)                   # last column: today joins the waiting days
    return answer

# LC 901: Online Stock Span
# Prices arrive one day at a time. For each new price, 
# return its span: the number of consecutive days ending 
# today (counting today) where the price was ≤ today’s price. 
# Walk backward from today and stop at the first day with a higher price.
# Ex. 
# day:    0    1    2    3    4    5    6
# price: 100   80   60   70   60   75   85
# span:   1    1    1    2    1    ?    ?
class StockSpanner:
    def __init__(self):
        self.stack = []                  # (price, span) pairs, prices decreasing

    def next(self, price):
        span = 1                         # today
        while self.stack and self.stack[-1][0] <= price:
            p, s = self.stack.pop()
            span += s                    # absorb its receipt
        self.stack.append((price, span))
        return span