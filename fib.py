a = eval(input('enter a number : '))

fib = 0
m = 1
l = 0
for i in range(1,a+1):
    print(fib)
    l = m + fib
    fib = m
    m = l