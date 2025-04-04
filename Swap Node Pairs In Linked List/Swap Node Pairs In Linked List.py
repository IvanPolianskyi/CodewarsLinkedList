class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    work_el = Node(0)
    work_el.next = head
    prev = work_el

    while head and head.next:
        a = head
        b = head.next

        prev.next = b
        a.next = b.next
        b.next = a

        prev = a
        head = a.next

    return work_el.next
