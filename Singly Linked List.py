'''Нужно реализовать методы удаления элемента из списка.
delete_by_index
delete_by_data'''


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

    def is_empty_or_len_is_1(self):

        if self.first is None:
            return

        elif self.first.next is None:
            self.first = None
            return

    def delete_by_index(self, index):

        self.is_empty_or_len_is_1()

        counter = 0
        current = self.first
        while counter != index:
            if current.next is None and index > counter:
                print('Введёный индекс больше, чем число элементов в списке')
                return
            else:
                previous = current
                current = current.next
                counter += 1
        # counter сравнялся с индексом, current = элемент с индексом
        current.data = None
        previous.next = current.next
        current.next = None

    def delete_by_data(self, data):

        self.is_empty_or_len_is_1()

    def print_lst(self, current=None):

        if current is None:
            current = self.first

        while current is not None:
            print(current)
            current = current.next


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
print('xxxxxxxxxx')
lst.print_reversed()
print('xxxxxxxxxx')
lst.delete_by_index(3)
print('xxxxxxxxxx')
lst.print_lst()
