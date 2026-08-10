class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):

            # Add the current element to the window
            if nums[right] == 0:
                zeros += 1

            # Too many zeros → shrink from the left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1

                left += 1

            # Current window is valid
            max_length = max(max_length, right - left + 1)

        return max_length

    # left only move when zeros are more than k, and right 
    # always moves forward. The window size is calculated as right - left + 1, 
    # and we keep track of the maximum length of valid windows.