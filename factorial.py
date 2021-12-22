a = eval(input("enter a limit: "))

fact = 1
while a >= 1:
    fact = fact * a
    a-=1

print(fact)