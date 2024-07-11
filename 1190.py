class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk=[]
        op=[]
        for i in range(len(s)):
            if s[i]=="(":
                stk.append(s[i])
                op+=[i,]
            elif s[i].isalpha():
                stk.append(s[i])
            else:

                x=("".join(stk)).rfind("(")
                stk[x+1:i+1]=stk[x+1:i+1][::-1]
                stk.pop(x)
        return "".join(stk)