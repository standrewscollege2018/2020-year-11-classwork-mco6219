""" this program will be used for a silent auction to find the highest bidder """

# asking for seller name and item
auction_item = input("What is the item you are putting up for sale?")
reserve = int(input("What is the reserve price?"))
highest_bid = 0
highest_name = ""

# set up Boolean
keep_asking = True

# asking for user name, price they're willing to pay, highest bidder and highest price and set while loop
while keep_asking == True:
    
    try:
        user_name = input("What is your name?")
        bid = int(input("What are you willing to pay for this item?"))
        
        if:
            bid == -1
            print("The auction for {} has now finished and the winner of the {} is {} with a bid of ${}".format(auction_item, auction item, highest_name, highest_bid)
        elif bid > highest_bid:
            print("You are now the highest bidder")
    
        else bid < highest_bid:
            print("The highest bidder is {} with a bid of ${}".format(highest_name, highest_bid))
        
        except:
            pass 
            