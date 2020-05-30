from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            if not self.current.next:
                self.current.value = item
                self.current = self.storage.head
            else:
                self.current.value = item
                self.current = self.current.next

    def get(self):
        node_arr = []
        current = self.storage.head
        while current:
            node_arr.append(current.value)
            current = current.next
        return node_arr
