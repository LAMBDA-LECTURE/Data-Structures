"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import queue
from stack import stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value): # root = 10, value = 2 (the thingy we wanna add)
        if value < self.value: #if 2 < 10 LEFT
            if self.left: # (conditional boolean)does the left one exist?
                self.left.insert(value) # a redo the checks w value here //recursion mind break
            else:
                # if the left one doesn't exist, let's add it!
                self.left = BSTNode(value) # assign that empty left pointer to a new node that we're making with the value
        else: # when value is >= 10 GO RIGHT
            if self.right: # is something here?
                self.right.insert(value) # RECURSION if it's already there
            else: # it's empty, lets drop it here in a new node
                self.right = BSTNode(value)
                # ?celebrate

    # Return True if the tree contains the value
    # False if it does not

    ##Solution from Canvas pre-course
    # def insert(self, value):
    #     if value < self.value:
    #         if self.left is None:
    #             self.left = BSTNode(value)
    #         else:
    #             self.left.insert(value)
    #     else:
    #         if self.right is None:
    #             self.right = BSTNode(value)
    #         else:
    #             self.right.insert(value)

    ##Solution from canvas precourse where they called it search
    def search(self, target):
        if self.value == target:
            return self
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)
    ##contains is the actual homework assignment
    def contains(self, target):
        # start at the top/root/self, by calling the fn
        # if target == self, tada!
        if target == self.value: #
        # return true if tada
            return True
        # is target bigger or smaller than self
        if target < self.value: # go left and look at the left one?
            if self.left: #if that left one exists,
                self.left.contains(target) #loops in loops happily
            else:
                return False
        else: # when target is bigger to self.value
            if self.right: #exists
                self.right.contains(target) # recursion it!
            else: # we hit a dead end, sadface
                return False # let 'em know


            # go left or right until i find it.
        # returnn false if sadface and it doens't exist

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def helper(root):
        if root is None:
            return
        helper(root.left)
        helper(root.right)
        print(root.value)

    def post_order_dft(self):
        # result = []
        helper(self)
        # return result





"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()
