class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right

        def capacityfind(capacity):
            ships = 1
            curr_capacity = capacity
            for w in weights:
                if curr_capacity - w < 0:
                    ships +=1
                    if ships > days:
                        return False
                    
                    curr_capacity = capacity

                curr_capacity -= w
            return True
        
        while left <= right:
            capacity = (left + right) //2
            if capacityfind(capacity):
                res = min(res,capacity)
                right = capacity-1
            else:
                left = capacity+1

        return res
        

                    