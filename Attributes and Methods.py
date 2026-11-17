class Student():
    # constructor method
    def __init__(self, name, marks, attendence=80):
        self.name = name                # attirbute
        self.marks = marks              # attribute
        self.attendence = attendence    # default attribute

    def calculate_average(self):
        print(sum(self.marks) / len(self.marks))

s1 = Student("Sadia", [70, 80])  # default value of attendence is used

print(s1.marks)       # attirbute
print(s1.name)        # attirbute
print(s1.attendence)  # default attribute