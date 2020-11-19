"""
125.验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true


示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """

        :param s: str
        :return: bool
        """

        if len(s) == 0:
            return True
        index_front = 0
        index_back = len(s) - 1

        while index_front < index_back:

            while not s[index_front].isalnum() and index_front < len(s) - 1:
                index_front += 1


            front_char = s[index_front]

            while not s[index_back].isalnum() and index_back >= 0:
                index_back -= 1

            back_char = s[index_back]

            if not front_char.lower() == back_char.lower():
                return False
            if not index_back == index_front:
                index_back -= 1
                index_front += 1
        return True


solution = Solution()
result = solution.isPalindrome("，：")
print(result)











