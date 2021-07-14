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