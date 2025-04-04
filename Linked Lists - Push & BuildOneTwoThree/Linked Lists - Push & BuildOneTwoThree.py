class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
def push(head, data):
    a = Node(data)
    a.next = head    
    return a

def build_one_two_three():
    el = 0
    counter = 4
    for _ in range(4):
        if el == 0:
            el  = None
        else:
            counter -=1
            el = push(el,counter)
    return el
