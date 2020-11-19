"""
95. 不同的二叉搜索树
给定一个整数 n，生成所有由 1 ...n 为节点所组成的 二叉搜索树 。



示例：

输入：3
输出：
[
 [1,null,3,2],
 [3,2,null,1],
 [3,1,null,null,2],
 [2,1,3],
 [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

其中： 0 <= n <= 8
"""

"""
二叉查找树（Binary Search Tree），
（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 
 
 
 它的左、右子树也分别为二叉排序树。二叉搜索树作为一种经典的数据结构，它既有链表的快速插入与删除操作的特点，又有数组快速查找的优势；
 所以应用十分广泛，例如在文件系统和数据库系统一般会采用这种数据结构进行高效率的排序与检索操作。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        """

        :param n: int
        :return: List[TreeNode]
        """
        def generateTrees(start, end):
            if start > end:
                return [None, ]
            allTrees  = []

            for i in range(start, end + 1):
                leftTrees = generateTrees(start, i - 1)

                rightTrees = generateTrees(i + 1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            return allTrees




        return generateTrees(1, n) if n else []


