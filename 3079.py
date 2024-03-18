def encrypt(x):
    l=len(str(x))
    m=max(list(str(x)))
    t=""
    for i in range(l):
        t+=m
    return int(t)
        
        
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            c+=encrypt(i)
        return c
        s