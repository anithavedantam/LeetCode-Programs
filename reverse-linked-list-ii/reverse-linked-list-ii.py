# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(next=head)
        prev = dummy
        curr = head
        k = 0
        while curr:
            k += 1
            if left <= k < right:
                next_node = curr.next
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
            else:
                if k < right:
                    prev = prev.next
                curr = curr.next
            
        return dummy.next