# Reversing a singly linked list:

def reverseSinglyLinkedList(linkedlist):
    previous = None
    current = linkedlist.head

    while current:  # while current != None
        current.next = previous
        previous = current
        current = current.next
        if current.next:  # if current.next != None
            current.next = current.next.next

    linkedlist.head = previous
