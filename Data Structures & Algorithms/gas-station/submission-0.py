class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        res = 0
        total = 0
        
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(0,len(gas)-1):
            total += gas[i]-cost[i]

            if total <0:
                total = 0
                res = i+1

        return res