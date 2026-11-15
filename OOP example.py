#Example-01: About Mobile Phone

class Mobile:
    def __init__(self,brand,model,battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def make_call(self,number):
        print(f"{self.brand} {self.model} is calling the number: {number}...")

    def send_message(self,message):
        print(f"Sending message from the phone {self.brand}: {message}")

    def chech_battery(self):
        print(f"The phone {self.brand} and the model {self.model}'s battery is remaining: {self.battery}")

phn1 = Mobile("Apple", "14 pro", 91)
phn2 = Mobile("Samsung", "24 Ultra", 87)

#Methods call
phn1.make_call("01769999966") #Apple 14 pro is calling the number: 01769999966...
phn2.chech_battery() #The phone Samsung and the model 24 Ultra's battery is remaining: 87
phn1.send_message("Hello Hejbulla Shehab") #Sending message from the phone Apple: Hello Hejbulla Shehab
