# how do we implement an array-reverse function in-place? 
def reverse(arr):
    # this doesn't work because slicing creates a copy
    # of the input array
    # return arr[::-1]
    left = 0
    right = len(arr) - 1

    # how do we iterate?
    # iterate so long as left < right
    while left < right:
        # if there's an odd number of elements in the input arr
        # we have the case where left and right land on that 
        # middle element 
        # swap the elements they're pointing at 
        # this does use an extra `temp` variable under 
        # the hood 
        arr[left], arr[right] = arr[right], arr[left]
        # increment the left pointer 
        left += 1
        # decrement the right pointer 
        right -= 1

    return arr 

arr = [26, 42, 16, 22, 8, 7, 4, 5]
print(reverse(arr))
