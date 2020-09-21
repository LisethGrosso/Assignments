#######################################################################################
# A3P1. Maximum Depth of Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution7:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if type(root) == int:
            return 1
        else: 
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

#######################################################################################
# A3P2. Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printList(self):
        node = self
        while node is not None:
            print(node.val)
            node = node.next 
class Solution8:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergeListHead = ListNode()
        mergeList = mergeListHead
        while(l1 and l2):
            if(l1.val < l2.val):
                mergeList.next= l1
                l1 = l1.next
            else:
                mergeList.next = l2
                l2 = l2.next
            mergeList = mergeList.next
        if(l1 is not None):
            mergeList.next = l1
        if(l2 is not None):
            mergeList.next = l2
        return mergeListHead.next

#######################################################################################
# A2P3. K-th Symbol in Grammar
class Solution9:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1 or K==1:
            return 0
        else:
            mid = (2**(N-1))//2
            if K <= mid:
                return self.kthGrammar(N-1, K)
            else:
                return 1- self.kthGrammar(N-1, K-mid)
        
if __name__ == '__main__':

    print("Maximum Depth of Binary Tree")
    p7 = Solution7()
    p7 = p7.maxDepth(TreeNode(3, TreeNode(9,None, None), TreeNode(20, 15, 7)))
    print(p7)
 
    print("Merge Two Sorted Lists")
    p8 = Solution8()
    p8 = p8.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4, None))), ListNode(1, ListNode(3, ListNode(4, None))))
    p8.printList()

    print("K-th Symbol in Grammar")
    p9 = Solution9()
    print(p9.kthGrammar(4,3))
    
