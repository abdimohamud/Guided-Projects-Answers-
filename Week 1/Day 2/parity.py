"""
Challenge #8:
Given an integer, write a function that returns "Even" for even integers and
"Odd" for odd integers.
Examples:
- parity(0) -> "Even"
- parity(1) -> "Odd"
- parity(2) -> "Even"
"""
def parity(input_int):
    # Solution 1
    return 'Odd' if input_int % 2 else 'Even'

    # Solution 2
    return 'Even' if input_int % 2 == 0 else 'Odd'

    # Solution 3
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

    # Solution 4
    return ["Even", "Odd"][number % 2]