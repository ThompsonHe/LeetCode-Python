"""
136.只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1

示例2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import reduce


class Solution1:
    def singleNumber(self, nums):
        """
        哈希表法
        :param nums: List[int]
        :return: int
        """
        dict = {}

        for num in nums:
            if not dict.get(num):
                dict[num] = 1
            else:
                dict[num] += 1
        for key in dict:
            if dict[key] == 1:
                return key

solution  = Solution1()
result = solution.singleNumber([2, 2, 1])
print(result)

class Solution2:
    def singleNumber(self, nums):
        """
        位运算法：
        线性时间复杂度
        不使用额外的空间


        异或运算有以下三个性质。

        任何数和 0 做异或运算，结果仍然是原来的数，即：a XOR 0 = a
        任何数和其自身做异或运算，结果是0, 即：a XOR a = 0
        异或运算满足交换律和结合律，即 a XOR b XOR a = b XOR a XOR a = b XOR (a XOR a) = b XOR 0 = b

        假设数组中有 2m+1 个数，其中有 m 个数各出现两次，一个数出现一次。
        令a1, a2, ..., am为出现两次的m个数， am+1为出现一次的数。
        有(a1 XOR a1) XOR (a2 XOR a2) ...(am XOR am) XOR am+1 = am+1

        :param nums: List[int]
        :return: int
        """

        if len(nums) == 1:
            return nums[0]

        result = nums[0]

        for i in range(1, len(nums)):
            result = result ^ nums[i]

        return result

solution = Solution2()
result = solution.singleNumber([2, 2, 1])
print(result)



class Solution3:
    def singleNumber(self, nums):
        """
        同样也是位运算法，采用reduce()函数进行计算

        reduce() 函数会对参数序列中元素进行累积。
        函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
        用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
        得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

        语法
        reduce() 函数语法：
        reduce(function, iterable[, initializer])

        参数
        function -- 函数，有两个参数
        iterable -- 可迭代对象
        initializer -- 可选，初始参数

        返回值
        返回函数计算结果。

        实例
        以下实例展示了 reduce() 的使用方法：
        def add(x, y) :            # 两数相加
            return x + y

        reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
        15
        reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
        15

        :param nums: List[int]
        :return: int
        """
        return reduce(lambda x, y: x ^ y, nums)

solution  = Solution3()
result = solution.singleNumber([2, 2, 1])
print(result)






