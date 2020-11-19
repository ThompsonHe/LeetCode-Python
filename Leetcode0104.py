"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明:叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
"""
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        """
        递归
        :param root: TreeNode
        :return: int
        """
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
        return max(left, right) + 1



class Solution2:
    def maxDepth(self, root: TreeNode) -> int:

        """
        广度优先搜索
        :param root: TreeNode
        :return: int
        """
        if not root:
            return 0

        queue = collections.deque()
        queue.append(root)
        max_depth = 0

        while queue:


            size = len(queue)
            while(size > 0):

                top = queue.popleft()

                if not top.left:
                    queue.append(top.left)

                if not top.right:
                    queue.append(top.right)

                size -= 1
            max_depth += 1

        return max_depth






























