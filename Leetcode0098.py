"""
98.验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


示例1:

输入:
    2
   / \
  1   3
输出: true

示例2:

输入:
    5
   / \
  1   4
     / \
  3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
    根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        递归
        :param root:
        :return:

        要解决这道题首先我们要了解二叉搜索树有什么性质可以给我们利用，由题目给出的信息我们可以知道：
        如果该二叉树的左子树不为空，则左子树上所有节点的值均小于它的根节点的值；
        若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；它的左右子树也为二叉搜索树。
        这启示我们设计一个递归函数 helper(root, lower, upper) 来递归判断，函数表示考虑以 root 为根的子树，
        判断子树中所有节点的值是否都在 (l,r)(l,r) 的范围内（注意是开区间）。
        如果 root 节点的值 val 不在 (l,r)(l,r) 的范围内说明不满足条件直接返回，
        否则我们要继续递归调用检查它的左右子树是否满足，如果都满足才说明这是一棵二叉搜索树。
        那么根据二叉搜索树的性质，在递归调用左子树时，我们需要把上界 upper 改为 root.val，
        即调用 helper(root.left, lower, root.val)，因为左子树里所有节点的值均小于它的根节点的值。
        同理递归调用右子树时，我们需要把下界 lower 改为 root.val，即调用 helper(root.right, root.val, upper)。

        函数递归调用的入口为 helper(root, -inf, +inf)， inf 表示一个无穷大的值。
        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):

            if not node:
                return True

            val = node.val

            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False

            if not helper(node.left, lower, val):
                return False

            return True

        return helper(root)


class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        二叉搜索树「中序遍历」得到的值构成的序列一定是升序的，这启示我们在中序遍历的时候实时检查当前节点的值是否大于前一个中序遍历到的节点的值即可。
        如果均大于说明这个序列是升序的，整棵树是二叉搜索树，否则不是，下面的代码我们使用栈来模拟中序遍历的过程。

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        :param root:
        :return:
        """


class Solution2:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

