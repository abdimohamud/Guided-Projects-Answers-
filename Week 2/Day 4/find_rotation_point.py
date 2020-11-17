"""
I was bored one day and decided to look at last names in the phonebook for my
area.

I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.

When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."

Example:

surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
] => 5 

Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.

*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
from typing import List 

def find_rotation_point(surnames: List[str]) -> int:
    # Your code here
    # worst-case runtime: O(n) since we're doing a full 
    # linear pass through our list of names 
    # Brute Force Approach / Naive approch  
    # 1. iterate through our list of names 
        # check the names two at a time 
        # if we see the second name does not come after the 
        # first name in alphabetical ordering 
            # that's our rotation, return the index of the second name 
    # This plan does not take advantage of the fact that the input is sorted 

    # 2. How can we take advantage of the fact that the data is sorted? 
    # Binary Search: if you're tasked with searching through sorted data, 
    # you should always consider binary search 
    # to denote the boundaries of our search space, we'll have two 
    # variables, left and right 
    left = 0
    right = len(surnames) - 1

    # loop so long as left < right 
    while left < right:
        # get the midpoint of the current search space 
        mid = ((right - left) // 2) + left 
        # check the midpoint element against the first element in the search space
        # # if the midpoint element > the first element 
        if surnames[mid] > surnames[left]:
            # go right 
            left = mid
        else:
            # go left 
            # when we go left, we can't eliminate the midpoint element itself
            # since it might be the rotation point 
            right = mid 

        # check if left and right are next to each other 
        if left + 1 == right:
            return right
            
    
surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

print(find_rotation_point(surnames))
