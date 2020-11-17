"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"

             ["1", "2", "3", "4", "5"]
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str: str) -> str:
    # Your code here
    # given a string of numbers, figure out the min and max numbers 
    # we have functions `max` and `min` which will find the max and min
    # for us
    # max and min work on non-negative numeric strings 
    # it's feasible that we get a string of all negative numbers 
    # because of negative numbers, we can't get away with not turning 
    # the string into numbers 
    # how do we take the input string and turn it into a list of number? 
    # we can split the input string on spaces 
    str_digits = input_str.split(" ")
    int_digits = []

    # transform each str_digit into a number 
    # we can use the `int` function for that 
    for str_digit in str_digits:
        int_digit = int(str_digit)
        int_digits.append(int_digit)

    # once we have a list of numbers, then we can use max and min to 
    # calculate the max and min 
    mx = max(int_digits)
    mn = min(int_digits)

    # use an f-string to perform string interpolation to return the desired output 
    return f"{mx} {mn}"

print(max_and_min("1 2 3 4 5"))
