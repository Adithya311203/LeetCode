class Solution:
    def maxSatisfied(self, cust: List[int], grumpy: List[int], minutes: int) -> int:
        res = 0
        curr = 0
        
        # initial satisfied customers
        for i in range(len(cust)):
            if grumpy[i] == 0:
                res += cust[i]
        
        # initial additional customers if we use the grumpy technique
        for i in range(minutes):
            if grumpy[i] == 1:
                curr += cust[i]
        
        addi = curr  

        # Slidjng window to maximize additional customers
        for i in range(minutes, len(cust)):
            if grumpy[i - minutes] == 1:
                curr -= cust[i - minutes]  # Remove if grumpy at [i - minutes] 
            if grumpy[i] == 1:
                curr += cust[i]  # Add if grumpy at [i] 

            addi = max(addi, curr)  # Update
        
        return res + addi  # total satisfied customers