"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []

    # method to get the length the stack 
    def __len__(self):
        return len(self.data)
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()  # O(1)
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        # holds the elements from the in_stack in reversed order 
        # when we call the dequeue method, we'll pop from this stack 
        self.out_stack = Stack()
        # holds the incomine enqueued elements 
        self.in_stack = Stack()

    def enqueue(self, item):
        # add the element to our `in_stack` 
        self.in_stack.push(item)

    def dequeue(self):
        # we need to check if the `out_stack` is empty 
        # otherwise, just pop from the top of the `out_stack` 
        if len(self.out_stack) == 0:
            # empty the contents of the `in_stack` into the `out_stack` 
            while len(self.in_stack) != 0:
                # pop from the in_stack
                popped = self.in_stack.pop()
                # add it to the out_stack 
                self.out_stack.push(popped)
        
        return self.out_stack.pop()

q = QueueTwoStacks()

print(q.dequeue())

q.enqueue(3)
q.enqueue(6)
print(q.dequeue())
q.enqueue(7)
q.enqueue(8)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
            

# class QueueTwoStacks:
#     def __init__(self):
#         # Your code here
#         self.data = []
        
#     def enqueue(self, item):
#         # Your code here
#         self.data.append(item)

#     def dequeue(self):
#         # Your code here
#         if len(self.data) > 0:
#             return self.data.pop(0)  # O(n)
#         return "The queue is empty"

# Python's deque allows us to efficiently remove 
# from either the front or the back 
# from collections import deque

# class QueueTwoStacks:
#     def __init__(self):
#         self.data = deque()

#     def enqueue(self, item):
#         self.data.append(item)

#     def dequeue(self):
#         if len(self.data) > 0:
#             return self.data.popleft()
#         return "The queue is empty"
