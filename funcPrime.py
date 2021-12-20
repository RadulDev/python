def checkPrime(num):
    count = 0

    for i in range(num,1,-1):

        if num % i == 0:
            count+=1
    
    if count>=2:
        print(num,"is not a prime")
    else:
        print(num,"is a prime")

number = eval(input("enter a number to check prime: "))
checkPrime(number)