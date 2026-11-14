#class -> blueprint , empty form
#object -> filluped form


class Car:
    def __init__(self, color, brand, model, build_year): # constructor function
        self.color = color
        self.brand = brand
        self.model = model
        self.build_year = build_year

    def drive(self):
        print(f"{self.brand} is driving")

    def breaking(self):
        print("breaking the car...!!!")

    def stop(self):
        print(f"{self.brand} stopping..")



car1 = Car("Red", "Toyota", "Camry", "2024")
car2 = Car("Blue", "BMW", "X5", "2023")

car1.drive()
car2.drive()

car1.breaking()


#Toyota is driving
#BMW is driving
#breaking the car...!!!