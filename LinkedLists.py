class NodeInLinkedList:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = NodeInLinkedList(value)
        if self.head:  # if there is at least 1 node in a LL
            current = self.head
            while self.head:  # iterate through all nodes in the LL
                current = current.next
            current.next = node  # putting the new node in the end of the LL
        else:  # if the LL is empty
            node = self.head

    def print(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next



def reverseSinglyLinkedList(linkedList):
    previous = None
    current = linkedList.head

    while current:  # while current != None
        current.next = previous
        previous = current
        current = current.next
        if current.next:  # if current.next != None
            current.next = current.next.next

    linkedList.head = previous


linkedlist = SinglyLinkedList()

linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
print(repr(linkedlist))
linkedlist.print()
reverseSinglyLinkedList(linkedlist)
print(repr(linkedlist))
linkedlist.print()

