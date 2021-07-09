'''Разработать и реализовать иерархию классов для описанных объектов предметной области, используя механизмы наследования.
Объект – хлеб. Поля: масса, стоимость.
Методы: процедура инициализации, процедура вывода значений полей на экран, функция вычисления цены 100 грамм хлеба.
Объект – булочка с сыром.
Поля: масса булочки, масса начинки, стоимость.
Методы: процедура инициализации, процедура вывода значений полей на экран,
функция определения массовой доли начинки в булочке и функция вычисления цены 100 грамм продукта.'''


class Bread:

    def __init__(self, weight, price):
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'The bread weight is {self.weight} and the price is {self.price}'

    def price_for_100g(self):
        price = (self.price * 100) / self.weight
        return '100g of product cost ' + str(price)


class Broetchen(Bread):

    def __init__(self, weight, price, stuffing_weight):
        Bread.__init__(self, weight, price)
        self.stuffing_weight = stuffing_weight

    def __repr__(self):
        return Bread.__repr__(self) + f' and the stuffing weight is {self.stuffing_weight}'

    def price_for_100g(self):
        price = (self.price * 100) / (self.weight + self.stuffing_weight)
        return '100g of product cost ' + str(price)

    def stuffing_concentration(self):
        concentration = (self.stuffing_weight / (self.weight + self.stuffing_weight)) * 100
        return 'The stuffing concentration is ' + str(concentration) + '%'

bread = Bread(800, 50)
broetchen = Broetchen(125, 45, 75)

print(bread)
print(broetchen)
print(bread.price_for_100g())
print(broetchen.price_for_100g())
print(broetchen.stuffing_concentration())


