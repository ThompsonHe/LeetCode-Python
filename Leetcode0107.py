"""
107. 二叉树的层次遍历 2

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

"""
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def levelOrderBottom(self, root):
        """

        :param root: TreeNode
        :return: List[List[int]]
        """
        if not root:
            return []

        node_list = []

        queue = collections.deque()

        queue.append(root)

        # 记录当前所处的深度
        depth = 0

        while queue:

            node_list.append([])
            num_nodes_of_layer = len(queue)

            while num_nodes_of_layer:

                 top = queue.popleft()

                 node_list[depth].append(top.val)

                 if  top.left:
                     queue.append(top.left)

                 if  top.right:
                     queue.append(top.right)


                 num_nodes_of_layer -= 1

            depth += 1


        return node_list


# 建树

root = TreeNode(3)
head = root
root.left = TreeNode(9)
root.right = TreeNode(20)
root = root.right
root.left = TreeNode(15)
root.right = TreeNode(7)
solution = Solution1()
result = solution.levelOrderBottom(head)
result = result[::-1]
print(result)

class Solution2:
    def levelOrderBottom(self, root):

        def dfs(root: TreeNode, height: int):
            if root:
                if len(result) <= height:
                    result.insert(0, [])
                result[-height - 1].append(root.val)
                if not root.left and not root.right:
                    return
                dfs(root.left, height + 1)
                dfs(root.right, height + 1)

        result = []
        dfs(root, 0)
        return result




















