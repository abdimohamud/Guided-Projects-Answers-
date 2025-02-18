"""
You are a new author that is working on your first book. You are working on a
series of drafts. Each draft is based on the previous draft. The latest draft
of your book has a serious typo. Since each newer draft is based on the
previous draft, all the drafts after the draft containing the typo also include
the typo.

Suppose you have `n` drafts `[1, 2, 3, ..., n]` and you need to find out the
first one containing the typo (which causes all the following drafts to have
the typo as well).

You are given access to an API tool `containsTypo(draft)` that will return
`True` if the draft contains a typo and `False` if it does not.

You need to implement a function that will find the *first draft that contains
a typo*. Also, you have to pay a fee for every call to `containsTypo()`, so
make sure that your solution minimizes the number of API calls.

Example:

Given `n = 5`, and `draft = 4` is the first draft containing a typo.

containsTypo(3) -> False
containsTypo(5) -> True
containsTypo(4) -> True
"""
from typing import List

def firstDraftWithTypo(drafts: List[int]) -> int:
    # Your code here
    # use a binary search similar to the rotation point problem 
    left = 0
    right = len(drafts) - 1

    while left < right:
        mid = ((right - left) // 2) + left 

        if containsTypo(mid):
            # we can eliminate every draft after this draft 
            # but not this draft itself since it might be 
            # the first draft with the typo 
            right = mid
        else:
            # we can eliminate every draft before this draft 
            # but not this draft itself since it might be 
            # the last draft without a typo 
            left = mid

        if left + 1 == right:
            return right 
