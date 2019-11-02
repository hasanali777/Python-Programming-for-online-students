'''#QUESTION_1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
#QUESTION_2
import platform
print("version of python language is: ",platform.sys.version)
#QUESTION_3
import datetime
print("current date and time is: ",datetime.datetime.now())
#QUESTION_4
import math
# BY RADIUS
r = int(input("enter radius of circle: "))
area = math.pi * r**2
print("Area of circle by radius ",area)
# BY DIAMETER
d = int(input("enter diameter of circle: "))
area = math.pi/4 * d**2
print("Area of circle by diameter ",area)
# BY CIRCUMFERENCE
c = int(input("enter circumference of circle: "))
area = c**2/4*math.pi
print("Area of circle by circumference ",area)
#QUESTION_5
f_name = input("enter first name: ")
l_name = input("enter last name: ")
full_name = f_name+" "+l_name
print("User name in reverse order with space between them  "+" ".join(reversed(full_name)))
#QUESTION_6
input_1 = int(input("enter first value: "))
input_2 = int(input("enter second value: "))
addition = input_1+input_2
print("The calculated result of addition of two inputs are: ",addition)'''