import random
import time
import sys
#Classes (Not Final, Just Experimental for Integration Later)  
class Passenger:
    def __init__ (self, name, battery):
        self.name = name
        self.status = "Healthy"
        self.hunger = 100
        self.phone_battery = battery
        self.fever_days = 0
    
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
    def fever_counter(self):
        self.fever_days += 1
    def get_fever_days(self):
        return self.fever_days
    def reduce_phone_battery(self, reduction):
        self.phone_battery -= reduction

    def __str__(self):
        return f"Name: {self.name}, Status: {self.status}, Hunger: {self.hunger} Phone Battery: {self.phone_battery}"
    
class Vehicle:
    def __init__(self, health):
        self.health = health
        self.fuel = 20
        self.gas_tank_size = 20
        self.miles_driven = 0
    def get_health(self):
        return self.health
    def reduce_health(self, reduction):
        self.health -= reduction
    def use_fuel(self, reduction):
        self.fuel -= reduction
    def get_fuel(self):
        return self.fuel
    def get_miles_driven(self):
        return self.miles_driven
    def drive_miles(self, miles):
        self.miles_driven += miles
    def __str__(self):
        return f"Vechicle Health: {self.health}, Gas: {self.fuel} gallons"
    
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
    def spend_money(self, amount):
        if self.money > 0:
            self.money -= amount
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
        if passengers[selection].get_status() != "Dead":
            passengers[selection].set_status("Car Sick")
            print(f"{passengers[selection].get_name()} has gotten car sick!")

    def fever():
        selection = random.randint(0, 3)
        if passengers[selection].get_status() != "Dead":
            passengers[selection].set_status("Fever")
            print(f"{passengers[selection].get_name()} has gotten a Fever!")
    
    def use_phone():
        selection = random.randint(0, 3)
        if passengers[selection].get_status() != "Dead":
            passengers[selection].reduce_phone_battery(10)
            print(f"{passengers[selection].get_name()} used their phone.")

    def object_in_road():
        try:
            user_input = input("There is debris in the road! You can try to avoid it but it may damage the car.\n You could also take another way, but you will lose distance on your destination. (y (Avoid) / n (Detour)): ")
            if user_input == "y":
                chance = random.randint(1, 10)
                if chance <= 6:
                    print("You sucessfully avoided the debris!")
                else:
                    print("You hit the debris, damaging the car.")
                    car.reduce_health(25)
            elif user_input == "n":
                print("You took a detour, losing some distance.")
                car.drive_miles(-40)
        except ValueError:
            print("Invalid Input")
    
    def flat_tire():
        user_input = input("You got a flat tire! You can try to fix it yourself or call for roadside assistance. (f (fix) / c (call)): ")
        try:
            if user_input == "f":
                chance = random.randint(1, 20)
                if chance > 15:
                    print("You successfully fixed the tire!")
                else:
                    print("You failed to fix the tire, damaging the car.")
                    car.reduce_health(25)
            elif user_input == "c":
                print("You called for roadside assistance, spending some money.")
                supplies.spend_money(30)
        except ValueError:
            print("Invalid Input")
    

            
#Event Testing
event_list = [Events.flat_tire, Events.object_in_road, Events.car_sick, Events.fever, Events.use_phone]
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


#Item Use / Selection / and Game Check Functions
def supply_selection(selection, passenger):
    match selection:
        case 1:
            if supplies.get_snacks() > 0:
                supplies.use_snack()
                passenger.increase_hunger(30)
                print(f"{passenger.get_name()} has eaten a snack.")
            else:
                print("No Snacks Left!")
        case 2:
            if supplies.get_medicine() > 0:
                supplies.use_medicine()
                passenger.set_status("Healthy")
                print(f"{passenger.get_name()} has used some medicine.")
            else:
                print("No Medicine Left!")

#Passenger Item Use Function
def passenger_item_use(choice):
    match choice:
        case 1:
            print("1. Snacks")
            print("2. Medicine")
            selection = int(input(f"Which item would you like to give to {driver.get_name()}?"))
            supply_selection(selection, driver)
        case 2:
            print("1. Snacks")
            print("2. Medicine")
            selection = int(input(f"Which item would you like to give to {passenger1.get_name()}?"))
            supply_selection(selection, passenger1)
        case 3:
            print("1. Snacks")
            print("2. Medicine")
            selection = int(input(f"Which item would you like to give to {passenger2.get_name()}?"))
            supply_selection(selection, passenger2)
        case 4:
            print("1. Snacks")
            print("2. Medicine")
            selection = int(input(f"Which item would you like to give to {passenger3.get_name()}?"))
            supply_selection(selection, passenger3)

def game_check():
    #Check if Passenger has starved
    for passenger in passengers:
        if passenger.get_hunger() <= 0:
            passenger.set_status("Dead")
            print(f"{passenger.get_name()} has died of starvation.")
    #Check Passenger with Fever
    for passenger in passengers:
        if passenger.get_status() == "Fever":
            passenger.fever_counter()
            if passenger.get_fever_days() > 4:
                print(f"{passenger.get_name()} has died from their fever.")
                passenger.set_status("Dead")
    #Check if Vehicle is Dead or out of fuel
    if car.get_health() <= 0 or car.get_fuel() <= 0:
        print("Your vehicle is no longer operable! Game Over.")
        sys.exit()
    dead_count = 0
    for passenger in passengers:
        if passenger.get_status() == "Dead":
            dead_count += 1
    if dead_count == 4:
        print("All Passengers have died! Game Over.")
        sys.exit()
    





#Running a Test for the Game Loop
while True:
    #Simulate driving a certain amount of miles
    for passenger in passengers:
        passenger.reduce_hunger(10)
    car.use_fuel(1)
    car.drive_miles(20)
    game_check()
    run_event()
    

    while True:
        print("\n") #Add space for readability
        print(f"Miles Left: {1000 - car.get_miles_driven()}")
        print("1. View Stats")
        print("2. Use Item")
        print("3. Continue Driving")
        try:
            selection = int(input("What would you like to do?: "))
            match selection:
                case 1: #Shows All Stats
                    print_stats()
                    continue #Restarts the inner loop after viewing stats
                #Note for Case 2, it does not check if the passenger is dead or not, only displays it, will be added later.
                case 2: #Allows you to use an item
                    print("\n")
                    print(supplies)
                    if driver.get_status() != "Dead":
                        print(f"1. {driver.get_name()}")
                    else:
                        print(f"1. {driver.get_name()} is Dead.")
                    if passenger1.get_status() != "Dead":
                        print(f"2. {passenger1.get_name()}")
                    if passenger2.get_status() != "Dead":
                        print(f"3. {passenger2.get_name()}")
                    if passenger3.get_status() != "Dead":
                        print(f"4. {passenger3.get_name()}")
                    #try and except will catch any invalid inputs when choosing a passenger
                    try:
                        choice = int(input("Which passenger would you like to give an item to? (1-4):"))
                        print("\n")
                        passenger_item_use(choice)
                        continue #Restarts the inner loop after using an item
                    except ValueError:
                        print("Invalid Input")
                case 3: #Allows you to continue driving
                    break #Restarts the entire loop to continue driving
        except ValueError:
            print("Invalid Input")
