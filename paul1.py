def get_health(self): car
def get_fuel(self): car
def get_hunger(self): passenger
def get_phone_battery(self): passenger
def get_snacks(self): supplies

for passenger in self.passenger:
    passenger.get_hunger()