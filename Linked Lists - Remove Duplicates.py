class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current_node = head
    while current_node and current_node.next:
        if current_node.data == current_node.next.data:

            current_node.next = current_node.next.next
        else:

            current_node = current_node.next
    return head