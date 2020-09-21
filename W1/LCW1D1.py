
from typing import List

#######################################################################################
# A1P1 Reverse String

class Solution1:
    def reverseString(self, s: List[str]) -> None:
        #s[:]= s[::-1]    
        s= s[::-1]            

#######################################################################################
# A1P2 Swap Nodes in Paris

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printList(self):
        node = self
        while node is not None:
            print(node.val)
            node = node.next 
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None : 
            return head
        if head.next==None:
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp

#######################################################################################
# A1P3 Reverse Linked List

class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:

        def recursiveListHelp(cur , prev):
            if not cur:
                return prev
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
            return recursiveListHelp(cur, prev)

        return recursiveListHelp(cur = head, prev= None)

if __name__ == '__main__':

    print("Reverse String")
    listN1 = '["h","e","l","l","o"]'
    p1 = Solution1()
    p1.reverseString(listN1)

    print("Swap Nodes in Paris")
    listN2 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5, None)))))
    p2 = Solution2()
    p2.swapPairs(listN2).printList()

    print("Reverse Linked List")
    listN3 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5, None)))))
    p3 = Solution3()
    p3.reverseList(listN3).printList()