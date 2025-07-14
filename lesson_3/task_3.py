class ListNode:
    def __init__(self, value: int = None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert(self, position: int, value: int):
        new_node = ListNode(value)
        current_position = 0
        current_node = self.head
        while current_position < position - 1 and current_node.next:
            current_node = current_node.next
            current_position += 1
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, value: int):
        current_node = self.head
        if current_node.value == value:
            self.head = current_node.next
            return

        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


    def get(self, index: int) -> int:
        current_node = self.head
        current_index = 0

        while current_node:
            if current_index == index:
                return current_node.value
            current_node = current_node.next
            current_index += 1


def merge_sorted_list(l1: ListNode, l2: ListNode) -> ListNode:
    result_node_dummy = ListNode()
    result_node_tail = result_node_dummy
    while l1 and l2:
        if l1.value < l2.value:
            result_node_tail.next = l1
            l1 = l1.next
        else:
            result_node_tail.next = l2
            l2 = l2.next
        result_node_tail = result_node_tail.next
    result_node_tail.next = l1 if l1 else l2
    return result_node_dummy.next

def swap_elements(node: ListNode) -> ListNode:
    prev = ListNode()
    cursor = node
    head_modified = None

    while cursor and cursor.next:

        node1 = cursor
        node2 = cursor.next
        next_pair = node2.next

        if not head_modified:
            head_modified = node2

        prev.next = node2
        node1.next = next_pair
        node2.next = node1

        prev = node1
        cursor = next_pair

    return head_modified
    # while head_modified:
    #     print(head_modified.value)
    #     head_modified = head_modified.next


list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
# list1.append(6)

head = list1.head
# while head:
#     print(head.value, end=' -> ')
#     head = head.next

swap_elements(head)
# while head:
#     print(head.value, end=' -> ')
#     head = head.next