# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tempList1 = ListNode()
        tempList2 = tempList1 

        while list1 and list2:
            if list2.val > list1.val:
                tempList1.next = list1
                list1 = list1.next
            else:
                tempList1.next = list2
                list2 = list2.next
            tempList1 = tempList1.next

        if list2:
            tempList1.next = list2
        else:
            tempList1.next = list1

        return tempList2.next
