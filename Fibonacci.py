# Finding a Fibonacci sequence

# Solution 1:
def fibonacci(number):
    n1, n2 = 0, 1
    count = 0
    while count < number:
        print(n1)
        nnew = n1 + n2
        n1 = n2
        n2 = nnew
        count +=1

fibonacci(10)

# Solution 2 - Recursion:
# Nn = N1 + N2

def fibonacci_rec(number):
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return fibonacci_rec(number - 1) + fibonacci_rec(number - 2)

print(fibonacci_rec(4))