""" this program will run a simple raffle draw and produce a winner """

# set list to store movies
raffle = []
import random
# print intro and questions
print("Welcome to the raffle")
raffle_item = input("Enter the raffle item that's up for grabs:\n")
raffle_value = int(input("Enter the raffle prize value:\n"))

stop_options = ["end", "stop"]

# set boolean
keep_asking = True

# asking for names of entrants
while keep_asking == True:
    name = input("What is your name to enter for the raffle?\n")
    
    # if the name = end or stop then stop asking for another name
    if name.lower() in stop_options:
        keep_asking = False
        
    # if name doesn't equal end or stop then add the name to the list
    else:
        raffle.append(name)
 
# len(raffle) is asking how many items are in the list, and the -1 afterwards is saying how many items are in the list minus 1 equals the numbers randomint has to choose from   
winner = random.randint(0,len(raffle)-1)
print(raffle[winner])
        

    
    
        