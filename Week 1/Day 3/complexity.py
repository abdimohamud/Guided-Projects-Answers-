# We only multiply when some logic is nested
# When code is stacked sequentially on top of one another 
# we add their respective runtimes 

# O(1) + O(1) + O(1) + O(0.5n) + O(2000)
# O(0.5n + 2000 + 1 + 1 + 1)
# O(0.5n + 2003)
# O(n + 2003)
# O(n)
def do_a_bunch_of_stuff(items):
    last_idx = len(items) - 1 # getting the length is O(1)

    print(items[last_idx]) # accessing an array element via index - O(1)
                           # we'll consider printing/console logging O(1) 

    middle_idx = len(items) / 2 # arithmetic operations - O(1) 
    idx = 0                     # initializing a variable - O(1) 

    # 0.5n * 1 * 1 = 0.5n 
    while idx < middle_idx:  # this loop only runs over half our items 
                             # 1000 * n
                             # ~ n 
        print(items[idx])    # O(1)
        idx = idx + 1        # O(1)

    # O(2000 * 1) = O(2000)
    for num in range(2000):  # O(2000)
        print(num)           # O(1) 

# O(n) + O(n) = O(2 * n) = O(n)
def removeDuplicate(arr):
  differents = {} # initializing a variable - O(1)

  # O(n) * O(1) * O(1) * O(1) = O(n)
  for i in arr: # O(n)
    if i not in differents: # O(1)
      differents[i] = []    # O(1) - Setting `i` as a key in the dict and setting its
                            # value to an empty list 

    differents[i] += [i]    # 1. appending onto the end of the list - O(1)
                            # 2. accessing the key in the dictionary - O(1)

  return differents.keys()  # the `keys` method takes all the keys in the dictionary
                            # and returns them all as a list 
                            # O(n)

print(removeDuplicate([1,1,2,4,5,5,3,3,1,2]))
