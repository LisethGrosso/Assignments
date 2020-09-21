
#######################################################################################
# A2P1. Search in a Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution4:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if (root == None or root.val == val) :
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)

#######################################################################################
# A2P2. Pascal's Triangle II
class Solution5:
    def getRow(self, rowIndex: int):
        row=[]
        row.append(1)
        for i in range(rowIndex):
            for j in range(len(row)-1, 0, -1):
                row[j] = row[j-1] + row[j]
            row.append(1)
        return row

#######################################################################################
# A2P3 70. Climbing Stairs
class Solution6:
    steps={1:1, 2:2, 3:3}
    def climbStairs(self, n: int) -> int:
        if n in self.steps.keys():
            return self.steps[n]
        else:
            self.steps[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.steps[n]

if __name__ == '__main__':
    
    print("Search in a Binary Search Tree")
    p4 = Solution4()
    p4 = p4.searchBST(TreeNode(4, TreeNode(2, 1, 3), 7), 2)
    print(p4.val)
    
    print("Pascal's Triangle II")
    p5 = Solution5()
    print(p5.getRow(3))
    
    print("Climbing Stairs")
    p6 = Solution6()
    print(p6.climbStairs(5))