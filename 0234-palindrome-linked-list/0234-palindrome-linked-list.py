# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(prev, head):
            if not head:
                return prev
            tmp = head.next
            head.next = prev
            return reverse(head, tmp)
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = reverse(None, slow)
        
        def check(mid, head):
            if not mid:
                return True
            elif mid.val == head.val:
                return check(mid.next, head.next)
            else:
                return False
        return check(mid, head)
        