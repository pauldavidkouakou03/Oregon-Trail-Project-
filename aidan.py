from random import randint

    
class Passenger:
    def __init__ (self, name):
        self.name = name
        self.status = "Healthy"
        self.hunger = 100
    
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

    def __str__(self):
        return f"Name: {self.name}, Status: {self.status}, Hunger: {self.hunger}"

driver = Passenger("Aidan")
passenger1 = Passenger("Bob")
passenger2 = Passenger("Charlie")
passenger3 = Passenger("Diana")
passengers = [driver, passenger1, passenger2, passenger3]

class Event_list:
    def car_sick():
        selection = randint(0, 3)
        passengers[selection].set_status("Car Sick")
        return f"{passengers[selection].get_name()} has gotten car sick!"

    def fever():
        selection = randint(0, 3)
        passengers[selection].set_status("Fever")
        return f"{passengers[selection].get_name()} has gotten a Fever!"

def run_random_event():
    list_of_events = [Event_list.car_sick(), Event_list.fever()]
    event_selected = randint(0, len(list_of_events)-1)
    list_of_events[event_selected]
    
run_random_event()

def print_passengers():
    print(driver)
    print(passenger1)
    print(passenger2)
    print(passenger3)

print_passengers()

