#### constructor ----

class Student : ### class
    roll = ""
    gpa = ""

    # def set_value(self, roll, gpa):
    #    self.roll = roll
    #    self.gpa = gpa

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

rahim = Student(101, 3.23)
# rahim.set_value(101, 3.23)
rahim.display()


karim = Student(102,3.433)
# karim.set_value(102,3.433)
karim.display()
















