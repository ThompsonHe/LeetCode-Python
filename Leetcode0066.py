"""
66. 加一

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。


示例2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

"""
class Solution:
    def plusOne(self, digits):
        """
        :param digits: List[int]
        :return: int
        """
        #if len(digits) == 1 and digits[0] == 0:
        #    return 1

        s = 0
        for i in range(len(digits) - 1, -1, -1):

            if i == len(digits) - 1:
                s = digits[i] + 1
            else:
                s += digits[i]
            digits[i] = s % 10
            s = s // 10
            if i == 0 and s != 0:
                digits.insert(0, s)
        return digits




solution = Solution()
result = solution.plusOne([0])
print(result)



