class Solution:
    def largestInteger(self, num: int) -> int:
        num=list(str(num))
        N=len(num)
        even=[False]*N

        for i,x in enumerate(num):
            if int(x)%2==0:
                even[i]=True
        num.sort()
        num.reverse()
        evens=collections.deque()
        odds=collections.deque()
        for x in  num:
            if int(x)%2==0:
                evens.append(x)
            else:
                odds.append(x)
        ans=[]
        for i in range(N):
            if even[i]:
                ans.append(evens.popleft())
            else:
                ans.append(odds.popleft())
        return int("".join(ans))