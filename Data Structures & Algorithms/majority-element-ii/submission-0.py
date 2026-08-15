class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1

        
        result = []
            
        for key,value in freq.items():
            if value > n/3:
                result.append(key)
            
        
        return result