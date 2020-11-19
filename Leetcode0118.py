"""
118.杨辉三角
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""


class Solution:
    def generate(self, numRows):
        """

        :param numRows: int
        :return: L
        ist[List[int]]
        """
        if numRows == 1:
            return [[1]]

        triangle = [[1]]

        for i in range(2, numRows + 1):

            row = [None for _ in range(i)]

            row[0] = 1
            row[-1] = 1

            if i == 2:
                triangle.append(row)
            else:
                for j in range(1, len(row) - 2):
                    row[j] = triangle[i - 2][j - 1] + triangle[2 - 1][j]

                triangle.append(row)

        return triangle


solution = Solution()
result = solution.generate(5)
print(result)
