"""
67. 二进制求和


给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字1和0。



示例1:

输入: a = "11", b = "1"
输出: "100"


示例2:

输入: a = "1010", b = "1011"
输出: "10101"

提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if not a:
            return b
        elif not b:
            return a

        min_length = min(len(a), len(b))

        for i in range(min_length - 1, -1, -1):

            if a[i] == "1" 

