class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if (n==1):
            return 2
        result= []
        i=1
        while(n>=i):
            result.append(n*i)
            i+=1
        for i in range(len(result)):
            if result[i] % 2==0:
                return result[i]