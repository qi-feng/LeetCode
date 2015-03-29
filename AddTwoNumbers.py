# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        current_res = ListNode(l1.val + l2.val)
        forward = 0
        if current_res.val >= 10:
            current_res.val = (current_res.val)%10
            forward = 1
        res = current_res
        l1_cp = l1.next
        l2_cp = l2.next
        while (l1_cp != None) or (l2_cp != None):
            next_res = ListNode(0)
            current_res.next = next_res
            if l1_cp == None:
                next_res.val = l2_cp.val + forward
                l2_cp = l2_cp.next
            elif l2_cp == None:
                next_res.val = l1_cp.val + forward
                l1_cp = l1_cp.next
            else:
                next_res.val = l1_cp.val + l2_cp.val + forward
                l1_cp = l1_cp.next
                l2_cp = l2_cp.next

            if next_res.val >= 10:
                next_res.val = (next_res.val)%10
                forward = 1
            else:
                forward = 0

            current_res = next_res

        if forward == 1:
            next_res = ListNode(forward)
            current_res.next = next_res

        return res

test1 = ListNode(0)
#test1.next = ListNode(4)
#test1.next.next = ListNode(7)
#test1.next.next.next = ListNode(3)

test2 = ListNode(7)
test2.next = ListNode(3)
#test2.next.next = ListNode(4)

sol = Solution()
test = sol.addTwoNumbers(test1, test2)
print test.val, test.next.val #, test.next.next.val, test.next.next.next.val