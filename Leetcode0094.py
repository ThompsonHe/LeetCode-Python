"""
94. 二叉树的中序遍历

给定一个二叉树，返回它的中序遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def inorderTraversal(self, root):
        """
        采用递归方法实现 中序遍历
        :param root: TreeNode
        :return: List[int]
        """

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        ans = []
        inorder(root)
        return ans

    def preorderTraversal(self, root):
        """
        采用递归方法实现 先序遍历
        :param root: TreeNode
        :return: List[int]
        """

        def preorder(root):
            if not root:
                return
            ans.append(root)
            preorder(root.left)
            preorder(root.right)

        ans = []
        preorder(root)
        return ans

    def postorderTraversal(self, root):
        """
        采用递归方法
        :param root: TreeNode
        :return: List[int]
        """

        def postorder(root):
            if not root:
                return

            postorder(root.left)
            postorder(root.right)
            ans.append(root)



        ans = []
        postorder(root)
        return ans


class Solution2:
    def inorderTraversal(self, root):
        """
        用迭代的方法实现
        :param root: TreeNode
        :return: List[int]
        """
        ans = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                ans.append(tmp.val)
                root = root.right
        return ans
