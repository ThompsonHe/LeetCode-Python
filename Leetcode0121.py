"""
121.买卖股票的最佳时机
给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。


示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


"""


class Solution1:
    def maxProfit(self, prices):
        """
        暴力解法
        :param prices: List[int]
        :return: int
        """
        max_val = -10 ** 9
        for i in range(len(prices)):

            now_price = prices[i]

            for j in range(i + 1, len(prices)):

                post_price = prices[j]

                balance = post_price - now_price

                if balance > max_val:
                    max_val = balance
        return max_val


solution = Solution1()

result = solution.maxProfit([7, 1, 5, 3, 6, 4])
print(result)


class Solution2:
    def maxProfit(self, prices):
        """

        :param prices: List[int]
        :return: int
        """
        inf = int(1e9)
        min_price = inf
        max_profit = 0
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit

solution = Solution2()
result = solution.maxProfit([7, 1, 5, 3, 6, 4])
print(result)