from typing import List
#######################################################################################
# A4P1 95. Unique Binary Search Trees II

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution10:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTreesHelper(left, right):
            if left == right:
                return [None]
            nodes = []
            for i in range(left, right):
                for leftC in  generateTreesHelper(left, i):
                    for rightC in generateTreesHelper(i+1, right):
                        node = TreeNode(i+1, leftC, rightC)
                        nodes.append(node)  
            return nodes
        return generateTreesHelper(0, n) if n>0 else []      

#######################################################################################
# A4P2 98. Validate Binary Search Tree

class Solution11:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBSTHelper(cur, min, max):
            if not cur:
                return True
            if cur.val > min and cur.val < max:
                return isValidBSTHelper(cur.left, min , cur.val) and  isValidBSTHelper(cur.right,cur.val,max)
            return False
        return  isValidBSTHelper(root, float('-inf'), float('inf'))

#######################################################################################
# A4P3 240. Search a 2D Matrix II
class Solution12:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: 
            return False
        if len(matrix) == 1 and len(matrix[0])==1:
            return True if  matrix[0][0] == target else False
        
        midY = len(matrix)//2
        midX = len(matrix[0])//2

        tl = self.searchMatrix([row[:midX] for row in matrix[:midY]], target)
        tr = self.searchMatrix([row[:midX] for row in matrix[midY:]], target)
        br = self.searchMatrix([row[midX:] for row in matrix[midY:]], target)
        bl = self.searchMatrix([row[midX:] for row in matrix[:midY]], target)
        return tl or tr or br or bl

if __name__ == '__main__':
    
    print("Unique Binary Search Trees II")
    p10 = Solution10()
    p10.generateTrees(3)

    print("Validate Binary Search Tree")
    tree11 = TreeNode(5,TreeNode(1,None, None), TreeNode(8, TreeNode(6, None, None), TreeNode(10, None, None)))
    p11 = Solution11()
    p11.isValidBST(tree11)

    print("Search a 2D Matrix II")
    matrix12 = [
                [1,   4,  7, 11, 15],
                [2,   5,  8, 12, 19],
                [3,   6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
                ]
    p12 = Solution12()
    print(p12.searchMatrix(matrix12, 20))