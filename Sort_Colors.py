'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
1. A rather straight forward solution is a two-pass algorithm using counting sort.
2. First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''

#Solution: With Single-Pass

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        mid = 0
        while mid <= r: 
            if nums[mid] == 0: 
                nums[l], nums[mid] = nums[mid], nums[l] 
                l = l + 1
                mid = mid + 1
            elif nums[mid] == 1: 
                mid = mid + 1
            else: 
                nums[mid], nums[r] = nums[r], nums[mid]  
                r = r - 1
        return nums 
        
        
        
        
        
