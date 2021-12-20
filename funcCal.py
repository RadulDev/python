def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

opt = eval(input(" 1. Add: \n 2. Sub: \n 3. Mul: \n 4. Div: \n enter any option from above: "))

a = eval(input("enter number: "))
b = eval(input("enter number: "))

if opt==1:
    print("sum is : ", add(a,b))
elif opt == 2:
    print("diff is : ", sub(a,b))
elif opt == 3:
    print("product is : ", mul(a,b))
elif opt == 4:
    print("quotient is : ", div(a,b))
else:
    print("retry")