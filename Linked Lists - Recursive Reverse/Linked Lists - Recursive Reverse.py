class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverse(head):
    if head is None or head.next is None:
        return head

    work_rest_list = reverse(head.next)

    head.next.next = head
    head.next = None

    return work_rest_list
