class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=word.find(ch)
        print(a)
        x=word[:a+1][::-1]
        return x+word[a+1:]