"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。

示例1:

输入: ["flower","flow","flight"]
输出: "fl"
示例2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母a-z。

"""


"""
注：
python zip()函数

zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。

>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]

"""
class Solution1:
    """
    横向扫描：时间复杂度 O(MN), 空间复杂度为O(1), 额外使用的空间为常数


    LCP(S1, S2, ..., Sn) = LCP(Sn(...LCP(S3, LCP(S1, S2))))
    依次遍历字符串数组中的每个字符串，对于每个遍历到的字符串，更新最长公共前缀，当遍历完所有的字符串以后，即可得到字符串数组中的最长公共前缀。
    """
    def longestCommonPrefix(self, strs):

        # 如果strs是空，直接返回""
         if not strs:
             return ""
         # 取第一个字符串作为起点
         prefix, count = strs[0], len(strs)
         # 遍历字符串并比较
         for i in range(1, count):
             prefix = self.lcp(prefix, strs[i])
             if not prefix:
                 break
         return prefix
    def lcp(self, str1, str2):
        # 取较短字符串为长度，并依次对比每个字符，当index >= length或出现不相同字符串时跳出循环
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1

        return str1[:index]

class Solution2:
    """
    纵向扫描：
    """
    def longestCommonPrefix(self, strs):
        pass

