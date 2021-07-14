class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node (data={self.data} link=<{self.next.data if self.next is not None else None}>)'


class MyList:

    def __init__(self):
        self.first = None

    def add(self, node):

        if self.first is None:
            self.first = node
            return

        current = self.first

        while current.next is not None:
            current = current.next

        current.next = node

    def print_reversed(self, pointer=None):

        if pointer is None:
            pointer = self.first

        print(pointer)

        if pointer.next is None:
            print(pointer)
            return

        self.print_reversed(pointer.next)
        print(pointer)


n1 = Node('1')
n2 = Node('2')
n3 = Node('3')

lst = MyList()
lst.add(n1)
lst.add(n2)
lst.add(n3)
lst.add(Node('4'))
lst.add(Node('dfdffd'))
print(lst.first)
print(lst.first.next)

lst.print_reversed()