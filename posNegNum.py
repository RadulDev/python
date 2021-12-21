a = eval(input("enter starting number: "))
b = eval(input("enter ending number: "))

if a <= -1:
    a=a
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)