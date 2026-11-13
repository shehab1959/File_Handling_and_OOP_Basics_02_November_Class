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

s1 = Student("Rafin",[80,75,90])
s2 = Student("Shafin",[60,65,70])
s3 = Student("Sadia",[70,80,57])

s1.print_result() #Shafin Average marks:65.0
s2.print_result() #Shafin Average marks:65.0
s3.print_result() #Sadia Average marks:69.0


##Comment: This is more easy to write, understand and there is less possibility of manual error.