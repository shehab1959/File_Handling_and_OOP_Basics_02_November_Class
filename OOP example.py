#Example-01: About Mobile Phone


#class and constructor
class Mobile:
    def __init__(self,brand,model,battery):
        self.brand = brand
        self.model = model
        self.battery = battery

#create methods
    def make_call(self,number):
        print(f"{self.brand} {self.model} is calling the number: {number}...")

    def send_message(self,message):
        print(f"Sending message from the phone {self.brand}: {message}")

    def chech_battery(self):
        print(f"The phone {self.brand} and the model {self.model}'s battery is remaining: {self.battery}")

#create objects
phn1 = Mobile("Apple", "14 pro", 91)
phn2 = Mobile("Samsung", "24 Ultra", 87)

#Methods call
phn1.make_call("01769999966") #Apple 14 pro is calling the number: 01769999966...
phn2.chech_battery() #The phone Samsung and the model 24 Ultra's battery is remaining: 87
phn1.send_message("Hello Hejbulla Shehab") #Sending message from the phone Apple: Hello Hejbulla Shehab











###Example-02: About Bank Account Scenario

class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner_name} deposited {amount} BDT. New balance: {self.balance} BDT")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner_name} withdrew {amount} BDT. Remaining balance: {self.balance} BDT")
        else:
            print(f"Sorry {self.owner_name}, insufficient balance!")


# দুটি ব্যাংক অ্যাকাউন্ট তৈরি
acc1 = BankAccount("Rahim", 5000)
acc2 = BankAccount("Karim", 2000)

# লেনদেন করা হচ্ছে
acc1.deposit(1500)
acc1.withdraw(3000)

acc2.withdraw(4000)  # পর্যাপ্ত টাকা না থাকায় এরর মেসেজ দেখাবে

#Output:
#Rahim deposited 1500 BDT. New balance: 6500 BDT
#Rahim withdrew 3000 BDT. Remaining balance: 3500 BDT
#Sorry Karim, insufficient balance!

#
