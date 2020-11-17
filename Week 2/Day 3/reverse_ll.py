"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(node):
    # we want the input node (the "head") to become the new tail 
    # we want the old tail to becom the new head 
    # three pointers, prev, current, forward 
    current = node 
    prev = None 
    forward = None 

    while current:
        # set `forward` to current's `next`
        forward = current.next 

        # switch the direction of `current`'s arrow 
        current.next = prev 

        # update our pointers
        prev = current 
        current = forward 

    # we need to return the new head, which the `prev` pointer is referring to 
    return prev

def print_ll(node):
    # we'll traverse the ll from left to right
    # some way to keep track of where we are as we're iterating 
    # use a variable/reference
    # set your `current` variable to the starting node 
    current = node 

    # keep moving `current` in a loop 
    # while current:
    while current is not None: 
        # how do we move `current`?
        # the variable itself 
        # and what the variable is referring 
        print(current.value)
        current = current.next 

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
a = LinkedListNode('A')

x.next = y
y.next = z
z.next = a

print_ll(x)

new_head = reverse(x)

print_ll(new_head)
