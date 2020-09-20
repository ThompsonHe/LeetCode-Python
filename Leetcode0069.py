"""
69. x 的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2

示例 2:

输入: 8
输出: 2

说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

"""
import math


class Solution1:
    def mySqrt(self, x: int) -> int:
        """
        袖珍计算器法
        我们将 sqrt{x}，写成幂的形式 x^{1/2}
        再使用自然对数e进行换底，即可得到

        sqrt{x} = x ^ {1/2} = e ^ {1/2 * ln x}
        :param x:
        :return:
        """

        if x == 0:
            return 0

        else:
            result = math.exp(0.5 * math.log(x))
        return int(result // 1)


solution = Solution1()
result = solution.mySqrt(8)
print(result)



class Solution2:
    def mySqrt(self, x: int) -> int:

        left, right, ans = 0, x, -1

        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

solution = Solution2()
result = solution.mySqrt(8)
print(result)



class Solution3:
    def mySqrt(self, x: int) -> int:
        pass











