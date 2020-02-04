""" This program gets an item name and price, then adds GST to the price """

# Set the GST to 15%
# Because GST is constant we name it in uppercase
GST = 0.15

# get the name and price
item_name = input("Item name?")
item_price = float("Item price?")

# print the name and item of the price including GST
print("The", item_name, "will cost",  