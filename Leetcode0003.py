"""
3.无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

示例1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def lengthOfLongestSubString(self, s: str) -> int:

        dict = {}
        left_pointer = 0
        right_pointer = 0
        max_len = 0
        now_len = 0

        while left_pointer < len(s) and right_pointer < len(s):

            dict_get = dict.get(s[right_pointer])
            if not dict_get and dict_get != 0:
                dict[s[right_pointer]] = right_pointer
                right_pointer += 1
                now_len += 1
                max_len = max(now_len, max_len)
            else:
                left_temp = left_pointer + 1
                if left_temp < len(s) - 1:
                    left_pointer = left_temp
                    right_pointer = left_pointer
                    dict.clear()
                    now_len = 0
                else:
                    return max_len
        return max_len

solution = Solution()
result = solution.lengthOfLongestSubString("")
print(result)









































