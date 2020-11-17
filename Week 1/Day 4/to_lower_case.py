"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string: str) -> str:
    # Your code here

    # use the `ord` function to transform the characters from the string 
    # into a list of ascii numeric values 
    encoded_chars = [ord(char) for char in string]
    # encoded_chars = []
    # for char in string:
    #     encoded_chars.append(ord(char))

    # loop through our list of ascii numeric values 
    for i in range(len(encoded_chars)):
        # check if the current value > 64 and value < 91
        if encoded_chars[i] > 64 and encoded_chars[i] < 91:
            # add 32 to the ascii value 
            encoded_chars[i] += 32

    # use the `chr` function to translate each ascii number back to 
    # a letter 
    decoded_chars = [chr(n) for n in encoded_chars]
    # decoded_chars = []
    # for n in encoded_chars:
    #     decoded_chars.append(chr(n))

    # transform the list back to a string 
    joined = "".join(decoded_chars)

    return joined

    # ord('a') - ord('A') == 32 
    # look up the Python `ord` -> ascii representation 
    #                    `chr` -> character 

to_lower_case("LLAMA")
