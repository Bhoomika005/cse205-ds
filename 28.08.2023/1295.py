class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            j=len(str(i))
            if j%2 ==0:
                n=n+1
        return n