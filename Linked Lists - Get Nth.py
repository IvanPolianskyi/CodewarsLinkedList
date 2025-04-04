class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    if not isinstance(node, Node) or index < 0:
        raise Exception("Invalid input")

    current = node
    count = 0

    while current:
        if count == index:
            return current
        current = current.next
        count += 1

    raise Exception("Index out of range")
