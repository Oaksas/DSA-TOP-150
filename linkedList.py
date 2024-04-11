class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.tail is not None:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def getAll(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next


linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
print(linkedList.search(1))
linkedList.getAll()
