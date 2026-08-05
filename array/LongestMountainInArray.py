class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i , count, max_count = 0,1,0
        mountain = False

        n = len(arr)

        while i < n :
            mountain = False
            while i + 1 < n and arr[i] < arr[i+1]:
                count+=1
                i+=1
            
            if count > 1:
                while i + 1 < n and arr[i] > arr[i+1]:
                    count+=1
                    i+=1
                    mountain = True
            else:
                i+=1
            
            if mountain:
                max_count = max(max_count,count)
            
            count = 1
            
        return(max_count)

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.