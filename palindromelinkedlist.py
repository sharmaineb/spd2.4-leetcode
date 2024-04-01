"""
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false
 
Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 
Follow up: Could you do it in O(n) time and O(1) space?
"""

class Solution:
    def isPalindrome(self, head):
        # helper function to reverse a linked list
        def reverse_linked_list(node):
            prev_node = None
            while node:
                next_node = node.next
                node.next = prev_node
                prev_node = node
                node = next_node
            return prev_node
        
        # find the middle of the linked list using the slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the linked list
        reversed_second_half = reverse_linked_list(slow)
        
        # compare the first half with the reversed second half
        while reversed_second_half:
            if head.val != reversed_second_half.val:
                return False
            head = head.next
            reversed_second_half = reversed_second_half.next
        
        return True