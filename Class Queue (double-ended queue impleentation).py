'''
Моделировать очередь, в качестве элементов которой могут использоваться целые числа и символы.
Операции: добавление элемента, удаление элемента, печать элементов очереди.

Создать класс-потомок, который содержит процедуру сортировки элементов очереди (числа по возрастанию, символы по алфавиту).
Числа и символы не могут идти в очереди вперемешку,
то, какой тип элементов будет присутствовать в очереди определяется при ее инициализации.
Дальше при попытке добавления в очередь данных, которые не предусмотрены должна выводиться ошибка.
'''

class Queue:

    allowed_types = [int, str]

    def __init__(self, data_type, items=[]):
        self.data_type = data_type
        self.items = items
        if self.data_type not in Queue.allowed_types:
            print('Ошибка: тип данных должен быть числом или строкой')

    def print_items(self):
        print([i for i in self.items])

    def check_type(self, data):
        if type(data) not in Queue.allowed_types:
            print('Ошибка: тип данных не совпадает с заданным')

    def add_right(self, data):
        self.check_type(data)
        self.items.append(data)

    def add_left(self, data):
        self.check_type(data)
        self.items.insert(0, data)

    def del_right(self):
        del self.items[0]

    def del_left(self):
        del self.items[-1]

queue = Queue(int)
queue.add_left(1)
queue.add_left(2)
queue.add_right(3)
queue.print_items()
queue.add_left('Hi')
queue.print_items()

