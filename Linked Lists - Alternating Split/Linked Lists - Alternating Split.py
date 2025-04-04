class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Context:
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError

    work_el1 = Node(0)
    work_el2 = Node(0)
    el1, el2 = work_el1, work_el2

    current = head
    Flag = True

    while current:
        if Flag:
            el1.next = current
            el1 = el1.next
        else:
            el2.next = current
            el2 = el2.next
        current = current.next
        Flag = not Flag

    el1.next = None
    el2.next = None

    return Context(work_el1.next, work_el2.next)
