class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] < k:
                count+=1
            sm= nums[i]
        
            for j in range(i+1,n):
                if i == 0 and i == n-1:
                    break
                    
                sm = sm * nums[j]
                print("sm",sm)
                if sm < k:
                    count+=1
            print("c",count)
        return(count)