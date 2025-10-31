import oregontrail
from random import randint

def car_sick():
    selection = randint(0, 3)
    oregontrail.passengers[selection].set_status("Car Sick")
    return f"{oregontrail.passengers[selection].get_name()} has gotten car sick!"
