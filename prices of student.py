""" finding out if the user is a student and determine what price to pay """


age = int(input("How old are you?"))
if age > 13:
    student = input("Are you a student? (y/n)")
    if student == "y":
        print ("$8")
    elif age >= 18:
        print ("$12")
    else:
        print("$9")
elif age >= 5:
    print("$7")
else:
    print("free")

