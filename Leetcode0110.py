"""
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回false 。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        自顶向下递归
        :param root: TreeNode
        :return: bool

        最坏情况需要遍历完所有结点 为O(n)

        对于结点p，若其高度为d，则height(p) 最多会被调用d次（遍历到他的每一个祖先结点）

        平均情况，一棵树的高度h满足O(h) = O(logn),因为d <= h所以时间复杂度为O(nlogn)

        对于最坏情况，二叉树形成链式结构，高度为O(n)，此时总时间复杂度为O(n^2)
        """
        def height(root):
            if not root:
                return 0

            return max(height(root.left), height(root.right)) + 1


        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        自底向上递归
        :param root: TreeNode
        :return: bool

        自底向上每个节点,对于每个节点,函数height只会被调用一次
        """
        def height(root: TreeNode) -> int:

            if not root:
                return 0
            left_height = height(root.left)

            right_height = height(root.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1



        return height(root) >= 0




















