from oregontrail import Passenger, passengers
from random import randint
class Event_list:
    def car_sick():
        selection = randint(0, 3)
        passengers[selection].set_status("Car Sick")
        return f"{passengers[selection].get_name()} has gotten car sick!"
