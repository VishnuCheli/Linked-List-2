#Time Complexity:: O(n)-all nodes are visited and some are traversed multiple times
#Space Complexity:: O(1)-no extra space used as everything is inplace
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        mid = self.findMid(head) #finding the mid to split
        mid_next = mid.next #mid next is stored as the linkedlist from there has to be reversed
        mid.next = None #cutting head node and pointing last node to null
        
        headB = self.reverse(mid_next) #reversing half of the original linked list
        
        headA = head #original head is headA
        
        self.mergeLinkedList(headA,headB) #head A and reversed linkedlist headB to be merged
        
    def findMid(self,head):
        slow = head
        fast = head
        
        while fast.next!= None and fast.next.next!=None: #makes sure that fast stops before hitting null, with odd and even sized linked lists
            slow = slow.next 
            fast = fast.next.next #moves 2 nodes at a time
        return slow #slow stops exactly in the middle when fast reaches end
    
    def reverse(self,head):
        prev = None #head node should point to prev so initially null
        curr = head #starting curr node at head
        
        while curr != None: #code to reverse the linked list inplace
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev # returning prev as curr would have reached null and prev is the new head
    
    def mergeLinkedList(self,head1,head2):
        ptr1 = head1
        ptr2 = head2
        
        while ptr2!=None:
            temp = ptr1.next #creating temp ptr that points to next node of ptr1
            ptr1.next = ptr2 #merging head1 node with head2 node
            ptr2 = ptr2.next #moving ptr2 to next node in head2
            ptr1.next.next = temp #traversing through the merged node and connecting to temp in head1
            ptr1 = temp #moving ptr to next node in head1