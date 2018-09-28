# 面试题5：从头到尾打印链表
class Node(object):

    def __init__(self, value, nextNode):
        self.val = value
        self.next = nextNode


def printListReversing(pHead):
    if pHead == None:
        return False

    valueContainer = []

    while pHead.next != None:
        value = pHead.val
        valueContainer.append(value)
        pHead = pHead.next

    valueContainer.append(pHead.val)

    return valueContainer

if __name__=="__main__":


    pHead = Node(1, None)
    node1 = Node(3, None)
    node2 = Node(13, None)
    node3 = Node(55, None)
    node4 = Node(16, None)
    pHead.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    result = printListReversing(pHead)
    reversedResult = list(reversed(result))

    print(reversedResult)

