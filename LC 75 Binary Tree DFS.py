'''
Mission 8 of 19: Binary Tree DFS (cut to 3 problems)

Encounter:
  Give a linked-list node two arrows, .left and .right, and it becomes a tree.
  A `while cur:` loop can only follow one arrow, so how do you visit both sides?

Concept:
  Recursion. The function calls itself on each child, and Python pauses the
  current call until the child returns (the call stack, same pause/resume
  idea as the stack in Decode String).

      def dfs(node):
          if node is None:           # base case
              return ...
          left = dfs(node.left)      # visit the left side
          right = dfs(node.right)    # visit the right side
          return ...                 # combine

Problems:
  LC 104  Maximum Depth             answers flow UP: each node returns a number to its parent
  LC 1448 Count Good Nodes          information flows DOWN: pass the max so far as an argument
  LC 236  Lowest Common Ancestor    both: children report up, the node combines the reports

Likely hot spots:
  - node vs. .val (your where-vs-what error): compare node.val, return node
  - which variable holds what: catch the child's answer (left = dfs(...))
    instead of calling and dropping it
  - comparison order: "good" means node.val >= max_so_far (build it from the comment)
  - off by one: what None returns (0, not 1) and where the +1 goes

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