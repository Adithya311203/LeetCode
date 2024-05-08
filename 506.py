class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x=sorted(score,reverse=True)
        if len(x)<=3:
            x1=x
            x2=[]
        else:
            x1=x[:3]
            x2=x[3:]
        d={}
        l=[]
        awards=["Gold Medal","Silver Medal","Bronze Medal"]
        for i in range(len(x1)):
            d[x1[i]]=awards[i]
        for i in range(len(x2)):
            d[x2[i]]=str(i+4)
        print(d)
        for i in score:
            l.append(d[i])
        return l
