# Mission 18 Summary
# Problem:
#   - "Which stored words start with what's been typed?" Checking every
#     word letter by letter repeats work: "cat", "car", "cart" all start
#     c-a, and each check re-reads those same letters.
#
# Concept:
#   - A trie: a tree where each edge is a letter. Words with the same
#     beginning share one path from the root. A prefix is a walk from the
#     root; every word below that node starts with it.
#   - Node: children = {letter: child NODE} and is_end (the ★: a word ends
#     here). A bare dict means keys: ch in cur.children asks about letters.
#   - ch is a LETTER (what); cur.children[ch] is a NODE (where).
#
# How it works:
#   - Insert (LC 208): for each letter, check first, then add
#     (if ch not in cur.children: create a TrieNode), then step:
#     cur = cur.children[ch]. Mark cur.is_end = True after the loop.
#   - search and startsWith walk the same way; a missing letter → False.
#       search      → return cur.is_end    (a WORD must end here)
#       startsWith  → return True          (the PATH is enough)
#     "ca" is a path in {cat, car} but not a word.
#   - Suggestions (LC 1268): insert products in SORTED order; each node keeps
#     the first 3 words that pass through it (len(cur.words) < 3). Typing
#     walks one node per letter and reads cur.words; after falling off,
#     append [] (an empty list, not None).
#   - Stored fields have no ( ): cur.is_end, not cur.isEnd().
#
# When to use it:
#   - Questions about PREFIXES (starts with, autocomplete, suggestions as
#     you type) over many words → trie.
#   - Exact-word lookups only → a set (Mission 4) is enough.

# LC 208 Implement Trie (Prefix Tree)
# Build a Trie with insert(word), search(word) (True if word was
# inserted), and startsWith(prefix) (True if any inserted word starts
# with prefix).
# Example: insert("apple"); search("apple") → True; search("app") → False;
#          startsWith("app") → True; insert("app"); search("app") → True

class TrieNode:
    def __init__(self):
        self.children = {}       # letter → child NODE
        self.is_end = False      # the ★: does a word end here?

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:           # check first,
                cur.children[ch] = TrieNode()    # then add
            cur = cur.children[ch]               # step to the child NODE
        cur.is_end = True                        # mark the ★

    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]               # a NODE, not the letter ch
        return cur.is_end                        # a word must end here

    def startsWith(self, prefix):
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True                              # the path exists


# LC 1268 Search Suggestions System
# Given products and searchWord, after each letter typed, return up to 3
# products that start with the typed prefix, in alphabetical order.
# Return a list of these lists.
# Example: products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
#          searchWord = "mouse" →
#          [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"],
#           ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]

class SuggestNode:
    def __init__(self):
        self.children = {}       # letter → child NODE
        self.words = []          # up to 3 suggestions for this prefix

def suggested_products(products, searchWord):
    root = SuggestNode()
    for p in sorted(products):                 # alphabetical, so the first 3 are the right 3
        cur = root
        for ch in p:
            if ch not in cur.children:
                cur.children[ch] = SuggestNode()
            cur = cur.children[ch]
            if len(cur.words) < 3:             # this node holds fewer than 3 words
                cur.words.append(p)

    ans = []
    cur = root
    for ch in searchWord:
        if cur and ch in cur.children:
            cur = cur.children[ch]
            ans.append(cur.words)              # this node's suggestions (a list)
        else:
            cur = None                         # fell off: nothing matches from here on
            ans.append([])                     # an empty LIST, not None
    return ans
