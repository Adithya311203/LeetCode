class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(heights)):
            d[heights[i]]=names[i]
        c=sorted(d)
        l=[]
        for i in range(len(c)):
            l.append(d[c[i]])
        return l[::-1]