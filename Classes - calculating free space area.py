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
        return f'Free area is {self.area} and taken area is {self.percentage_taken}%'

    def free_space(self):
        self.area = self.area - (self.area * self.percentage_taken * 0.01)
        return self.area

    def take_space(self, squaremeters):
        if squaremeters <= self.free_space():
            self.percentage_taken = (squaremeters / self.area) * 100
            self.area = self.area - squaremeters
            return self.percentage_taken
        else:
            print('Not enough space')

    def make_free_space(self, sqaremeters):
        self.area = self.free_space() - sqaremeters
        if self.area >= 0:
            return self.area
        else:
            print(f'Space to be taken ({sqaremeters}) is bigger than free space left {self.area}')

a = Area(10)
a.take_space(3)
a.take_space(2)
print(a)

