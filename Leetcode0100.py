"""
100. 相同的树

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false


"""
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        深度优先搜索
        1. 如果两个二叉树都为空，则两个二叉树相同。

        2. 如果两个二叉树中有且只有一个为空，则两个二叉树一定不相同。

        3. 如果两个二叉树都不为空，那么首先判断它们的根节点的值是否相同，若不相同则两个二叉树一定不同，
        若相同，再分别判断两个二叉树的左子树是否相同以及右子树是否相同。
        这是一个递归的过程，因此可以使用深度优先搜索，递归地判断两个二叉树是否相同。


        :param p: TreeNode
        :param q: TreeNode
        :return: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)


class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        广度优先搜索

        初始时将两个二叉树的根节点分别加入两个队列。每次从两个队列各取出一个节点，进行如下比较操作。

        1. 比较两个节点的值，如果两个节点的值不相同则两个二叉树一定不同；

        2. 如果两个节点的值相同，则判断两个节点的子节点是否为空，如果只有一个节点的左子节点为空，
        或者只有一个节点的右子节点为空，则两个二叉树的结构不同，因此两个二叉树一定不同；

        3. 如果两个节点的子节点的结构相同，则将两个节点的非空子节点分别加入两个队列，子节点加入队列时需要注意顺序，
        如果左右子节点都不为空，则先加入左子节点，后加入右子节点。

        4. 如果搜索结束时两个队列同时为空，则两个二叉树相同。如果只有一个队列为空，则两个二叉树的结构不同，因此两个二叉树不同。

        :param p: TreeNode
        :param q: TreeNode
        :return: bool
        """

        if not p and not q:
            return True
        elif not p or not q:
            return False

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2): # ^ 为XOR符号：同号得正（0） 异号得负（1）
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2


















