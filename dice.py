import random

num = [1,2,3,4,5,6]

roll = input('do you want to roll dice ?? Y/N: ')

if roll == 'Y':
    # a = random.shuffle(num)
    # print(random.shuffle(num))
    # print(num)
    random.shuffle(num)
    # print(num)
    print(num[1])
    

else:
    # python3 dice.py
    print('stopped !!')

