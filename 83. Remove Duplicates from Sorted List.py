# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #currentNode = head
        # while(currentNode):
        #     if(currentNode.next != None):
        #         nextNode = currentNode.next
        #         print(nextNode.val)
        #         if (nextNode.val == currentNode.val):
        #             currentNode.next  = nextNode.next
        #             currentNode = nextNode.next
        #             if(currentNode.next == None):
        #                 if(currentNode.val == )
        #         else:
        #             currentNode = currentNode.next
                    
        #     else:
        #         break
        # return head
        currentNode = head

        while currentNode and currentNode.next:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return head

    
