"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
from typing import List

# def get_left_sum(nums, index):
#     if index == 0:
#         return 0
#     return sum(nums[0:index])

# def get_right_sum(nums, index):
#     if index == len(nums) - 1:
#         return 0
#     return sum(nums[index+1:])

# def pivot_index(nums: List[int]) -> int:
#     # Your code here
#     # 1. for each number, we'll go ahead and sum up everything to its left 
#     # and everything to its right 
#     # check if those sums are equal 
#     # as soon as we find such a number, we'll return it 
#     # O(n^2)
#     for i in range(len(nums)): # O(n)
#         # get the left sum 
#         # these two sum steps have us touch every other list element
#         # for j in range(len(nums)) 
#         # O(n)
#         left_sum = get_left_sum(nums, i) # O(n/2)
#         # get the right sum 
#         right_sum = get_right_sum(nums, i) # O(n/2)

#         if left_sum == right_sum:
#             return i
    
#     return -1

# O(2 * n) ~ O(n)
def pivot_index(nums):
    left = 0
    right = sum(nums) # O(n)

    for i, num in enumerate(nums): # O(n)
        right -= num

        if left == right:
            return i

        left += num

    return -1

print(pivot_index([1,7,3,6,5,6]))
