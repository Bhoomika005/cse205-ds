class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def go(arr):
            N=len(arr)
            nx=[0]*(N-1)

            for i in range(N-1):
                nx[i]=(arr[i]+arr[i+1])%10
            return nx
        while len(nums)>1:
            nums=go(nums)
        return nums[0]