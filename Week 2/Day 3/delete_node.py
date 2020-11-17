"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

# Receives the first node in the linked list 
# and a linked list "index" 
def delete_node(head, index):
    # Your code here
    # start traversing our linked list from the head 
    # until we get to the node right before the one 
    # we're going to delete 
    current = head 
    # keep a counter to know how many linked list nodes we've traversed 
    counter = 1

    # iterate until counter == index - 1
    while counter != index - 1:
        current = current.next 
        counter += 1

    # `current` is now at the index - 1 position 
    # update the current node's `next` to the next node's next 
    current.next = current.next.next 

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

delete_node(z, 3)

print_ll(x)
