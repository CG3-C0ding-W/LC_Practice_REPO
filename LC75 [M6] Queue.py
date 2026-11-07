# Mission 6 Summary
# Problem:
#   - Each new item has to interact with the OLDEST pending item, not the
#     most recent (a "*" that deletes the first letter, pings that expire
#     after 3000 ms, senators taking turns in rounds).
#   - A list can remove from the front with pop(0), but every remaining
#     item shifts down one slot: O(n) per removal.
#
# Concept:
#   - A queue (a line at a store): join at the back, leave from the front.
#     First in, first out.
#   - In Python, collections.deque: append(x) at the back, popleft() from
#     the front, q[0] to peek at the front. All O(1).
#
# How it works:
#   - Recent Calls: append each ping; while the front ping is earlier than
#     the range start (q[0] < t - 3000), popleft it. len(q) is the answer.
#     A while loop, because one ping can expire several at once.
#   - Dota2 Senate: one queue of INDEXES per party. Pop both fronts; the
#     smaller index acts first and bans the other. The winner goes back as
#     i + n, so it waits behind everyone in the current round.
#     Turn order decides the winner, not head count.
#
# When to use it:
#   - "Process items in the order they arrived" or "drop the oldest items
#     once they expire" → queue.
#   - Stack vs. queue: most recent pending → stack (pop()); oldest pending
#     → queue (popleft()).

from collections import deque

q = deque()
q.append("x")      # join at the back        O(1)
q.popleft()      # leave from the front    O(1)
q[0]             # peek at the front       O(1)

# LC 933: Number of Recent Calls
# Each call ping(t) adds a request at time t (in ms) and 
# returns how many requests happened in the range [t - 3000, t], 
# both ends included. Each t is larger than the last.

from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# LC 649: Dota2 Senate
# A string senate lists senators in order: 'R' (Radiant) or 'D' (Dire). 
# Voting happens in rounds, going left to right. On their turn, each 
# senator who hasn’t been banned bans one senator from the other party. 
# Banned senators skip all future turns. Rounds repeat until only one 
# party has senators left; return "Radiant" or "Dire".
# Every senator plays smart: ban the opposing senator who would act next 
# (wrapping around to the next round if needed). That’s the opponent 
# who’d otherwise ban one of yours soonest.
# Ex.
# idx:     0  1  2  3  4
# senate:  R  R  D  D  D
from collections import deque

def predict_party_victory(senate):
    n = len(senate)
    r = deque()
    d = deque()
    for i in range(n):
        if senate[i] == "R":
            r.append(i)
        else:
            d.append(i)

    while r and d:
        ri = r.popleft()
        di = d.popleft()
        if ri < di:
            r.append(ri + n)
        else:
            d.append(di + n)
    return "Radiant" if r else "Dire"