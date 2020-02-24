
""" this program demonstrates how lists work, including how to print, change and append items """

# lists always have square brackets. items are separated by commas
fruit = ["apples", "bananas", "pineapple", "oranges"]

# to print an item from a list, we use the name of the list and its index (which starts at 0)
print(fruit[3])

# to change an item, just use its index and set it directly
fruit[0] = "mango"
print(fruit)

# to insert an item at a specific locstion, use insert(index, item)
fruit.insert(3, "apples")
print(fruit)

# often it's just easier to add a new item to the end of the list
# to do this we use append
fruit.append("guavas")
print(fruit)

