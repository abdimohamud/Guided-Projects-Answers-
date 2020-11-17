"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt: str) -> bool:
    # Your code here
    # how do we keep track of the number of "x"s and "o"s
    # let's keep two variables, one that tracks of number of "x"s
    # the other one tracks number of "o"s
    xs = 0
    os = 0
    # figure out the number of "o"s and "x"s in the input string 
    # we need to look at every character in the `txt` string 
    # we'll iterate over `txt`
    # we need to accommodate case insensitivity 
    # you could use the `string.lower` method to lowercase the input string 
    for character in txt:
        # if we see an "x", increment `xs`
        if character == "x" or character == "X":
            xs += 1
        # if we see an "o", increment `os`
        if character == "o" or character == "O":
            os += 1
    # at this point, `os` and `xs` should each be keeping track of 
    # number of "x"s and "o"s respectively 
    # check if the number of "o"s and "x"s is the same 
    # if xs == os:
    #     return True
    # else: 
    #     return False 
    return xs == os 
    # return True if they are, False otherwise 

print(XO("ooxXm"))