class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counts = reduce(lambda x, y: x & y, map(Counter, words))
        return list(common_counts.elements())