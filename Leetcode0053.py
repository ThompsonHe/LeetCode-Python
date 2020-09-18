"""
53. 最大子序和
定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:连续子数组[4,-1,2,1] 的和最大，为6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""
class Solution1:
    def maxSubArray(self, nums):
        """
        BF 时间复杂度O(n) 空间复杂度O(1)
        :param nums: List[int]
        :return: int
        """
        max = - 1000
        for i in range(len(nums) - 4):
            now_sum = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
            if now_sum > max:
                max = now_sum
        return max

solution = Solution1()
result = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)


class Solution2:
    def maxSubArray(self, nums):
        """
        二分法
        :param nums: List[int]
        :return: int
        """
        n = len(nums)

        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[:n //2])

            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[n // 2 : n])

        # 计算中间的最大子序和
        max_l = nums[n // 2 - 1]
        tmp = 0
        for i in range(n // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)

        max_r = nums[n // 2]
        tmp = 0

        for i in range(n // 2, n):
            tmp += nums[i]
            max_r = max(tmp, max_r)

        return max(max_right, max_left, max_r + max_l)

solution = Solution2()
result = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)




class Solution3:
    def maxSubArray(self, nums):
        """
        分治
        :param nums: List[int]
        :return: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[: n // 2])
            max_right = self.maxSubArray(nums[n // 2 :])

        # 开始查找中间序列的最大值
        temp = 0
        max_l = nums[n // 2 - 1]
        for i in range(n // 2 - 1, -1 , -1):
            temp += nums[i]
            max_l = max(max_l, temp)

        temp = 0
        max_r = nums[n // 2]
        for i in range(n // 2, n):
            temp += nums[i]
            max_r = max(max_r, temp)

        return max(max_right, max_left, (max_r + max_l))
