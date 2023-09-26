"""
Concept mapping:

How do things relate?
Input (month, day, year) needs to be matched with a *specific* output. 
This needs to be reproducable (i.e. same input yields same output). So, input and output need to be meaningfully connected, not just randomly connected. 

What needs to be matched with what?
Months need to be matched with a predefined list: each month (int) has a specific (str) counterpart. 12 months means 12 list-items.
In the same way, days need to be matched with a predefined list: 31 days, 31 list-items. Year should be discounted as a variable (only there for show). 

Crux:
How to match the user input (months & days) with the lists? 
Need to define a function that takes month/day as input and spits out a name as output. 

1. Maybe take user input and use it in combination with a print function to print corresponding name?
    - i.e. if user input for day is 10, then print(Names_Day[10]). How to link the two?

"""

import sys

print("hello, hello")
print("come one, come all")
print("today you will receive a new name; your true name")
Start = input("are your ready to be reborn? * yes / no *  ")
if Start == "yes":
   print("excellent, continue")
else: 
   print("shame, you will never know your true name")
   sys.exit()
Birth_Day = int(input("what day were you born? "))
Birth_Month = int(input("what month were you born? "))
Generate = input("Press enter for your new name")




