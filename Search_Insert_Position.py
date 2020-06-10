'''
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
'''

#Solution 1: Using linear search (O(n))

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=len(nums)
        for i in range(l):
            if(nums[i]==target or nums[i]>target):
                return i
        else:
            return l
            
#Solution 2: Using Binary Search (O(log(n))     

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums)-1
        while l <= r:
            mid=(l+r)//2
            if nums[mid] < target:
                l = mid+1
            else:
                if nums[mid]== target and nums[mid-1]!=target:
                    return mid
                else:
                    r = mid-1
        return l
        
        
