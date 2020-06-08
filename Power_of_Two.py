'''
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false
'''
#Solution: All power of two numbers have only one bit set.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c=bin(n).count('1')
        return True if (c==1 and n>0) else False
        
        
        
        
        
