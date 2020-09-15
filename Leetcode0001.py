"""
1. 两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例：
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""

"""
暴力求解f
"""
class Solution(object):
    def twoSum(self, nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        for index, item in enumerate(nums):
            found_data = []

            now_data = item
            now_index = index
            found_data.append(now_index)
            for i in range(index + 1, len(nums)):
                if nums[i] + now_data == target:
                    found_data.append(i)
                    return found_data
                found_data.clear()


"""
利用字典模拟哈希求解
"""
class Solution1(object):
    def twoSum(self, nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        dict = {}
        for index, item in enumerate(nums):
            dict[item] = index

        for first_num_index, item in enumerate(nums):

            balance = target - item

            second_num_index = dict.get(balance)

            if second_num_index is not None and first_num_index != second_num_index:
               return [first_num_index, second_num_index]





