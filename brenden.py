
#Slow Print Function
import time
def slow_print(ascii_art,speed):
  for line in ascii_art.strip().split('\n'):
    print(line)
    time.sleep(speed)

#Find Passengers
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

#Find Package
def find_package():
    package1 = ['15 packs of snacks', 'phone charged to 75%', 'car health 100']
    package2 = ['25 packs of snacks', 'phone charged to 25%', 'car health 50']
    package3 = ['50 packs of snacks', 'phone charged to 50%', 'car health 25']
    print(package1)
    print(package2)
    print(package3)
    selection = int(input("Select your package!: "))
    return f"This is your package: {selection}"

#Check Package
def check_package(correct_package):
    while correct_package != 'y':
        print(package1)
        print(package2)
        print(package3)
        print(f"This is your package: {selection}")
        selection = int(input("Select your package!: "))
        correct_package = input("Is this the correct package? (please enter y or n): ")
#Set Package
def set_package(input):
  if input == 1:
   return 15, 75, 100
  elif input == 2:
    return 25, 25, 50
  elif input == 3:
    return 50, 50, 25
snacks, phone_charge, car_health = set_package(selection)

ascii_art_box = """
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

ascii_art_car = r"""
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