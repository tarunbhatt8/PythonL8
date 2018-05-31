''' Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student. '''

class Student:
        ''' class to set and display the student information '''

        def __init__(self):
            self.name='student'
            self.rno=0

        def display(self):
            '''method to display student information'''
            print("Name: {}, RollNo: {}, Age: {}, Marks: {}".\
            format(self.name,self.rno,self.age,self.marks))

        def setAge(self,age):
            '''setter method to set age of student'''
            self.age=age

        def setMarks(self,marks):
            '''setter method to set marks of student'''
            self.marks=marks

s1.setAge(21)
s1.setMarks(75)
s1.display()
