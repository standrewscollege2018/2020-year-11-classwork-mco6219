""" this program will ask for a number between 5 > 10 and will continue to ask until the user guesses the correct number """

# set number and set Boolean to true
keep_asking = True

# Start asking for number guesses
while keep_asking == True:
    num = int(input("Pick a number below 20"))
    if num == 7 :
        keep_asking = False
    else:
        print("Wrong number!")
        
print("You guessed the right number!")
    





