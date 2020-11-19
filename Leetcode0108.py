"""
108. 将有序数组转换成二叉搜索树

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

 
"""
from random import random, randint


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def sortedArrayTOBST(self, nums):
        """
        总是以中间偏左的数字作为根节点

        因为二叉搜索树的中序遍历是升序序列
        题目给定的数字序列也是升序的
        所以可以确保数组是二叉搜索树的中序遍历
        :param nums: List[int]
        :return: TreeNode
        """

        def create(left, right):
            if left > right:
                return None

            # 总是以中间偏左作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = create(left, mid - 1)
            root.right = create(mid + 1, right)
            return root

        return create(0, len(nums) - 1)


class Solution2:
    def sortedArrayTOBST(self, nums):
        """
        总是以中间偏右的数字作为根节点

        因为二叉搜索树的中序遍历是升序序列
        题目给定的数字序列也是升序的
        所以可以确保数组是二叉搜索树的中序遍历
        :param nums: List[int]
        :return: TreeNode
        """

        def create(left, right):
            if left > right:
                return None

            mid = (left + right + 1) // 2

            root = TreeNode(nums[mid])

            root.left = create(left, mid - 1)
            root.right = create(mid + 1, right)

            return root

        return create(0, len(nums) - 1)


class Solution3:
    def sortedArrayTOBST(self, nums):
        """
        任取一个中间位置数字作为根节点

        因为二叉搜索树的中序遍历是升序序列
        题目给定的数字序列也是升序的
        所以可以确保数组是二叉搜索树的中序遍历
        :param nums: List[int]
        :return: TreeNode
        """
        def create(left, right):

            if left > right:
                return

            mid = (left + right + randint(0, 1))

            root = TreeNode(nums[mid])

            root.left = create(left, mid - 1)
            root.right = create(mid + 1, right)
            return root

        return create(0, len(nums) - 1)
