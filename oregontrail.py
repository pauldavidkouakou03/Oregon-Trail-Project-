#Here is our code for amazing Oregon Trail Game
#Slow Print Function
def slow_print(ascii_art,speed):
  for line in ascii_art.strip().split('\n'):
    print(line)
    time.sleep(speed)
events_list = ['car sick', 'ran out of snacks', 'phone died']
#Intro
import Events
import sys
import time
ascii_art_intro = r"""
__        __   _                            _                                
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___                          
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \                         
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |                        
 __\_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/       _                 
|  \/  | ___   __| | ___ _ __ _ __   |  _ \ ___   __ _  __| |                
| |\/| |/ _ \ / _` |/ _ \ '__| '_ \  | |_) / _ \ / _` |/ _` |                
| |  | | (_) | (_| |  __/ |  | | | | |  _ < (_) | (_| | (_| |                
|_|  |_|\___/ \__,_|\___|_|  |_| |_| |_| \_\___/ \__,_|\__,_|                
 _____     _          ___                               _____          _ _ _ 
|_   _| __(_)_ __    / _ \ _ __ ___  __ _  ___  _ __   |_   _| __ __ _(_) | |
  | || '__| | '_ \  | | | | '__/ _ \/ _` |/ _ \| '_ \    | || '__/ _` | | | |
  | || |  | | |_) | | |_| | | |  __/ (_| | (_) | | | |   | || | | (_| | | |_|
  |_||_|  |_| .__/   \___/|_|  \___|\__, |\___/|_| |_|   |_||_|  \__,_|_|_(_)
            |_|                     |___/                                    
"""
slow_print(ascii_art_intro, 0.08)
print(" ")
ready = input("Ready to continue? (y/n): ")
#Find and check passengers
ascii_art_car = r"""
Here is your car!
                            ▒▒░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░
                            ▒▒  ░░  ▒▒    ▒▒    ▒▒    ░░  ░░  ░░                                  
                              ▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░                                    
                                  ▒▒                    ▒▒                                        
                              ▓▓▓▓████▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓██████▓▓                                    
                            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                                  
                          ██▒▒▒▒▒▒▒▒██████████████████████████▒▒██                                
                        ▓▓▒▒▒▒▒▒▒▒██░░░░▒▒  ░░██▒▒██░░  ░░▒▒░░██▒▒▓▓                              
                      ██▒▒▒▒▒▒▒▒██░░          ██▒▒██          ░░██▒▒██                            
                    ██▒▒▒▒▒▒▒▒██              ██▒▒██            ████▒▒██                          
        ▒▒██████████████▒▒▒▒██                ██▒▒██            ██▒▒██▒▒██████████████            
  ██████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████▓▓▓▓████████████████████▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████  
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒░░░░▒▒▒▒▒▒▒▒██▒▒░░░░▒▒▒▒▒▒▒▒████▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓▓▓▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒████▓▓▓▓▒▒▒▒▒▒██  
████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▓▓▓▓▓▓▓▓██▒▒▒▒██  
██░░░░██████▒▒▒▒▒▒██▓▓▓▓▒▒▒▒▓▓▓▓██▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██▓▓▓▓▒▒▒▒▓▓▒▒▓▓██████
██░░░░░░░░░░▓▓██████▓▓▒▒░░░░▒▒▓▓██▓▓██▓▓████████████████████████▓▓████████████▓▓▒▒░░░░▒▒▒▒██░░░░██
  ██████████▒▒▒▒▒▒██▓▓▒▒░░░░▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▒▒░░░░▒▒▓▓██████  
            ████████▓▓▓▓▒▒▒▒▓▓▓▓██████████████████████████████████████████████▓▓▓▓▒▒▒▒▓▓▓▓██      
                    ██▓▓▓▓▓▓▓▓██                                              ██▓▓▓▓▓▓▓▓██        
                      ████████                                                  ████████          
"""  
def find_passengers():
  slow_print(ascii_art_car, 0.05)
  print(" ")
  passenger1 = input("Enter first name of wagon leader: ")
  passenger_list.append(passenger1)
  passenger2 = input("Enter first name of first passenger: ")
  passenger_list.append(passenger2)
  passenger3 = input("Enter first name of second passenger: ")
  passenger_list.append(passenger3)
  passenger4 = input("Enter first name of third passenger: ")
  passenger_list.append(passenger4)
  return passenger_list      
passenger_list = []
if ready == 'y':
  find_passengers()
print(passenger_list)

correct_names = input("Is this correct? (y/n): ")
print(" ")
while correct_names != 'y':
    find_passengers()
    correct_names = input("Is this correct? (y/n): ")
    print(" ")
#Packages
package1 = ['15 packs of snacks', 'phone charged to 75%', 'car health 100']
package2 = ['25 packs of snacks', 'phone charged to 25%', 'car health 50']
package3 = ['50 packs of snacks', 'phone charged to 50%', 'car health 25']
ascii_art_box = r"""
+-----------------------------------+
  /                                  /|
/                                  / |
/                                  /  |
+---------------------------------+   |
|                                 |   |
|                                 |   |
|    #########################    |   |
|    #                       #    |   |
|    #                       #    |   |
|    #      +-----------+    #    |   |
|    #      |           |    #    |   |
|    #      |           |    #    |   |
|    #      |  PACKAGE  |    #    |   |
|    #      |           |    #    |   |
|    #      |           |    #    |   |
|    #      +-----------+    #    |   |
|    #                       #    |   |
|    #                       #    |   |
|    #########################    |   |
|                                 |   |
|                                 |   |
|                                 |   |
+---------------------------------+  /
/                                 / /
/                                 / /
+---------------------------------+
"""
slow_print(ascii_art_box, 0.03)
print(" ")
print(f"Package 1: {package1}")
print(f"Package 2: {package2}")
print(f"Package 3: {package3}")
selection = int(input("Select your package!: "))
if selection > 3:
  print("Invalid Package")
else:
    print(f"This is your package: {selection}")
#Check Package
correct_package = input("Is this the correct package? (y/n): ")
def check_package(correct_package):
    while correct_package != 'y':
        slow_print(ascii_art_box, 0.05)
        print(" ")
        print(f"Package 1: {package1}")
        print(f"Package 2: {package2}")
        print(f"Package 3: {package3}")
        selection = int(input("Select your package!: "))
        print(" ")
        print(f"This is your package: {selection}")
        correct_package = input("Is this the correct package? (y/n): ")
while correct_package != 'y':
  check_package(correct_package)
#Set Package
def set_package(input):
  if input == 1:
   return 15, 75, 100
  elif input == 2:
    return 25, 25, 50
  elif input == 3:
    return 50, 50, 25
snacks, phone_charge, car_health = set_package(selection)
print(f"Snacks: {snacks}, Phone Charge: {phone_charge}%, Car Health: {car_health}%")
#Game Begins
ascii_art_begin = r"""
__________________ _______  _______   _________ _______    ______   _______  _______ _________ _        _ 
\__   __/\__   __/(       )(  ____ \  \__   __/(  ___  )  (  ___ \ (  ____ \(  ____ \\__   __/( (    /|( )
  ) (      ) (   | () () || (    \/     ) (   | (   ) |  | (   ) )| (    \/| (    \/   ) (   |  \  ( || |
  | |      | |   | || || || (__         | |   | |   | |  | (__/ / | (__    | |         | |   |   \ | || |
  | |      | |   | |(_)| ||  __)        | |   | |   | |  |  __ (  |  __)   | | ____    | |   | (\ \) || |
  | |      | |   | |   | || (           | |   | |   | |  | (  \ \ | (      | | \_  )   | |   | | \   |(_)
  | |   ___) (___| )   ( || (____/\     | |   | (___) |  | )___) )| (____/\| (___) |___) (___| )  \  | _ 
  )_(   \_______/|/     \|(_______/     )_(   (_______)  |/ \___/ (_______/(_______)\_______/|/    )_)(_)
"""
#Class System
class Passenger:
  def __init__(self, name):
    self.name = name
    self.status = "Fine"
    self.hunger = 100
  def get_name(self):
    return self.name
  def set_status(self, new_status):
    self.status = new_status
  def get_status(self):
    return self.status
  def get_hunger(self):
    return self.hunger
  def set_hunger(self, new_hunger):
    self.hunger = new_hunger

driver = Passenger(passenger_list[0])
passenger_one = Passenger(passenger_list[1])
passenger_two = Passenger(passenger_list[2])
passenger_three = Passenger(passenger_list[3])
passengers = [driver, passenger_one, passenger_two, passenger_three]
Events.Event_list.car_sick()


#Start of the actual game

#Ending