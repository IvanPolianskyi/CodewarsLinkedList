class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def loop_size(node):
    next_1, next_2 = node, node
    

    while next_2 and next_2.next:
        next_1 = next_1.next
        next_2 = next_2.next.next
        if next_1 == next_2:
            break
    else:
        return 0 

    res = 1
    current = next_1.next
    while current != next_1:
        res += 1
        current = current.next
    
    return res
