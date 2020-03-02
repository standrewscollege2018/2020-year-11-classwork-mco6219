""" this program will run a simple raffle draw and produce a winner """

# set list to store movies
raffle = []

# print intro and questions
print("Welcome to the raffle")
raffle_item = input("Enter the raffle item that's up for grabs:\n")
raffle_value = int(input("Enter the raffle prize value:\n"))

# set boolean
keep_asking = True


while keep_asking == True:
    name = input("What is your name to enter for the raffle?\n")
    
    if name == "end" or "stop":
        keep_asking = False
        
    else:
        raffle.append(name)
        

        

    
    
        