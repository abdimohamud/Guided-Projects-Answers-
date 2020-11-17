"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""

def is_even(n: int) -> bool:
    # use the `%` or modulo operator to determine if it's even or odd 
    return n % 2 == 0

def get_middle(input_str):
    # Your code here
    # how do we determine if the length of a string is even or odd?
    if is_even(len(input_str)):
        # return the two middle characters if the length of the string is even 
        # figure out how to get the middle chars
        midpoint = len(input_str) // 2
        # we want to slice from midpoint - 1 up to midpoint + 1
        return input_str[midpoint - 1 : midpoint + 1]
    else:
        # return the single middle character if the length of the string is odd 
        # figure out how to get the middle char
        # calculate the midpoint index by dividing the length by 2 
        # since we want to use the midpoint as an index, we can't have it be a 
        # decimal, we can round the midpoint down 
        midpoint = len(input_str) // 2
        return input_str[midpoint]


print(get_middle("middle"))
