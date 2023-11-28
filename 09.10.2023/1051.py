class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h=sorted(heights)
        sum=0
        for i in range(len(heights)):
            if h[i]!=heights[i]:
                sum+=1
        return sum