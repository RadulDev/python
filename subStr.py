def checkString(string,substring):
    if string.find(substring)==-1:
        print("the substring", substring, "is not present in ", string )
    else:
        print("the substring", substring, "is present in ", string )

str1 = input("Enter the String: ")
substr1 = input("Enter the subString: ")

checkString(str1,substr1)