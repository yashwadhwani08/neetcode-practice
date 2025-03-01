from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = None
            prev = curr
            curr = temp
        return prev
    
    # TC - O(n)
    # SC - O(1)
    
class Solution2:        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
    
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)  # Recursive call
            head.next.next = head  # Reverse the link
        head.next = None  # Break the original link
        # print(new_head.val)  # Print the value of the new head
        return new_head  # Return the new head
    
    # TC - O(n)
    # SC - O(n) due to recursion stack


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)

list = Solution2()
reversed_ll = list.reverseList(head)

# URL - https://neetcode.io/problems/reverse-a-linked-list
