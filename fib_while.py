a = eval(input('enter a number : '))

fib = 0
m = 1
l = 0

while a > 0:
    print(fib)
    l = m + fib
    fib = m
    m = l
    a-=1