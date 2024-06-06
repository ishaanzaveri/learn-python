class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# If p1 < p2 insert p1 and increment p1 else insert p2 and increment p2 and you loop this 
class Solution:
    # def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
    #     runner1 = list1
    #     runner2 = list2
    #     resultList = None
    #     currentNode = None
    #     if runner1 is None and runner2 is None:
    #         return currentNode
    #     elif runner1 is None:
    #         return list2
    #     elif runner2 is None:
    #         return list1
    #     while runner1 is not None or runner2 is not None:
    #         if runner1 is None:
    #             currentNode.next = runner2
    #             break
    #         if runner2 is None: 
    #             currentNode.next = runner1
    #             break
    #         if runner1.val < runner2.val:
    #             if resultList is None:
    #                 resultList = runner1
    #                 currentNode = runner1
    #                 runner1 = runner1.next
    #             else: 
    #                 currentNode.next = runner1
    #                 currentNode = currentNode.next
    #                 if runner1.next is None and runner2 is not None:
    #                     currentNode.next = runner2
    #                     break
    #                 runner1 = runner1.next

    #         else:
    #             if resultList is None:
    #                 resultList = runner2
    #                 currentNode = runner2
    #                 runner2 = runner2.next
    #             else: 
    #                 currentNode.next = runner2
    #                 currentNode = currentNode.next
    #                 if runner2.next is None and runner1 is not None:
    #                     print("Here")
    #                     currentNode.next = runner1
    #                     break
    #                 runner2 = runner2.next
    #         #currentNode = currentNode.next
    #         # print(f"{runner1.val}:{runner2.val}:{currentNode.val}" )
    #     return resultList
    
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        r1 = list1
        r2 = list2
        curr = None
        res = None 
        
        if r1 is None:
            return list2
        elif r2 is None:
            return r1
        elif r1.val < r2.val:
            res = r1
            curr = r1
            r1 = r1.next
        else:
            res = r2
            curr = r2
            r2 = r2.next
            
        while r1 is not None and r2 is not None:
            if r1.val < r2.val:
                curr.next = r1
                curr = curr.next 
                r1 = r1.next 
            else:
                curr.next = r2
                curr = curr.next
                r2 = r2.next
        
        if r1 is None and r2 is not None:
            curr.next = r2

        if r2 is None and r1 is not None:
            curr.next = r1
        return res
        
        
    def printList(res:[ListNode]):
        print (res.val)
        res = res.next

def main():
    l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    l2 = ListNode(1, ListNode(3, ListNode(4, None)))
    # l1 = ListNode(1)
    # l2 = ListNode(2)
    
    res = Solution.mergeTwoLists(None, l1,l2) 
    print("++++++")
    while res is not None:
        print (res.val)
        res = res.next

if __name__ == "__main__":
    main()