# Write a Python script to sort (ascending and descending) a dictionary by value

d = {'a': 5, 'с': 2, 'b': 3}


def sort_dict_by_value_asc(d):
    return sorted(d.values())


def sort_dict_by_value_desc(d):
    return sorted(d.values(), reverse=True)


def sort_dict_by_key_asc(d):
    return sorted(d)


def sort_dict_by_key_desc(d):
    return sorted(d, reverse=True)


print(sort_dict_by_value_asc(d))
print(sort_dict_by_value_desc(d))
print(sort_dict_by_key_asc(d))
print(sort_dict_by_key_desc(d))

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

def square_given_sequence(n):
    d = dict()
    return {x: x * x for x in range(n)}
    # Alternative solution without a dict: return list(map(lambda x: x*x, range(0, n + 1)))


print(square_given_sequence(5))

# Write a Python program to sum all the items in a dictionary

d = {1: 2, 3: 4, 5: 6}


def sum_items(d):
    s = 0
    for key, val in d.items():
        s = s + key + val
    return s


print(sum_items(d))


# Write a Python program to multiply all the items in a dictionary

def multiply_items(d):
    s = 1
    for key, val in d.items():
        s = s * key * val
    return s


print(multiply_items(d))


# Write a Python program to remove a key from a dictionary
# It is not possible to delete a key without deleting its value, so here is a solution with None:

def remove_key_but_not_value(d, key):
    if key in d:
        d[None] = d[key]
    return d


print(remove_key_but_not_value(d, 1))


# ...and here is the solution with deleting both the key and its value:

def remove_key_and_its_value(d, key):
    d.pop(key)
    return d


print(remove_key_and_its_value(d, 3))


#  Write a Python program to map two lists into a dictionary

def map_lists_into_dict(keys, vals):
    return dict(zip(keys, vals))


print(map_lists_into_dict([1, 2], ['abc', 'def']))

# Write a Python program to get the maximum and minimum value in a dictionary

d = {'a': 555, 'b': 1, 'c': 33}


def find_min_max(d):
    k = (lambda vals: d[vals])
    return d[max(d.keys(), key=k)], d[min(d.keys(), key=k)]


print(find_min_max(d))

# Write a Python program to remove duplicates from a dictionary

d = {'id1':
         {'name': ['Sara'],
          'class': ['V'],
          'subject_integration': ['english, math, science']
          },
     'id2':
         {'name': ['David'],
          'class': ['V'],
          'subject_integration': ['english, math, science']
          },
     'id3':
         {'name': ['Sara'],
          'class': ['V'],
          'subject_integration': ['english, math, science']
          },
     }


def remove_duplicates(d):
    dict_without_duplicates = dict()
    for key, val in d.items():
        if val not in dict_without_duplicates.values():
            dict_without_duplicates[key] = val
    return dict_without_duplicates


print(remove_duplicates(d))

# Write a Python program to check if a dictionary is empty or not.

d1 = dict()


def is_dict_empty(d):
    return ("The dictionary is not empty" if d else "The dictionary is empty")


print(is_dict_empty(d))
print(is_dict_empty(d1))

# Write a Python program to print all unique values in a list of dictionaries.

lst = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

def print_unique_values(lst):
    return set(val for d in lst for val in d.values())


print(print_unique_values(lst))


