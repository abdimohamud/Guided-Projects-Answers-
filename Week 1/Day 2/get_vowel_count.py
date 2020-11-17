"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str: str) -> int:
    # Your code here
    # count number of vowels
    # keep a counter to keep track of number of vowels 
    num_vowels = 0
    # we need to inspect every character in the input string 
    # to see if it's a vowel 
    # keep a list or a string of all the vowels we care about 
    vowels = "aeiou"

    # iterate through the characters of our input string 
    # we don't care about the indices of each character 
    for char in input_str:
        # how do we know it's a vowel? 
        # doesn't look like there's a built-in function/method for this 
        # as we iterate, we can check if the current character is part of the 
        # vowel string/list 
        if char in vowels:
            # if it is, increment our counter 
            num_vowels += 1

    # return our counter 
    return num_vowels

print(get_count("abcdefghijklmnopqrstuvwxyz"))
