### Introduction to OOP ### 
# (first we will see normally then same thing using OOP)

             ##Normally##
#For student 1
student_1_name = "Rafin"
student_1_marks = [80,75,90]

#For student 2
student_2_name = "Shafin"
student_2_marks = [60,65,70]

#For student 3
student_3_name = "Sadia"
student_2_marks = [70,80,57] #(here student_2 instant of student_3 made intentional mistake because this time of error may happen anytime)


def calculate_avg(marks):
    return sum(marks)/len(marks)

def print_result(name,marks):
    avg = calculate_avg(marks)
    print(f"{name} Average marks:{avg}")

print_result(student_1_name,student_1_marks) #Rafin Average marks:81.66666666666667
print_result(student_2_name,student_2_marks) #Shafin Average marks:69.0
#print_result(student_3_name,student_3_marks) #error= (there is no student_3_marks)

#Comment: To solve this type of problem we have to use OOP, because OOP make it easier and less possibility of taking wrong input manually.






             ###Now same this using OOP###

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def calculate_avg(self):
        return sum(self.marks)/len(self.marks)

    def print_result(self):
        avg = self.calculate_avg()
        print(f"{self.name} Average marks:{avg}")

#now Create objects
s1 = Student("Rafin",[80,75,90])
s2 = Student("Shafin",[60,65,70])
s3 = Student("Sadia",[70,80,57])

s1.print_result() #Shafin Average marks:65.0
s2.print_result() #Shafin Average marks:65.0
s3.print_result() #Sadia Average marks:69.0


##Comment: This is more easy to write, understand and there is less possibility of manual error.













##Another example

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def print_result(self):
        avg = self.calculate_average()
        print(f"{self.name} Average: {avg}")

    def check_grade(self):
        avg = self.calculate_average()
        if avg >= 80:
            print("A")
        elif avg >= 70:
            print("B")
        else:
            print("C")



s1 = Student("Rafin", [80, 75, 90])
s2 = Student("Shafin", [60, 65, 70])
s3 = Student("Sadia", [70, 80, 90])


s1.print_result() #Rafin Average: 81.66666666666667
s1.check_grade() #A
#print()
s2.print_result() #Shafin Average: 65.0
s2.check_grade() #C




students = [
    Student("Rafin", [80, 75, 90]),
    Student("Shafin", [60, 65, 70]),
    Student("Shakil", [80, 75, 90]),
    Student("Jihad", [60, 65, 70]),
    Student("Samia", [60, 65, 70]),
    Student("Sadia", [60, 69, 70]),
    Student("Nirob", [60, 65, 70]),
    Student("Shovon", [60, 65, 70])
]


for std in students:
    std.calculate_average()
    std.print_result()
    # std.check_grade()
    print() #this gives just extra space

#Outputs are: 
#Rafin Average: 81.66666666666667

#Shafin Average: 65.0

#Shakil Average: 81.66666666666667

#Jihad Average: 65.0

#Samia Average: 65.0

#Sadia Average: 66.33333333333333

#Nirob Average: 65.0

#Shovon Average: 65.0