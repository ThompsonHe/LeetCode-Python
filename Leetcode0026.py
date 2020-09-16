"""
26. 删除排序数组中的重复项

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例1:

给定数组 nums = [1,1,2],

函数应该返回新的长度2, 并且原数组nums的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。




示例2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度5, 并且原数组nums的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。


说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
 print(nums[i]);
}

"""

# 解题思路： 把每串具有相同的数字序列看成一个组 用index_group记录该相同数字的序列的第一个数字的index。
# 用index_real 记录最后要返回的数字序列的长度（删除重复元素后的序列）
# 遍历整个数组，如果当前遍历到的数字与index_group所指的数字相同（也就是说当前数字还是属于一个连续的数字串）则继续
# 如果不同（也就是说当前遍历到的数字不属于前一个连续数字串，属于一个新的数字串）则将当前数字覆盖到index_real的位置上去（相当于为数字新增一个数组）
# index_real 自增到下一个位置为下一个数字做准备。index_group设置为当前的遍历的数字的位置（也是就开始了一个新的数字连续串组）


class Solution:
    def removeDuplicate(self, nums) -> int:

        """
        :param nums: List[int]
        :return: int
        """


        if (len(nums) == 0):
            return 0
        index_real = 1
        index_group = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[index_group]:
                continue
            else:
                nums[index_real] = nums[i]
                index_real += 1
                index_group = i
        return index_real

solution = Solution()
result = solution.removeDuplicate([1, 1, 2])
print(result)

class Solution1:
    def removeDuplicate(self, nums) -> int:
        """
        :param nums: List[int]
        :return: int
        """
        if len(nums) == 0:
            return 0
        index_real = 1
        index_group = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[index_group]:
                continue
            else:
                nums[index_real] = nums[i]
                index_real += 1
                index_group = i
        return index_real

solution = Solution1()
result = solution.removeDuplicate([1, 1, 2])
print(result)


