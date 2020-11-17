"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:                               0  1  2  3
- nth_smallest([7, 5, 3, 1], 1) ➞ 1    [1, 3, 5, 7], 5
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""
from typing import List

def nth_smallest(lst: List[int], n: int) -> int:
    # Your code here
    # what if there is no nth smallest? 
    # check if n > len(lst) to determine if there is an nth smallest 
    if n > len(lst):
        return None
    # given an unsorted array, find the nth smallest 
    # note that the smallest element is the first smallest 
    # how can we find the nth smallest? 
    # let's sort the list first 
    lst.sort()
    # now that the list is in sorted order, we can index into it 
    # to fetch the nth smallest 
    # note that we'll need to index by n - 1 to account for 0-indexing 
    n_smallest = lst[n - 1]
    # return the nth smallest number 
    return n_smallest

    # return lst[n - 1]

print(nth_smallest([1,3,5,7], 5))