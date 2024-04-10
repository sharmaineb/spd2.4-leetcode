"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 
Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        # initialize pointers
        # pointer to the previous node (initially None)
        prev = None
        # pointer to the current node
        curr = head
        
        # traverse the linked list
        while curr:
            # store the next node
            next_node = curr.next
            # reverse
            curr.next = prev 
            
            # move pointers forward
            prev = curr
            curr = next_node
        
        # return the new head of the reversed list
        return prev
