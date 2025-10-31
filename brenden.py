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

package1 = ['15 packs of snacks', 'phone charged to 75%', 'car health 100']
package2 = ['25 packs of snacks', 'phone charged to 25%', 'car health 50']
package3 = ['50 packs of snacks', 'phone charged to 50%', 'car health 25']
print(f"Package 1: {package1}")
print(f"Package 2: {package2}")
print(f"Package 3: {package3}")
selection = int(input("Select your package!: "))
if selection > 3:
  print("Invalid Package")
else:
    print(f"This is your package: {selection}")
#Check Package
correct_package = input("Is this the correct package? (please enter y or n): ")
def check_package(correct_package):
    while correct_package != 'y':
        print(package1)
        print(package2)
        print(package3)
        print(f"This is your package: {selection}")
        selection = int(input("Select your package!: "))
        correct_package = input("Is this the correct package? (please enter y or n): ")
#Set Package
def set_package(selection):
  if input == 1:
    snacks = 15
    phone_charge = 75
    car_health = 100
  elif input == 2:
    snacks = 25
    phone_charge = 25
    car_health = 50
  elif input == 3:
    snacks = 50
    phone_charge = 50
    car_health = 25

ascii_art_box = """
+-------------------------------------------+
  /                                          /|
 /                                          / |
/                                          /  |
+------------------------------------------+   |
|                                          |   |
|   #####################################  |   |
|   #                                   #  |   |
|   #   +---------------------------+   #  |   |
|   #   |                           |   #  |   |
|   #   |                           |   #  |   |
|   #   |          ████████         |   #  |   |
|   #   |         ███   ███         |   #  |   |
|   #   |        ███     ███        |   #  |   |
|   #   |        ███  C  ███        |   #  |   |
|   #   |        ███  R  ███        |   #  |   |
|   #   |        ███  A  ███        |   #  |   |
|   #   |        ███  T  ███        |   #  |   |
|   #   |        ███  E  ███        |   #  |   |
|   #   |         ███   ███         |   #  |   |
|   #   |          ████████         |   #  |   |
|   #   |                           |   #  |   |
|   #   +---------------------------+   #  |   |
|   #                                   #  |   |
|   #####################################  |   |
|                                          |   |
|                                          |   |
|                                          |   |
|                                          |   |
|                                          |   |
+------------------------------------------+  /
/                                          / /
/                                          / /
+------------------------------------------+
"""
print(ascii_art_box)