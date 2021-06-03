import sys

#Finding factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

#Handling recursion limit:
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
