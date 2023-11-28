# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur=root
        prev=TreeNode(float("-inf"))
        replace=[]
        stack=[]
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            temp=stack.pop()
            if temp.val<prev.val:
                replace.append((prev,temp))
            prev=temp
            cur=temp.right
        replace[0][0].val,replace[-1][1].val = replace[-1][1].val,replace[0][0].val