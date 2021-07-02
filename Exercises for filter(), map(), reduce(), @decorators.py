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

# Задание 3
# Переписать через reduce

sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = 0
for sentence in sentences:
    cap_count += sentence.count('капитан')

print(cap_count)

# Задание 4
# Самостоятельно написать реализацию функции zip

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
