# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        b=head
        while b is not None and b.next is not None:
            a=a.next
            b=b.next.next
        return a