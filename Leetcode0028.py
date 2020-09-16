"""
28. 实现strStr()
实现strStr()函数。

给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2



示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

"""

class Solution1:
    def strStr(self, haystack, needle):
        """
        :param haystack: str
        :param needle: str
        :return: int
        """
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1





