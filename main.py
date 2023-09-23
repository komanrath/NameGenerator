"""
Concept mapping:

How do things relate?
Input (month, day, year) needs to be matched with a *specific* output. 
This needs to be reproducable (i.e. same input yields same output). So, input and output need to be meaningfully connected, not just randomly connected. 

What needs to be matched with what?
Months need to be matched with a predefined list: each month (int) has a specific (str) counterpart. 12 months means 12 list items.
In the same way, days need to be matched with a predefined list: 31 days, 31 list items. Year should be discounted as a variable (only there for show). 

Crux:
How to match the user input (months & days) with the lists? 
Need to define a function that takes month/day as input and spits out a name as output. 

"""

print("hello, hello")
print("come one, come all")
print("today you will receive a new name; your true name")
Start = input("are your ready to be reborn? * yes / no *  ")
Age = input("what is your date of birth? * month/day/year * ")



