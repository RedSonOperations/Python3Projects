import math
print("Hello world.")
#user input for simple miles to km calculator
#miles=input("How many miles? ")
miles = 6
#since inputs are always strings, convert to type desired
km = miles * 1.60934
print("{} miles equals {} kilometers".format(miles, km))

var1, operator, var2 = input("Enter Calculation: ").split()
var1 = int(var1)
var2 = int(var2)
if operator == "+":
    print("{} + {} = {}".format(var1, var2, var1 + var2))
elif operator == "-":
    print("{} - {} = {}".format(var1, var2, var1 - var2))
elif operator == "*":
    print("{} * {} = {}".format(var1, var2, var1 * var2))
elif operator == "/":
    print("{} / {} = {}".format(var1, var2, var1 / var2))
elif operator == "^":
    print("{} ^ {} = {}".format(var1, var2, math.pow(var1, var2)))
else:
    print("Use one of the following operators: + - * /")

