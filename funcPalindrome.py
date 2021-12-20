def palindrome(s1):
    s2 = s1[::-1]
    l = len(s1)

    count=1

    for i in range(1,l-1,1):
        if (s1[i]==s2[i]):
            count=count+1
        return count

s = input("enter a string: ")

result = palindrome(s)

if result<=1:
    print("not Palindrome")
else:
    print("Palindrome")