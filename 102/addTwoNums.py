# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

import node

def addTwoNums(l1, l2):
    l1Num = l2Num = ''
    n1, n2 = l1, l2
    while(True):
        l1Num += n1.val
        if l1.next == None:
            break
        else:
            n1 = n1.next


    while(True):
        l2Num += n2.val
        if l2.next == None:
            break
        else:
            n2 = n2.next
    
    sumNum = int(l1Num) + int(l2Num)
    for i in str(sumNum):
        nod = Node(i)

n = Node(1)
print(n.val)