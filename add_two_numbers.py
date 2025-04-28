# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_list_to_number(ln):
            l = []
            while ln.val is not None:
                l.append(ln.val)
                if ln.next is None:
                    break
                ln = ln.next

            r = l[::-1]
            s = "".join(str(i) for i in r)
            i = int(s)
            return i
        
        i1 = reverse_list_to_number(l1)
        i2 = reverse_list_to_number(l2)

        i3 = i1+i2
        s3 = str(i3)

        l3 = []
        for i in s3:
            l3.append(int(i))

        ln3 = ListNode(l3.pop(0))
        while len(l3) != 0:
            v = l3.pop(0)
            ln3_next = ln3
            ln3 = ListNode(v)
            ln3.next = ln3_next

        return ln3
