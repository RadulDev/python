class Student:
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place

    def printStudentDetails(self):
        print("I'm ",self.name,". im coming from ",self.place," and I'm ",self.age," years old.")


studentName = input("Enter your name: ")
studentAge = input("Enter your age: ")
studentPlace = input("Enter your place: ")


student1 = Student(studentName,studentAge,studentPlace)
student1.printStudentDetails()