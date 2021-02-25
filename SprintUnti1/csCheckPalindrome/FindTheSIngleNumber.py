"""
You are given a non-empty array of integers.

One element appears exactly once, with every other element appearing at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.

Example 1:

Input: [1,1,2,1]
Output: 2
"""

def csFindTheSingleNumber(nums):
    res = {}
    
    for i in nums:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    
    for key, value in res.items():
        if value == 1:
            return key
    

