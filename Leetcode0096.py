"""
96. 不同的二叉搜索树

给定一个整数 n，求以1 ...n为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


"""
思路: 定义两个函数
G(n): 长度为 nn 的序列能构成的不同二叉搜索树的个数。

F(i,n): 以 i 为根、序列长度为 n 的不同二叉搜索树个数(1≤i≤n)。
"""


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]



solution = Solution()
result = solution.numTrees(3)
print(result)