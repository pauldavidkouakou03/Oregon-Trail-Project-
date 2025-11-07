import random

#Classes (Not Final, Just Experimental for Integration Later)  
class Passenger:
    def __init__ (self, name):
        self.name = name
        self.status = "Healthy"
        self.hunger = 100
        self.phone_battery = 100
    
    def get_name(self):
        return self.name
    def get_status(self):
        return self.status
    def set_status(self, new_status):
        self.status = new_status
    def get_hunger(self):
        return self.hunger
    def reduce_hunger(self, reduction):
        self.hunger -= reduction
    def increase_hunger(self, increase):
        self.hunger += increase
    def reduce_phone_battery(self, reduction):
        self.phone_battery -= reduction

    def __str__(self):
        return f"Name: {self.name}, Status: {self.status}, Hunger: {self.hunger}"
    
class Vehicle:
    def __init__(self, health):
        self.health = health
        self.fuel = 100    
    def get_health(self):
        return self.health
    def reduce_health(self, reduction):
        self.health -= reduction
    def reduce_fuel(self, reduction):
        self.fuel -= reduction
    def __str__(self):
        return f"Vechicle Health: {self.health}"
    
class Supplies:
    def __init__(self, snacks, medicine):
        self.snacks = snacks
        self.medicine = medicine
    def get_snacks(self):
        return self.snacks
    def get_medicine(self):
        return self.medicine
    def get_fuel(self):
        return self.fuel
    def use_snack(self):
        if self.snacks > 0:
            self.snacks -= 1
    def use_medicine(self):
        if self.medicine > 0:
            self.medicine -= 1
    def __str__(self):
        return f"Supplies - Snacks: {self.snacks}, Medicine: {self.medicine}"
    



driver = Passenger("Aidan")
passenger1 = Passenger("Bob")
passenger2 = Passenger("Charlie")
passenger3 = Passenger("Diana")
passengers = [driver, passenger1, passenger2, passenger3]
car = Vehicle(100)
supplies = Supplies(10, 3)

#Event Functions
class Events:
    def car_sick():
        selection = random.randint(0, 3)
        passengers[selection].set_status("Car Sick")
        print(f"{passengers[selection].get_name()} has gotten car sick!")

    def fever():
        selection = random.randint(0, 3)
        passengers[selection].set_status("Fever")
        print(f"{passengers[selection].get_name()} has gotten a Fever!")
    
    def use_phone():
        selection = random.randint(0, 3)
        passengers[selection].reduce_phone_battery(10)
        print(f"{passengers[selection].get_name()} used their phone.")




#Event Testing
event_list = [Events.car_sick, Events.fever, Events.use_phone]
def run_event():
    chosen_event = random.choice(event_list)
    chosen_event()

def print_stats():
    print(driver)
    print(passenger1)
    print(passenger2)
    print(passenger3)
    print(car)
    print(supplies)


run_event()
print_stats()
'''
user_input = input(f"Would you like to give {passenger1.get_name()} a snack? (y/n):")
if user_input == "y":
    supplies.use_snack()
    passenger1.increase_hunger(25)
    print(f"{passenger1.get_name()} has eaten a snack.")
else:
    pass

print_stats()
'''






#Prompt the user for inputs every certain amount of miles driven
#Let the user choose to use items for their passengers
#Set up a time system
#End the game if all passengers are gone or if vehicle health reaches 0
#Occansional stops will happen along the way, allowing the user to restock supplies
