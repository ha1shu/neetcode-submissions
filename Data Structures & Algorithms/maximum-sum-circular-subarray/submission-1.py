class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globmax,globmin = nums[0],nums[0]
        currmax,currmin,total = 0,0,0

        for num in nums:
            currmax = max(currmax+num,num)
            currmin = min(currmin+num,num)
            total +=num
            globmax = max(globmax,currmax)
            globmin = min(globmin,currmin)
        
        return max(globmax,total-globmin) if globmax > 0 else globmax
