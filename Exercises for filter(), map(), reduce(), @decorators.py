from functools import reduce

# Задание 1
# Переписать в виде генераторов списков

a = [1, 2, 3, 4, 5, 6, 7]
a = list(map(lambda x: x ** 3, a))
print(a)

a = [1, 2, 3, 4, 5, 6, 7]
print([x ** 3 for x in a])

# Задание 2
# Переписать в виде фильтра

const = 15

a = [1, 22, 3, 14, 25, 6, 7]
a = [i for i in a if i > const]
print(a)

a = [1, 22, 3, 14, 25, 6, 7]
a = list(filter(lambda x: x > const, a))
print(a)

# Задание 3
# Переписать через reduce

sentences = ['капитан капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = 0
for sentence in sentences:
    cap_count += sentence.count('капитан')

print(cap_count)

VALUE_TO_COUNT = 'капитан'
a = reduce(lambda x, y: x + (y.count(VALUE_TO_COUNT) if VALUE_TO_COUNT in y else 0), sentences, 0)

print(a)


# Задание 4
# Самостоятельно написать реализацию функции zip

def zip_implementation(iterable1, iterable2):
    zip_range = min(len(iterable1), len(iterable2))
    return [(iterable1[n], iterable2[n]) for n in range(zip_range)]

def zip_implementation_with_args(*args):
    zip_range = min(len(i) for i in args)
    zipped = [[] for i in range(zip_range)]
    return [[arg[i] for arg in args] for i in range(zip_range)]


print(zip_implementation([1, 2, 3], ['a', 'b', 'c']))
print(zip_implementation_with_args([1, 2, 3], ['a', 'b', 'c'], [4, 5, 6]))

# Задание 5
# Переписать код через map, filter, reduce

people = [
    {'имя': 'Маша', 'рост': 160},
    {'имя': 'Саша', 'рост': 80},
    {'имя': 'Паша'}
]

height_total = 0
height_count = 0
for person in people:
    if 'рост' in person:
        height_total += person['рост']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count
    print(average_height)

people_with_height_data = filter(lambda x: 'рост' in x.keys(), people)
people_with_height_data = list(people_with_height_data).copy()
height_count = reduce(lambda x, y: x + 1, people_with_height_data, 0)
height_total = reduce(lambda x, y: x['рост'] + y['рост'], people_with_height_data)
try:
    avg = height_total/height_count
except ZeroDivisionError:
    print('Во входных данных не указан рост')

print(avg)

# Задание 6
# Переписать код с использованием декораторов

user1 = 'admin'
user2 = 'Stepan'
user3 = 'Varya'
user4 = None

users = [user1, user2, user3, user4]


def public_info(user):
    print('Информацию пытается получить юзер %s' % user)
    if user is not None:
        return 'Публичная информация для общего пользования'
    return 'Пользователь не авторизован'


def secret_info(user):
    print('Информацию пытается получить юзер %s' % user)
    if user is not None:
        if user == 'admin':
            return 'Секретная информация'
        else:
            return 'Нет доступа к секретной информации'
    return 'Пользователь не авторизован'


for user in users:
    print(public_info(user))
    print('---------')
    print(secret_info(user))
    print('---------')

def which_user_is_in(func):
    def wrapper(*args):
        print(f'Информацию пытается получить юзер {user}')
        return func(*args)

    return wrapper


def is_authorized(func):
    def wrapper(*args):
        if user is not None:
           return func(*args)
        else:
            return 'Пользователь не авторизован'

    return wrapper

def is_admin(func):
    def wrapper(*args):
        if user == 'admin':
            return func(*args)
        return 'Нет доступа к секретной информации'

    return wrapper

@which_user_is_in
@is_authorized
def public_info(user):
    return 'Публичная информация для общего пользования'

@which_user_is_in
@is_authorized
@is_admin
def secret_info(user):
    return 'Секретная информация'


for user in users:
    print(public_info(user))
    print('---------')
    print(secret_info(user))
    print('---------')

