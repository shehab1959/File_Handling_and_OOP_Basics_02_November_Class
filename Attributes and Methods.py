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




##

## Summary

# Defining a class
class Car():
    # construtor method
    def __init__(self, brand, color):
        self.brand = brand     # attribute
        self.color = color     # attribute

    # method
    def start_engine(self):
        print(f"{self.brand} engine starting..Whirrrr... vroom!")


    def get_color(self):
        return self.color


# Creating objects from a class
car1 = Car("Toyota", "White")
car2 = Car(brand="BMW", color="Black")

# Accessing data of an object
print(f"Car 1 color: {car1.color}")
print(f"Car 2 brand: {car2.brand}")

# Calling methods
car1.start_engine()
car2.start_engine()