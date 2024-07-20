class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        d={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in d:
                    
                    d[j].append(matrix[i][j])
                else:
                    d[j]=list([matrix[i][j],])
        x=[]
        for i in matrix:
            x.append(min(i))
        y=[]
        for i in list(d.values()):
            y.append(max(i))
        final=[]
        for i in x:
            if i in y:
                final.append(i)
        return final