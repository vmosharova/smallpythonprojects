# Palindrome

s = ' lorem ipsum '


def simple_reversed(s):
    return (s[::-1])  # faster approach


def reversed_with_join(s):
    return ''.join(reversed(s))  # slower approach


print(reversed_with_join(s))


def is_palindrome(s):
    new_s = s[::-1]
    return new_s == s


print(is_palindrome(s))  # False
print(is_palindrome('abcba'))  # True

# Return the string without any whitespace at the beginning or the end
print(s.strip())

# Convert the value of txt to upper case.
s = 'lorem ipsum'
print(s.upper())

# Make the first letter the upper case letter
print(s.capitalize())


# Write a program to count the number of characters (character frequency) in a string.
def number_char(s):
    a = dict()
    for i in s:
        keys = a.keys()
        if i in keys:
            a[i] += 1
        else:
            a[i] = 1
    return a


print(number_char(s))


# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return the empty string instead

def first2last2chars(s):
    if len(s) >= 2:
        return s[:2] + s[-2:]
    else:
        return ''


print(first2last2chars(s))


# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself.

def replace_first_char(s):
    char = s[0]
    s = s.replace(char, '$')
    return char + s[1:]


print(replace_first_char('sososos'))


#Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.

def add_ing(s):
    if len(s) >= 3:
        if s[-3:] != 'ing':
            return s + 'ing'
        else:
            return s + 'ly'
    return s

print(add_ing('abc'))


# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'poor' follows the 'not', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

def replace_substring_in_string(s):
    if 'not' in s and 'poor' in s:
        index_not = s.find('not')
        index_poor = s.find('poor')
        if index_poor > index_not:
            s = s.replace(s[index_not:(index_poor+4)], 'good')
        else:
            return s
    return s

print(replace_substring_in_string('It is not that poor'))

# Write a Python function that takes a list of words and returns the longest word and the length of the longest one.

def longest_word(l):
    max_word = dict()
    for word in l:
        max_word[len(word)] = word
    return(max(max_word.items()))

print(longest_word(['word', 'exercises', ' ', 'test']))


# Write a Python program to remove the nth index character from a nonempty string.

def remove_char(s, n):
    s = s.replace(s[n], '')
    return s
print(remove_char(s, 1))

def remove_char_2(s, n):
    s1 = s[:n]
    s2 = s[n+1:]
    return s1 + s2
print(remove_char_2(s, 1))

# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

def change_1st_and_last_chars(s):
    return s[-1] + s[1:-1] + s[0]

print(change_1st_and_last_chars(s))