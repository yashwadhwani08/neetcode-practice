from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        while True:
            if head in visited_nodes:
                return True
            else:
                visited_nodes.add(head)
            if head is None:
                return False
            head = head.next
    # TC - O(n)
    # SC - O(n) (set created) 

class Solution:
    # Floyd's Tortoise and Hare algorithm (used for detection of cycle) 
    # Floyd's algorithm - Optimised (for space) as no extra space used
    # Basic idea is slow moves by 1 node, fast by 2, if cycle in picture, slow
    # will be equal to fast
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    # TC - O(n)
    # SC - O(1) (No extra space used)
    
# URL - https://neetcode.io/problems/linked-list-cycle-detection
