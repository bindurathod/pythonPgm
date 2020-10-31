class Student:
    marks = []
    def getData(self, rn, name, m1, m2, m3, m4, m5, m6):
       Student.rn = rn
       Student.name = name
       Student.marks.append(m1)
       Student.marks.append(m2)
       Student.marks.append(m3)
       Student.marks.append(m4)
       Student.marks.append(m5)
       Student.marks.append(m6)
      
    def displayData(self):
           print("Roll Number is: ", Student.rn)
           print("Name is: ", Student.name)
           print("Marks in subject 1: ", Student.marks[0])
           print("Marks are: ", Student.marks)

    def total(self):
        return (Student.marks[0] + Student.marks[1] + Student.marks[2] + Student.marks[3] + Student.marks[4] + Student.marks[5])

r= int (input("Enter the roll number: "))
name= input("Enter the name: ")
m1 = int (input("Enter the marks in first subject: "))
m2 = int (input("Enter the marks in second subject: "))
m3 = int (input("Enter the marks in third subject: "))
m4 = int (input("Enter the marks in forth subject: "))
m5 = int (input("Enter the marks in fifth subject: "))
m6 = int (input("Enter the marks in sixth subject: "))

s1 = Student()
s1.getData(r, name, m1, m2, m3, m4, m5, m6)
s1.displayData()
print ("Total Marks are: ", s1.total())

        



        
