class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(list(s))
        c_list=sorted(c,key=lambda x:c[x],reverse=True)
        output=[]
        for char in c_list:
            output.append(char*c[char])

        return ''.join(output)