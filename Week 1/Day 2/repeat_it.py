"""
Challenge #7:
Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.
Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"
"""
def repeat_it(input_str):
    # Solution 1
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(input_str))

    # Solution 2
    return '-'.join((a * i).title() for i, a in enumerate(input_str, 1))

    # Solution 3
    output = ""
    for i in range(len(input_str)):
        output+=(input_str[i]*(i+1))+"-"
    return output.title()[:-1]

    # Solution 4
    i = 0
    result = ''
    for letter in input_str:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]