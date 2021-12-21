a = eval(input("enter a number to check amstrong or not : "))
k = a
sum = 0

while a > 0:
    num = a % 10
    sum += num ** 3
    a = a//10

print(int(sum))

if sum == k:
    print("amstrong number")

else:
    print("not an amstrong number")
    print(a)