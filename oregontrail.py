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
ascii_art_intro = """
__        __   _                            _                                    
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___                              
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \                             
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |                            
 __\_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/       _   _____     _       
|  \/  | ___   __| | ___ _ __ _ __   |  _ \ ___   __ _  __| | |_   _| __(_)_ __  
| |\/| |/ _ \ / _` |/ _ \ '__| '_ \  | |_) / _ \ / _` |/ _` |   | || '__| | '_ \ 
| |  | | (_) | (_| |  __/ |  | | | | |  _ < (_) | (_| | (_| |   | || |  | | |_) |
|_|__|_|\___/ \__,_|\___|_|  |_| |_|_|_|_\_\___/ \__,_|\__,_|   |_||_|  |_| .__/ 
 / _ \ _ __ ___  __ _  ___  _ __   |_   _| __ __ _(_) | |                 |_|    
| | | | '__/ _ \/ _` |/ _ \| '_ \    | || '__/ _` | | | |                        
| |_| | | |  __/ (_| | (_) | | | |   | || | | (_| | | |_|                        
 \___/|_|  \___|\__, |\___/|_| |_|   |_||_|  \__,_|_|_(_)                        
                |___/                                                                                                                       
"""
slow_print(ascii_art_intro, 0.08)
ready = input("Ready to continue? (please enter y or n): ")
#Find and check passengers
def find_passengers():
  slow_print(ascii_art_car, 0.05)
  passenger1 = input("Enter first name of wagon leader: ")
  passenger_list.append(passenger1)
  passenger2 = input("Enter first name of first passenger: ")
  passenger_list.append(passenger2)
  passenger3 = input("Enter first name of second passenger: ")
  passenger_list.append(passenger3)
  passenger4 = input("Enter first name of third passenger: ")
  passenger_list.append(passenger4)
  return passenger_list
ascii_art_car = """
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
passenger_list = []
if ready == 'y':
  find_passengers()
print(passenger_list)

correct = input("Is this correct? (please enter y or n): ")
while correct != 'y':
    find_passengers()
    correct = input("Is this correct? (please enter y or n): ")
#
ascii_art_begin = """
 _____ _                  _          _                _       _ 
|_   _(_)_ __ ___   ___  | |_ ___   | |__   ___  __ _(_)_ __ | |
  | | | | '_ ` _ \ / _ \ | __/ _ \  | '_ \ / _ \/ _` | | '_ \| |
  | | | | | | | | |  __/ | || (_) | | |_) |  __/ (_| | | | | |_|
  |_| |_|_| |_| |_|\___|  \__\___/  |_.__/ \___|\__, |_|_| |_(_)
                                                |___/           
"""
ascii_art_begin2 = """
__________________ _______  _______   _________ _______    ______   _______  _______ _________ _        _ 
\__   __/\__   __/(       )(  ____ \  \__   __/(  ___  )  (  ___ \ (  ____ \(  ____ \\__   __/( (    /|( )
   ) (      ) (   | () () || (    \/     ) (   | (   ) |  | (   ) )| (    \/| (    \/   ) (   |  \  ( || |
   | |      | |   | || || || (__         | |   | |   | |  | (__/ / | (__    | |         | |   |   \ | || |
   | |      | |   | |(_)| ||  __)        | |   | |   | |  |  __ (  |  __)   | | ____    | |   | (\ \) || |
   | |      | |   | |   | || (           | |   | |   | |  | (  \ \ | (      | | \_  )   | |   | | \   |(_)
   | |   ___) (___| )   ( || (____/\     | |   | (___) |  | )___) )| (____/\| (___) |___) (___| )  \  | _ 
   )_(   \_______/|/     \|(_______/     )_(   (_______)  |/ \___/ (_______/(_______)\_______/|/    )_)(_)
"""
slow_print(ascii_art_begin2, 0.08)


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

Events.car_sick()