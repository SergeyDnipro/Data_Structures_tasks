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

# def remove_elements(head: ListNode, val: int) -> ListNode | None:
#     if not head:
#         return head
#     new_head = head
#     new_tail = head
#     if new_head.value == val:
#         new_head = new_head.next
#         return new_head
#     else:
#         remove_elements(new_tail.next, val)

def remove_elements(head: ListNode, val: int) -> ListNode | None:
    if not head:
        return None

    # Recursively process the rest of the list
    head.next = remove_elements(head.next, val)

    # Decide whether to keep the current node
    if head.value == val:
        return head.next
    else:
        return head


list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(2)
list1.append(4)
list1.append(6)

result = remove_elements(list1.head, 2)
while result:
    print(result.value)
    result = result.next