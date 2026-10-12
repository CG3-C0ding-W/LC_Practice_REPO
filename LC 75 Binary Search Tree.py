'''
Mission 10 Summary
Problem:
  - In a plain tree, finding a value means visiting every node, since it
    could be anywhere. Deleting a node also has to keep the tree in shape.
    
Concept:
  - A binary search tree (BST): for every node, everything in its left
    subtree is smaller and everything in its right subtree is larger.
  - Each compare throws away a whole subtree (like opposite-ends two
    pointers throwing away one end).

How it works:
  - Search: compare val with root.val. Equal → return the NODE.
    Smaller → left, larger → right. Fell off (None) → not found.
    Recursive call: copy the def line, change only what moves
    (search_bst(root.left, val)).
  - Delete: each call returns the TOP of its subtree after the delete;
    the parent catches it (root.left = delete_node(root.left, key)).
      leaf or only a right child → return root.right
      only a left child          → return root.left
      two children               → cur = root.right; walk cur = cur.left
                                   to the smallest; copy cur.val into root;
                                   delete cur.val from root.right.
  - On a tie, neither < nor > is true: that's the found branch.

When to use it:
  - The tree is sorted by the BST rule and you need to find, insert, or
    delete a value → compare and go one way (O(height), not O(n)).
  - "Smallest / largest in a subtree" → walk left / right until None.
'''

# LC 700 Search in a Binary Search Tree. Given the root of a BST and an integer val, 
# return the node whose value equals val (the subtree rooted there). 
# If no such node exists, return None.
#             [8]
#            /   \
#         [3]     [10]          val = 7  → returns [7]
#         / \        \          val = 5  → returns None
#      [1]  [6]      [14]
#           / \
#        [4]  [7]
def search_bst(root, val):
    if root is None:
        return None                     # fell off the tree: not found
    if root.val == val:                            # val equals this node's value
        return root                     # a NODE
    if val < root.val:                        # val is less than this node's value
        return search_bst(root.left, val)         # go left
    return search_bst(root.right, val)             # go right

# LC 450 Delete Node in a BST. Search finds a node; deleting one 
# has to keep the BST rule true afterward. Start with the easiest case, a leaf:
#             [8]                              [8]
#            /   \                            /   \
#         [3]     [10]     delete 3 →      [4]     [10]
#         / \        \                     / \        \
#      [1]  [6]      [14]               [1]  [6]      [14]
#           / \                                \
#        [4]  [7]                              [7]
def delete_node(root, key):
    if root is None:
        return None                                   # key not in tree
    if key < root.val:
        root.left = delete_node(root.left, key)       # catch the new left top
    elif key > root.val:
        root.right = delete_node(root.right, key)     # catch the new right top
    else:                                             # found: delete root
        if root.left is None:                         # leaf, or only a right child
            return root.right
        if root.right is None:                        # only a left child
            return root.left
        cur = root.right                              # two children:
        while cur.left:                               # smallest on the right
            cur = cur.left
        root.val = cur.val                            # copy its VALUE
        root.right = delete_node(root.right, cur.val) # remove the duplicate below
    return root