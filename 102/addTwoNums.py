# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

from node import ListNode

def addTwoNums(l1, l2):
    l1Num = l2Num = ''
    n1, n2 = l1, l2
    while True:
        if n1 is not None:
            l1Num += str(n1.val)

        if n1.next is None:
            break
        else:
            n1 = n1.next


    while True:
        if n2 is not None:
            l2Num += str(n2.val)

        if n2.next is None:
            break
        else:
            n2 = n2.next
    
    sumNum = int(l1Num[::-1]) + int(l2Num[::-1])
    r1 = str(sumNum)[::-1]
    r2 = list(map(lambda x: ListNode(x), r1))
    
    for i in range(len(r1)-1):
        r2[i].next = r2[i+1]

    node = r2[0]
    return node

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

n2 = ListNode(2)
n4 = ListNode(4)
n3 = ListNode(3)
n2.next = n4
n4.next = n3

l5 = ListNode(5)
l6 = ListNode(6)
l4 = ListNode(4)
l5.next = l6
l6.next = l4

r = addTwoNums(n2, l5)

while r is not None:
    print(r.val)
    r = r.next