# Write a Python script to sort (ascending and descending) a dictionary by value

d = {'a': 5, 'с': 2, 'b': 3}


def sorting_dict_by_value_asc(d):
    return sorted(d.values())


def sorting_dict_by_value_desc(d):
    return sorted(d.values(), reverse=True)


def sorting_dict_by_key_asc(d):
    return sorted(d)


def sorting_dict_by_key_desc(d):
    return sorted(d, reverse=True)


print(sorting_dict_by_value_asc(d))
print(sorting_dict_by_value_desc(d))
print(sorting_dict_by_key_asc(d))
print(sorting_dict_by_key_desc(d))

# Write a Python script to add a key to a dictionary.

d.update({'new': 8})
print(d)

# Write a Python script to concatenate dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


def concatenate_dicts(*args):
    finaldict = {}
    for dict in args:
        finaldict.update(dict)
    return finaldict


print(concatenate_dicts(dic1, dic2, dic3))


# Write a Python script to check whether a given key already exists in a dictionary.

def key_is_in_dict(d, k):
    if k in d:
        return True
    return False


print(key_is_in_dict(d, 'a'))


# Write a Python program to iterate over dictionaries using for loops returning index, key and value

def return_ditem_dkey_dvalue(d):
    for i, (k, v) in enumerate(d.items()):
        print(i, k, v)


print(return_ditem_dkey_dvalue(d))


# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary for n == 5 :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def n_square_as_a_dict(n):
    d = dict()
    return {x: x * x for x in range(n)}
    # Alternative solution without a dict: return list(map(lambda x: x*x, range(0, n + 1)))


print(n_square_as_a_dict(5))

# Write a Python program to sum all the items in a dictionary

d = {1: 2, 3: 4, 5: 6}

def sum_items(d):
    s = 0
    for key, val in d.items():
        s = s + key + val
    return s


print(sum_items(d))

