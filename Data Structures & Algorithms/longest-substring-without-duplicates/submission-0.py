class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charaset = set()
        l = 0
        res = 0
        for r in range(0,len(s)):
            while s[r] in charaset:
                charaset.remove(s[l])
                l +=1
            
            charaset.add(s[r])
            res = max(res,r-l+1)

        return res


        
        

