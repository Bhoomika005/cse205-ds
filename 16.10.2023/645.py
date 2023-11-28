class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rep,mis=None,None
        n=len(nums)

        sumact=sum(nums)
        sumexp=sum([i for i in range(1,n+1)])
        prodact=reduce(mul,nums)
        prodexp=reduce(mul,[i for i in range(1,n+1)])
        mis=round((sumact-sumexp)/((prodact/prodexp)-1))
        rep=(sumact-sumexp)+mis
        return [rep,mis]