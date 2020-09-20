"""
83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例1:

输入: 1->1->2
输出: 1->2



示例2:

输入: 1->1->2->3->3
输出: 1->2->3


"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head
        else:
            prev = l1 = head

            l1 = l1.next

            while l1:

                # 如果l1结点当前的值与prev结点的值相等
                if l1.val == prev.val:

                    l1 = l1.next

                    prev.next = None
                else:

                    prev.next = l1
                    l1 = l1.next
                    prev = prev.next
        return head

list = [1, 1, 2, 3, 3]
head = ListNode(-1)
prev = head
for item in list:
    prev.next = ListNode(item)
    prev = prev.next

pointer = head.next
solution = Solution()
after_deleted = solution.deleteDuplicates(pointer)
result = []
while after_deleted:
    result.append(after_deleted.val)
    after_deleted = after_deleted.next
print(result)



