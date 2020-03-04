""" this program will run a booking system for the university cars so students can hire cars and see which vehicles are available and how many seats they have"""

# list of vehicles and vehicle details of availability and seat numbers
car_names = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsubishi Airtrek", "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ace"]
seats = [2, 4, 4, 4, 4, 4, 7, 12, 12]
available = [True, True, True, True, True, True, True, True, True] 
bookings = []
running = True
# keep running the qestion until the user puts in -1
while running == True:
    
    # asking user input for how many seats they need
    seats_car = int(input("How many seats do you need?\n"))
    
    # if user says -1 end program
    if seats_car == -1:
        running = False
        
        # print list of who has booked cars
        print(bookings)      
   
    else:    
        # display all cars and car details
        for i in range (len(car_names)):
            print("{}. {}, seats {}, available {}.".format (i + 1, car_names[i], seats[i], available[i]))
            
        # get user to input the number of the car they want
        selected_car = int(input("What is the number of the car you would like to borrow for today?\n"))
    
        # change availability of selected car
        available[selected_car-1] = False
        
        # ask for user name and match with car of choice and print line of what car is booked and by who
        customer_name = input("What is your name?\n")
        book = print("{} has booked the {} for today".format(customer_name, car_names[selected_car]))
        bookings.append("{} has booked the {} for today".format(customer_name, car_names[selected_car]))
       
    