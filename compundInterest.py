p = eval(input("initial balance : "))
r = eval(input("interest rate : "))
t = eval(input("time period elapsed: "))
n = 100


# A = p * (pow((1 + r/100),t))
A = p * ((1 + r/n) ** t)

print(A)
print(A-p)