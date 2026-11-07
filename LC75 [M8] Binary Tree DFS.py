'''
Mission 8 of 19: Binary Tree DFS (cut to 3 problems)

Encounter:
  Give a linked-list node two arrows, .left and .right, and it becomes a tree.
  A `while cur:` loop can only follow one arrow, so how do you visit both sides?

Concept:
  Recursion. The function calls itself on each child, and Python pauses the
  current call until the child returns (the call stack, same pause/resume
  idea as the stack in Decode String).
  Skeleton: base case for None, one call per child, one combine line.

      def dfs(node):
          if node is None:           # base case
              return ...
          left = dfs(node.left)      # visit the left side
          right = dfs(node.right)    # visit the right side
          return ...                 # combine

How it works:
  - Answers flow UP: catch each child's return (left = dfs(node.left)),
    then combine. Max Depth: max(L, R) + 1, None → 0.
    Count Good Nodes: good + left + right, None → 0.
  - Information flows DOWN as an argument: Count Good Nodes passes
    m = max value above; each node hands down max(node.val, m).
    Good means node.val >= m (a tie counts; the root ties with itself).
  - LCA: each call reports ONE thing, a node or None. If the node is
    p or q, return it. If both sides report something, this node is the
    LCA. Otherwise pass up whichever side found something.
  - A recursive call passes every argument: copy the def line and change
    only the one that moves.
When to use it:
  - A node needs facts about the PATH ABOVE it (depth from root, max so
    far, running path sum) → pass them DOWN as arguments.
  - A node needs facts about the SUBTREE BELOW it (height, counts, did
    I find p or q) → RETURN them UP and combine.
  - Test: change the nodes above, then change the nodes below. Whichever
    one changes the answer is the direction it travels.

Problems:
  LC 104  Maximum Depth             answers flow UP: each node returns a number to its parent
  LC 1448 Count Good Nodes          information flows DOWN: pass the max so far as an argument
  LC 236  Lowest Common Ancestor    both: children report up, the node combines the reports



Then: pattern statement, quiz card, Mission 8 summary as a Python comment block.
'''

# LC 104: Maximum Depth of a Binary Tree 
# Given the root of a binary tree, return its maximum depth: the number of 
# nodes along the longest path from the root down to the farthest leaf.
# 
# Example: the tree below → 4 (path 1 → 2 → 5 → 6). An empty tree (root = None) → 0.
def max_depth(node):
    if node is None:
        return 0            # slot 1: depth of no tree
    L = max_depth(node.left)                   # slot 2: depth of the left subtree
    R = max_depth(node.right)                   # slot 3: depth of the right subtree
    return max(R,L) + 1                # slot 4: your formula from the table

# LC 1448: Count Good Nodes in Binary Tree
# Given the root of a binary tree, a node X is good if, on the path from the root 
# down to X, no node has a value greater than X’s value. Return the number of 
# good nodes.
#           [3]
#          /   \
#        [1]   [4]
#        /     /  \
#      [3]   [1]  [5]
# Example: the tree below → 4. The root is always good.
def good_nodes(root):
    def dfs(node, m):                        # m = max value above node
        if node is None:
            return 0                         # no tree, no good nodes
        good = 1 if node.val >= m else 0     # this node's value is at least the max above it
        new_m = max(node.val, m)             # what node hands down
        left = dfs(node.left, new_m)         # pass new_m DOWN
        right = dfs(node.right, new_m)
        return good + left + right           # counts flow UP
    return dfs(root, root.val)

# LC 236: Lowest Common Ancestor of a Binary Tree
# 
# Given the root of a binary tree and two nodes p and q in it, 
# return their lowest common ancestor: the lowest (deepest) node 
# that has both p and q below it. A node counts as being below 
# itself, so if q is under p, the answer is p.
# 
# You return the node, not its value. Both p and q are always 
# in the tree, and all values are different.
#               [3]
#             /     \
#          [5]       [1]
#         /   \     /   \
#       [6]   [2] [0]   [8]
#            /   \
#          [7]   [4]
def lowest_common_ancestor(root, p, q):
    if root is None:
        return None                        # slot 1: found nothing
    if root is p or root is q:
        return root                        # slot 2: found a target
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)                           # slot 4: report from the right side
    if left and right:
        return root                        # slot 5: one target on each side
    return left if left else right         # pass up whichever side found something (or None)