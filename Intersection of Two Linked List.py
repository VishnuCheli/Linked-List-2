#Time Complexity:: O(m+n)-all nodes in both linked list are visited more than once
#Space Complexity:: O(1)-no extra space used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #edge case
        if headA == None or headB == None:
            return None
        
        lenA = 0 #length of linked list A
        lenB = 0 #length of linked list B
        
        pa = headA
        pb = headB
        
        while pa!=None: #till pa reaches end of linked list A
            lenA += 1 #length count increments for linked list A
            pa = pa.next
            
        while pb!=None:  #till pa reaches end of linked list B
            lenB += 1 #length count increments for linked list B
            pb = pb.next
            
        pa = headA
        pb = headB
        
        while lenA > lenB: #if linked list A is longer
            pa = pa.next #move pa till it's at same index away from intersection as pb
            lenA -=1 
            
        while lenB > lenA: #if linked list B is longer
            pb = pb.next #move pb till it's at same index away from intersection as pa
            lenB -=1
            
        while pa!=pb: #both pointer nodes are equal distance away from intersection 
            pa = pa.next #move both linked list pointers simultanesouly till they hit
            pb = pb.next #the intersection
            
        return pa