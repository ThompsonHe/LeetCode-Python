"""
167.两数之和 II - 输入有序数组
给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1必须小于index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def twoSum(self, numbers, target):
        """

        :param numbers: List[int]
        :param targer: int
        :return: int
        """

        if len(numbers) == 0 or len(numbers) == 1 and numbers[0] != target:
            return []

        dict = {}

        for index, number in enumerate(numbers):


            balance = target - number

            dict_get = dict.get(balance)

            if not dict_get:
                dict[number] = (balance, index)
            elif dict_get[0] == number:
                return [dict[balance][1] + 1, index + 1]

solution = Solution()
res = solution.twoSum([2, 4, 7, 11, 15], 9)
print(res)







        