class Parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

def printName(self):
    print(self.fname, self.lname)

class student(Parent):
    def doExams(self):
        pass

newStudent = student("Fredrick", "Boro")

print(newStudent.fname)
print(newStudent.lname)
print(newStudent.doExams)




