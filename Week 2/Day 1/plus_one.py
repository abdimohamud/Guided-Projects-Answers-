"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9] -> 999 -> +1 -> 1000 -> [1,0,0,0]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
from typing import List

def plus_one(digits: List[int]) -> List[int]:
    # Your code here
    # given a list of single-digit numbers that together represent 
    # a single number 
    # increment the number by 1 
    # case 1: the right-most digit is not 9 
    # just increment the right-most digit by 1 
    # case 2: the right-most digit is 9 
    # change 9 to 0, and then we need to add one to the digit to the left 
    # note that this might cascade if we have more than one 9 to the left 
    # if all the digits are 9s, then we need to add an additional digit to the list 

    # 1. work with the input in the format that it comes in (in-place)
    # 2. transform the input into integers to more easily work with them 
    # technically say idea 2 takes constant extra space since numbers are all 
    # represented with a fixed size 

    # for (let i = digits.length - 1; i >= 0; i--)

    # start iterating from right to left 
    for i in range(len(digits) - 1, -1, -1):
        # if we realize we don't need to continue iterating (cause the current digit 
        # is not a 9), then we'll break out of our loop 
        # check if the current digit is 9 
        if digits[i] == 9:
            digits[i] = 0
        # otherwise, we'll continue iterating from right to left so long as we need to 
        # continue carrying a one over to the next digit 
        else:
            # increment the digit 
            digits[i] += 1
            # we're done
            return digits

    # if we reach here, then we had the situation where every digit was a 9 
    # we need to add a 1 to the front of the `digits` list 
    return [1] + digits 
    # digits.insert(0, 1)
    # return digits 

