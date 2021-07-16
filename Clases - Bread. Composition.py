'''Разработать и реализовать иерархию классов для описанных объектов предметной области, используя механизмы композиции.

Объект – хлеб. Поля: масса, стоимость. Методы: процедура инициализации,
процедура вывода значений полей на экран, функция вычисления цены 100 грамм хлеба.
Объект сыр. Поля: масса, стоимость. Методы: процедура инициализации,
процедура вывода значений полей на экран, функция вычисления цены 100 грамм сыра.
Объект – булочка с сыром. Поля: самостоятельно. Методы: процедура инициализации,
процедура вывода значений полей на экран,
функция определения массовой доли начинки в булочке и функция вычисления цены 100 грамм продукта.'''

class Bread:

    def __init__(self, bread_weight, price):
        self.bread_weight = bread_weight
        self.price = price

    def __repr__(self):
        return f'The bread weight is {self.bread_weight} and the price is {self.price}'

    def price_for_100g(self):
        return (self.price * 100) / self.bread_weight


class Broetchen(Bread):

    def __init__(self, bread_weight, price, stuffing_weight):
        Bread.__init__(self, bread_weight, price)
        self.stuffing_weight = stuffing_weight

    def __repr__(self):
        return f'The product weight is {self.broetchen_full_weight()} and the stuffing takes {self.stuffing_concentration()}%'

    def price_for_100g(self):
        price = (self.price * 100) / (self.bread_weight + self.stuffing_weight)
        return round(price)

    def broetchen_full_weight(self):
        return self.bread_weight + self.stuffing_weight

    def stuffing_concentration(self):
        concentration = (self.stuffing_weight / (self.bread_weight + self.stuffing_weight)) * 100
        return round(concentration)

bread = Bread(800, 50)
broetchen = Broetchen(125, 45, 77)