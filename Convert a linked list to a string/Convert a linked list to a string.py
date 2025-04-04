'''Converting a linked list to string'''

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def stringify(node):
    res = ''
    sign = " -> "
    if isinstance(node, Node):
        node_data = node.data
        new_node = node.next
        while node_data != None:
            res += str(node_data) +sign
            if isinstance(new_node,Node):
                node_data = new_node.data
                new_node = new_node.next
            else:
                break
        res +="None"
    else:
        res += "None"
    return res

