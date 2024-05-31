class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        keys=list(d.keys())
        l=[]
        values=list(d.values())
        for i in range(len(keys)):
            if values[i]==1:
                l.append(keys[i])

        return l