#lets create a program that converts feet and inches to meters
print("I will ask for 2 numbers: your feet first, and then, inches second. So, If you are 5 foot 4 inches, please answer 5 first, and then 4 second.")

#1 foot = 0.3048 meters
#1 inch = 0.0254 meters
feet = int(input("How many feet tall are you?"))
inches = int(input("...and how many inches?"))

#note: the conversion rates are "HARD-CODED" - A fixed value in the code, cannot be changed.
#Math happens on right side of equal side
#Remember PEMDAS
meters = (feet * 0.3048) + (inches * 0.0254)

print("In meters, you are: " + str(meters) + " tall.")

apples = (meters / 0.06)

print("You are: " + str(apples) + " tall.")

#str --> "String"
#float --> decimal number