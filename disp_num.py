neg_num = []
pos_num = []

while True:

    a = eval(input('enter a number : '))
    if a == 0:
        print("task completed successfully !!")
        break
        
    elif a > 0:
        # print("positive")
        pos_num.append(a)

        
    elif a< 0:
        # print("negative")
        neg_num.append(a)
        
    else:
        print("")
    
print("count of positive number",len(pos_num),pos_num," \ncount of negative number",len(neg_num),neg_num)