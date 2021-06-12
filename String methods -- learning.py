#Palindrome

s = 'lorem ipsum'

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