import math
a = eval(input('enter a number : '))
sum = 0
for i in range(1,a+1):
    sum += (1/math.factorial(i))
    # print(sum)
    # print(i)

print("sum = ",sum)