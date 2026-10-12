'''
Mission 9 of 19: Binary Tree BFS

Encounter:
  DFS dives down one side before it touches the other. "Show me the
  rightmost node of each level" needs the tree one LEVEL at a time instead.

Concept:
   - Breadth-first search (BFS): the Mission 6 queue, holding NODES.
     Pop the front node, append its children to the back, so nodes come
     out row by row, left to right.
   - The snapshot: for _ in range(len(q)) reads len(q) ONCE, when the
     queue holds exactly one level. Children appended during the level
     wait for the next pass of the while loop.

      q = deque([root])
      while q:
          for _ in range(len(q)):     # exactly this level's nodes
              node = q.popleft()
              ...
              if node.left:  q.append(node.left)
              if node.right: q.append(node.right)
How it works:
  - Right Side View: after the for loop, node holds the LAST node popped,
    the rightmost of the level → ans.append(node.val).
    (First popped, i == 0, is the leftmost.)
  - Maximum Level Sum: each node adds itself (level_sum += node.val);
    after the level, if level_sum > best_sum, save the sum AND the level.
    ">" keeps the earlier level on a tie. Levels count from 1.
  - Tags: q holds NODES (append node.left), answers hold VALUES
    (node.val, no parentheses), and the function returns a LEVEL, not a sum.

When to use it:
  - The question is about each level (per-row answers, first/last in a
    row, level sums) → BFS with a len(q) snapshot.
  - The question is about a path from the root or a subtree below a node
    → DFS (Mission 8).
              
Problems:
  LC 199 Right Side View      the last node popped in each level → its .val
  LC 1161 Maximum Level Sum   add up each level; return the smallest level
                              number with the largest sum

Likely hot spots for you:
  - Node vs. .val: the queue holds NODES (append node.left), but the answer
    list holds VALUES (append node.val). Your most frequent error, in a
    new form; tag each append before you write it.
  - Which variable holds what: len(q) taken once as a snapshot vs. a queue
    that grows while you loop; the level counter vs. the sum.
  - Comparison: LC 1161 keeps the FIRST level on a tie, so it updates only
    on ">". Built from the comment: "this level's sum / is greater than /
    the best so far".
  - Off by one: levels are numbered from 1, not 0.
  - Path vs. level: "the right side view" is not just root.right.right...
    (a left-side node can stick out further down).

'''
# LC 199:  Right Side View
# Given the root of a binary tree, imagine standing on its right side. 
# Return the values of the nodes you can see, ordered from top to bottom.
#           [1]
#          /   \
#        [2]   [3]
#        / \
#      [4] [5]
#            \
#            [8]
from collections import deque

def right_side_view(root):
    if root is None:
        return []
    ans = []                          # holds VALUES
    q = deque([root])                 # holds NODES
    while q:
        for _ in range(len(q)):           # this level's size, read once
            node = q.popleft()
            if node.left:
                q.append(node.left)          # a NODE
            if node.right:
                q.append(node.right)          # a NODE
        ans.append(node.val())                # the last node popped this level
                                              # is the rightmost: record its VALUE
    return ans

# LC 1161 Maximum Level Sum of a Binary Tree: Given the root of a binary tree, the root is at level 1, 
# its children at level 2, and so on. Return the smallest level number whose sum of node values is the largest.
#           [1]              level 1
#          /   \
#        [7]   [0]           level 2
#        / \
#      [7] [-8]              level 3
from collections import deque

def max_level_sum(root):
    best_sum = float("-inf")          # largest SUM seen so far
    best_level = 0                    # the LEVEL where it was seen
    level = 0
    q = deque([root])                 # NODES
    while q:
        level += 1                    # levels count from 1
        level_sum = 0
        for _ in range(len(q)):
            node = q.popleft()
            level_sum += node.left.val + node.right.val           # a VALUE
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if level_sum > best_sum:                        # this level's sum is greater than the best so far
            best_sum = level_sum             # a SUM
            best_level = level           # a LEVEL
    return best_level