class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        end ,start,flag = -1,-1,0
        if len(nums) == 0:
            return(-1,-1)
        for i in range(0,len(nums)):
            if nums[i] == target:
                flag +=1
                if(flag == 1):
                    start = i
                end = i
        
        return start,end


# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.