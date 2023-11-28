class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res=[]
        row,cols=len(matrix),len(matrix[0])
        left,right=0,cols-1
        top,bottom=0,row-1

        while left <= right and top <= bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left += 1

            '''if not (left < right and top < bottom):
                break

            if i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            if i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left += 1'''

        return res