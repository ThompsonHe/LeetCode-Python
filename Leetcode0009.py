"""
9.回文数

判断一个整数是否是回文数。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true


示例2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。


示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False
        else:
            num_list = []
            while(x > 0):
                temp = x % 10
                num_list.append(temp)
                x = x // 10
            num_list_len = len(num_list)
            flag = True
            for i in range(num_list_len // 2):
                if num_list[i] != num_list[num_list_len - 1 - i]:
                    flag = False
            if flag == False:
                return False
            else:
                return True

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False
        else:
            num_str = str(x)
            if num_str == num_str[::-1]:
                return True
            else:
                return False











solution1 = Solution1()
result = solution1.isPalindrome(121)
print(result)

solution2 = Solution2()
result = solution2.isPalindrome(121)
print(result)