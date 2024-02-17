# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        mem = 0
        temp = 0
        signal = 1
        while(l1 or l2):
            temp+=mem
            mem = 0
            if(l1 and l2 and signal == 1):
                temp += l1.val + l2.val
                mem = temp // 10
                temp = temp % 10
                l1.val = temp
                if(l1.next == None):
                    signal = 0
                    if(l2.next == None and mem > 0):
                        l1.next = ListNode(val = mem)
                        break
                    l2 = l2.next
                    l1.next = l2
                    l1 = l1.next
                elif(l2.next == None):
                    signal = 0
                    l1 = l1.next
                    l2.next = l1
                    l2 = l2.next
                else:
                    l1 = l1.next
                    l2 = l2.next

            elif(signal == 0 ):
                l1.val += temp
                mem = l1.val // 10
                l1.val = l1.val % 10
                if(l1.next == None and mem != 0):
                    l1.next = ListNode(val = mem)
                    break
                l1 = l1.next
                l2 = l2.next
            temp = 0



        return head

