class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def disp(self):
        print( "the name is " + self.name )


prsn1 = Person("john",26)

print(prsn1.name)
print(prsn1.age)

prsn1.disp()