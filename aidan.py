import random
import time
#Classes (Not Final, Just Experimental for Integration Later)  
class Passenger:
    def __init__ (self, name, battery):
        self.name = name
        self.status = "Healthy"
        self.hunger = 100
        self.phone_battery = battery
    
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
        return f"Name: {self.name}, Status: {self.status}, Hunger: {self.hunger} Phone Battery: {self.phone_battery}"
    
class Vehicle:
    def __init__(self, health):
        self.health = health
        self.fuel = 20
        self.gas_tank_size = 20
    def get_health(self):
        return self.health
    def reduce_health(self, reduction):
        self.health -= reduction
    def use_fuel(self, reduction):
        self.fuel -= reduction
    def __str__(self):
        return f"Vechicle Health: {self.health}, Gas: {self.fuel}"
    
class Supplies:
    def __init__(self, snacks, medicine):
        self.snacks = snacks
        self.medicine = medicine
        self.money = 500
    def get_snacks(self):
        return self.snacks
    def get_money(self):
        return self.money
    def get_medicine(self):
        return self.medicine
    def use_snack(self):
        if self.snacks > 0:
            self.snacks -= 1
    def use_medicine(self):
        if self.medicine > 0:
            self.medicine -= 1
    def spend_money(self):
        if self.money > 0:
            self.money -= 10
    def __str__(self):
        return f"Supplies - Snacks: {self.snacks}, Medicine: {self.medicine}, Money: {self.money}"
    



driver = Passenger("Aidan", 100)
passenger1 = Passenger("Bob", 100)
passenger2 = Passenger("Charlie", 100)
passenger3 = Passenger("Diana", 100)
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


#run_event()
#print_stats()

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
def option_selection(selection):
    pass
def passenger_item_use(choice):
    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

#Running a Test for the Game Loop
while True:
    time.sleep(5)
    run_event()
    time.sleep(5)
    while True:
        print("\n") #Add space for readability
        print("1. View Stats")
        print("2. Use Item")
        print("3. Continue Driving")
        try:
            selection = int(input("What would you like to do?: "))
            match selection:
                case 1:
                    print_stats()
                    continue #Restarts the inner loop after viewing stats
                case 2:
                    print("\n")
                    print(supplies)
                    print(f"1. {driver.get_name()}")
                    print(f"2. {passenger1.get_name()}")
                    print(f"3. {passenger2.get_name()}")
                    print(f"4. {passenger3.get_name()}")
                    try:
                        choice = int(input("Which passenger would you like to give an item to? (1-4):"))
                        print("\n")
                        passenger_item_use(choice)
                        continue #Restarts the inner loop after using an item
                    except ValueError:
                        print("Invalid Input")
                case 3:
                    break #Restarts the entire loop to continue driving
        except ValueError:
            print("Invalid Input")



    '''
    if user_input == 1:
        print_stats()
    elif user_input == 2:
        print(supplies)
        print(f"1. {driver.get_name()}")
        print(f"2. {passenger1.get_name()}")
        print(f"3. {passenger2.get_name()}")
        print(f"4. {passenger3.get_name()}")
        passenger_choice = input("Which passenger would you like to give an item to? (1-4):")
        
    elif user_input == 3:
        pass
    else:
        print("Invalid Input")
    '''



#Prompt the user for inputs every certain amount of miles driven
#Let the user choose to use items for their passengers
#Set up a time system
#End the game if all passengers are gone or if vehicle health reaches 0
#Occansional stops will happen along the way, allowing the user to restock supplies
