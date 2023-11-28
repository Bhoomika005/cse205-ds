class Solution:
    def customSortString(self, order: str, s: str) -> str:
        lk=defaultdict(int)
        i=0
        for c in order:
            lk[c]=i
            i+=1
        return "".join(sorted(s,key=lambda x:lk.get(x,100)))