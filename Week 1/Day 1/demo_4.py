"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
def find_perimeter(length: int, width: int) -> int:
    # Your code here
    # take length and width integers, treat them as the dimensions 
    # of an imaginary rectangle 
    # how do we calculate the perimeter from a length and a width? 
    perimeter = 2 * length + 2 * width 
    # return the perimeter of this imaginary rectangle
    return perimeter 

    # return 2 * length + 2 * width
