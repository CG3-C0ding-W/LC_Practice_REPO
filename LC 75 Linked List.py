# Mission 7 Summary
# Problem:
#   - Removing from the front of a list is O(n), because every item sits in
#     a numbered slot and the rest have to shift.
#   - Then: find the middle without knowing the length, and reverse a chain
#     in place.
#
# Concept:
#   - A linked list: a chain of nodes, each holding a value (.val) and a
#     pointer to the next node (.next). The last node points to None.
#   - No indexes, so reaching position k means walking .next k times.
#     But removing or inserting next to the node you're on is one arrow: O(1).
#   - Node = where, .val = what.
#
# How it works:
#   - Delete: stand on the node BEFORE the one to remove;
#     prev.next = prev.next.next.
#   - Middle (fast/slow): slow moves 1, fast moves 2; when fast reaches the
#     end, slow is halfway. Start fast at head.next.next so slow stops one
#     before the middle. Loop while fast and fast.next.
#   - Reverse: save, flip, move prev, move cur:
#       nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
#     When cur is None, prev is the new head.
#
# When to use it:
#   - "Find the middle / a position relative to the end" → fast/slow pointers.
#   - "Process the list backward / compare front with back" → reverse
#     (the second half, if you still need the first half).
#   - Rewiring order matters: save any node you'll still need before
#     overwriting the arrow that leads to it.

# LC 2095: Delete the Middle Node of a Linked List
# Given the head of a linked list, delete the middle node and return the head. 
# For a list of n nodes, the middle is index n // 2 (counting from 0).
def delete_middle(head):
    if head.next is None:        # one node: deleting it leaves nothing
        return None
    slow = head                  # idx 0
    fast = head.next.next        # idx 2 (one-turn head start)
    while fast and fast.next:
        slow = slow.next           # slow moves 1 node
        fast = fast.next.next           # fast moves 2 nodes
    slow.next = slow.next.next                       # slow is before the middle: skip it
    return head

# LC 206: Reversing a linked list
# 
def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev 
        prev = cur 
        cur = nxt # four lines: save, flip, move prev, move cur
    return prev