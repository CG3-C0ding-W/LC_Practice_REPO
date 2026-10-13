'''
Mission 11 Summary
Problem:
  - Tree DFS assumes arrows only point down. In a graph, an edge can lead
    back to a node you've already seen (room 1 has a key to room 0), so
    dfs(0) → dfs(1) → dfs(0) … never ends.
  - Then: count separate groups, and measure how far something spreads.

Concept:
  - A graph: nodes plus edges in any direction, cycles allowed. Given as a
    list of neighbors (rooms[room]), a 0/1 matrix (isConnected[i][j]),
    or a grid where neighbors are up, down, left, right.
  - A visited set (Mission 4): check first, then add, then go.

How it works:
  - Reachable (LC 841): DFS from the start; return len(visited) == len(rooms).
  - Groups (LC 547): loop over every node; each node not in visited starts a
    new DFS, and each start is one group (count += 1 in the OUTER loop).
    j = the city (where); isConnected[i][j] = 1 or 0 (what).
  - Spreading (LC 994): BFS by levels (Mission 9), one level = one minute.
    Put EVERY starting cell in the queue first. q holds (r, c) cells;
    r, c = q.popleft(); neighbor nr, nc = r + dr, c + dc.
    Check bounds FIRST (0 <= nr < rows ...), then the cell (grid[nr][nc] == 1),
    so an off-grid neighbor is never read (grid[-1] wraps to the last row).
    Loop while q and fresh > 0; at the end, fresh left → -1.
    
When to use it:
  - "Can I reach / which are connected / how many groups" → DFS + visited.
  - "How far / fewest steps / how many minutes / spreads" → BFS by levels.
    BFS reaches each node at its shortest distance first; DFS can take the
    long way round.
'''

# LC 841 Keys and Rooms. There are n rooms numbered 0 to n - 1. Room 0 is unlocked; every other room is locked. 
# rooms[i] is the list of keys you find in room i, and each key is the number of a room 
# it unlocks. Return True if you can visit every room.
# idx:     0      1        2
# rooms = [[1],   [0, 2],  []]                       → True
# 
# idx:     0       1          2     3
# rooms = [[1, 3], [3, 0, 1], [2],  [0]]             → False (nothing unlocks room 2)

def can_visit_all_rooms(rooms):
    visited = {0}                          # room NUMBERS entered
    def dfs(room):
        for key in rooms[room]:            # each key is a room NUMBER
            if key not in visited:         # check first,
                visited.add(key)           # then add,
                dfs(key)                   # then go
    dfs(0)
    return len(visited) == len(rooms)

# LC 547 Number of Provinces
# There are n cities. Some are connected directly; connection is two-way, 
# and if a connects to b and b connects to c, then a is indirectly connected to c. 
# A province is a group of cities that are directly or indirectly connected, 
# with no other cities outside the group.
# 
# You get an n × n matrix isConnected, where isConnected[i][j] == 1 if city i 
# and city j are directly connected, and 0 if not. (Every city is connected to 
# itself, so the diagonal is all 1s.)
# 
# Return the total number of provinces.
#              j=0  j=1  j=2
# isConnected = [
#       i=0  [  1,   0,   1 ],
#       i=1  [  0,   1,   0 ],
#       i=2  [  1,   0,   1 ],
# ]
# n = 3                                  Output: 2
def find_circle_num(isConnected):
    n = len(isConnected)
    visited = set()                              # city NUMBERS reached

    def dfs(i):                                  # i = the city we're standing on
        for j in range(n):                       # j = a city NUMBER (where)
            if isConnected[i][j] == 1 and j not in visited:
                visited.add(j)                   # check first, then add,
                dfs(j)                           # then go

    count = 0
    for i in range(n):
        if i not in visited:                     # no earlier walk reached city i
            visited.add(i)
            dfs(i)
            count += 1                           # a new walk = a new province
    return count

# LC 994: Rotting Oranges
# You get a grid where each cell is:
# 0 = empty, 1 = fresh orange, 2 = rotten orange.
# 
# Every minute, any fresh orange that is next to 
# a rotten orange (up, down, left, or right; not 
# diagonal) becomes rotten.
# 
# Return the minimum number of minutes until no 
# fresh orange is left. If that’s impossible, return -1.
#         c=0  c=1  c=2  c=3
# grid = [
#   r=0  [ 2,   1,   1,   1 ],
#   r=1  [ 0,   0,   0,   1 ],
#   r=2  [ 2,   1,   1,   1 ],
# ]
from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()                          # (r, c) CELLS of rotten oranges
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))         # every rotten orange starts in the queue
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    while q and fresh > 0:               # stop as soon as nothing fresh is left
        minutes += 1                     # one level = one minute
        for _ in range(len(q)):          # snapshot: this minute's batch only
            r, c = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc                  # the neighbor: WHERE
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:   # in bounds, then WHAT
                    grid[nr][nc] = 2     # rot it now (check first, then add)
                    fresh -= 1
                    q.append((nr, nc))
    return minutes if fresh == 0 else -1