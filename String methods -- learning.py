#Palindrome

s = ' lorem ipsum '

def simple_reversed(s):
    return (s[::-1]) #faster approach

def reversed_with_join(s):
    return ''.join(reversed(s)) #slower approach

print(reversed_with_join(s))

def is_palindrome(s):
    new_s = s[::-1]
    return new_s == s

print(is_palindrome(s)) #False
print(is_palindrome('abcba')) #True


#Return the string without any whitespace at the beginning or the end
print(s.strip())

#Convert the value of txt to upper case.
s = 'lorem ipsum'
print(s.upper())

#Make the first letter the upper case letter
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