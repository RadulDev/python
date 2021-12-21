a = eval(input("enter a number to find factorial : "))
fact = 1
for i in range(a,1,-1):
    fact = fact * i
    # print(fact)
    
print("factorial of the given number is : ",fact)
