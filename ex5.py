# a variable containing the string Zed. A. Shaw
name = 'Zed A. Shaw'

# one inch equals 2.54 centimeters. remember, a variable or class much be defined before using.
inches_to_cm = 2.54

# one pound = 0.453592 kilos.
lb_to_kg = 0.453592
# a variable containing the number 35
age = 35 # not a lie
# a variable containing the number 74
height = 74 * inches_to_cm # inches
# a vaiable containing the number 180
weight = 180 * lb_to_kg # lbs
# a variable containing the string Blue.
eyes = 'Blue'
# a variable containing the string White.
teeth = 'White'
# a variable containing the string 'Brown'
hair = 'Brown'



# the f before the string tells Python 3 that this is a format string
# a format string contains embedded variables whose values are placed in the string when printed
# "Let's talk about Zed A. Shaw." will be printed
print(f"Let's talk about {name}.")
# another format string which will print "He's 74 inches tall."
print(f"He's {height} inches tall.")
# a format string which prints: "He's 180 pounds heavy."
print(f"He's {weight} pounds heavy.")
# the string "Actually, that's not too heavy." is printed
print("Actually, that's not too heavy.")
# a format string which prints: "He's got Blue eyes and Brown hair."
print(f"He's got {eyes} eyes and {hair} hair.")
# a format string which prints: "His teeth are usually White depending on the coffee."
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right.
# the sum of these values is stored in the variable total.
total = age + height + weight
# a format string which prints the values three variables defined earlier along with their sum:
# "If I add 35, 74, and 180 I get 289."
print(f"If I add {age}, {height}, and {weight} I get {total}.")
