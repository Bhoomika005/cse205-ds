class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff=arr[-1]-arr[0]
        res=[]
        for i in range(len(arr)-1):
            min_diff=min(min_diff,arr[i+1]-arr[i])
        for i in range(len(arr)):
            if (arr[i]-arr[i-1]==min_diff):
                res.append([arr[i-1],arr[i]])
        return res