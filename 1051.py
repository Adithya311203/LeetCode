class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=sorted(heights)
        None
        c=0
        for i in range(len(l)):
            if l[i]!=heights[i]:
                c+=1
        return c