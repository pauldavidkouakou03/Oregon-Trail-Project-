#Create a project Oregan Trail game 
class Player:
    def __init__(self, name, health=100, supplies=50):
        self.name = name
        self.health = health
        self.supplies = supplies

    def travel(self, distance):
        if self.supplies >= distance // 10:
            self.supplies -= distance // 10
            print(f"{self.name} traveled {distance} miles.")
        else:
            print(f"{self.name} does not have enough supplies to travel {distance} miles.")

    def rest(self, days):
        self.health += days * 5
        if self.health > 100:
            self.health = 100
        print(f"{self.name} rested for {days} days and now has {self.health} health.")

    def gather_supplies(self, amount):
        self.supplies += amount
        print(f"{self.name} gathered {amount} supplies and now has {self.supplies} supplies.")

    def status(self):
        print(f"Player: {self.name}, Health: {self.health}, Supplies: {self.supplies}")
















































