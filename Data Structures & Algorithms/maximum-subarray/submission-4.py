class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        currSum = 0
        totalSum = nums[0]

        for num in nums:
           
            if currSum < 0:
                currSum = 0
            currSum += num
            totalSum = max(currSum,totalSum)

        return totalSum