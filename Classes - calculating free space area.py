'''Описать класс, включающий заданные поля и методы.
Объект – ангар. Параметры: площадь и процент занятой площади. Изначально занятая площадь 0 процентов.

Методы:
1) Функция инициализации полей
2) Функция вывода на экран значений полей
3) Функция, определяющая и возвращающая по запросу свободную площадь помещения.
4) Функция, занять площадь. Принимает аргумент в виде квадратных метров. Должна менять процент занятой площади.
Должна корректно обрабатывать ситуации, когда площади недостаточно
5) Функция, освобождающая площадь. Также требуется корректная обработка ошибок.'''


class Area:

    def __init__(self, area, percentage_taken=0):
        self.area = area
        self.percentage_taken = percentage_taken

    def __repr__(self):
        return f'Free area is {round(self.free_space())} and taken area is {round(self.percentage_taken)}%'

    def free_space(self):
        return self.area - (self.area * self.percentage_taken * 0.01)

    def take_space(self, squaremeters):
        if squaremeters <= self.free_space():
            self.percentage_taken = (squaremeters / self.area) * 100
        else:
            print('Not enough space')

    def make_free_space(self, squaremeters):
        squaremeters_in_percent = (squaremeters / self.area) * 100
        self.percentage_taken = self.percentage_taken - squaremeters_in_percent
        if self.percentage_taken >= 0:
            return self.percentage_taken
        else:
            print(f'Space to be taken ({squaremeters}) is bigger than free space left {round(self.free_space())}')

a = Area(10)
a.take_space(3)
a.make_free_space(2)
a.take_space(22)
a.make_free_space(22)
print(a)


