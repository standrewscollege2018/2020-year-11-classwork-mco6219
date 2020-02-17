""" this program will ask the user to enter how many names to ask for, then ask that many times for a name """

# asking user for input
number = int(input("How many names do you want to enter?"))

# setting for loop
for i in range (0,number):
    name = input("Enter name")
    print("Hello", name)

