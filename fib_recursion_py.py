# Printing fibonacci series in recursion, python

n = int(input())
final = 0

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        final = fib(n-1) + fib(n-2)
    return final

print(fib(n))

# 0 1 1 2 3 5 8 13