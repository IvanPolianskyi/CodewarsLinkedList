'''Parse a linked list from a string'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    if s == "None":
        return None
    work_list = s.split(' -> ')
    work_list = list(reversed(work_list))
    work_el = None
    for _, val in enumerate(work_list):
        if val != "None":

            work_el = Node(int(val), work_el)
    return work_el
