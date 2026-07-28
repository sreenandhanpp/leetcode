class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        # Start with the first possible triplet
        res = nums[0] + nums[1] + nums[2]

        n = len(nums)

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # Update if this sum is closer to the target
                if abs(target - total) < abs(target - res):
                    res = total

                # Perfect match
                if total == target:
                    return total

                elif total < target:
                    left += 1

                else:
                    right -= 1

        return res

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
