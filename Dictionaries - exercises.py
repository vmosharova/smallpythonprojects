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