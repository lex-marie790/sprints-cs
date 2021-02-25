"""Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that can be formed.

Example 1:

Input: text = "mbxcdatlas"
Output: 1
"""

def csMaxNumberOfLambdas(text):
    lambdaDict = {'l': 0, 'a': 0, 'm': 0, 'b': 0, 'd': 0, 'a': 0}
    for i in text:
        if i in lambdaDict:
            lambdaDict[i] += 1
    return min(lambdaDict.values())
            
