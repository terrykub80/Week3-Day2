import math

def circle_area():
    ask = input("What is your circle's radius in centimeters? ")
    area = math.pi * float(ask)
    print(f"The area of your circle is {area}!")

def hypot():
    side1 = input("How many inches is the first side? ")
    side2 = input("Thanks! Now how many inches is the second side? ")
    hypotenuse = math.sqrt(int(side1)**2 + int(side2)**2)
    print(f"The hypotonuse of your triangle is {hypotenuse} inches!")




