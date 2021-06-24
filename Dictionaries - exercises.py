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
