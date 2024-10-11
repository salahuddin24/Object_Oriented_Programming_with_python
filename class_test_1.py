class Student : ### class
    roll = ""
    gpa = ""

# rahim = Student()  ### rahim hole student class ar akta object
# # print(isinstance(rahim, Student))# ata check kore je rahim Student class ar object kina .
# rahim.roll = 101
# rahim.gpa = 3.23
#
# print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")
#
# karim = Student()
# karim.roll = 102
# karim.gpa = 3.75

# print(f"Rool : {karim.roll}, GPA : { karim.gpa}")


    def set_value(self, roll, gpa):
       self.roll = roll
       self.gpa = gpa


    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

rahim = Student()
# rahim.roll = 101
# rahim.gpa = 3.43
rahim.set_value(101, 3.23)
rahim.display()


karim = Student()
# karim.roll = 102
# karim.gpa = 3.75
karim.set_value(102,3.433)
karim.display()


















