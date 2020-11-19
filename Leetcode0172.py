"""
172.阶乘后的零
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释:3! = 6, 尾数中没有零。
示例2:

输入: 5
输出: 1
解释:5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为O(logn)。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        res = 1
        while n > 0:
            res *=  n
            n -= 1
        result = 0

        while res > 0 and res % 10 == 0:
            res = res // 10
            result += 1
        return result

solution = Solution()
result = solution.trailingZeroes(3)
print(result)
