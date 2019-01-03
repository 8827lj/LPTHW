# variable declaration containing a value of 10
types_of_people = 10

# an f-string or format string which utilizes variables defined in your script.
# the value of the embedded variable is replaced when the string is printed.
x = f"There are {types_of_people} types of people."

# variable containing the string "binary"
binary = "binary"

# a variable containing the string "don't"
do_not = "don't"

# a variable containing a f-string. within the f-string, two other string variables are present.
y = f"Those who know {binary} and those who {do_not}."

# the variable x, an f-string, is printed. "There are 10 types of people."
print(x)

# the variable y, an f-string, is printed. "Those who know binary and those who don't."
print(y)

# an f-string, containing the variable x, is printed. "I said: There are 10 types of people."
print(f"I said: {x}")

# an f-string containing the variable y, is printed. the content of the variable y is also enclosed in single quotes.
# "I also said: 'Those who know binary and those who don't'."
print(f"I also said: '{y}'")

# hilarious is a variable set equal to the Boolean value of False. "False" is a Python keyword!
hilarious = False

# the variable joke_evaluation is an f-string which contains an empty format.
# ANY defined variable can be passed to this format and it will be printed with the string.
joke_evaluation = "Isn't that joke so funny?! {}"

# it appears that functions are also objects in Python?! joke_evaluation appears to call format()
# the format() function is invoked and the variable hilarious is passed as an argument to be formatted.
# the print function is invoked and the resulting, formatted string is passed to be printed.
# "Isn't that joke so funny?! False"
print(joke_evaluation.format(hilarious))

print(joke_evaluation.format(binary))

print(joke_evaluation.format(types_of_people))


# a string variable is defined
w = "This is the left side of..."

# a string variable is defined
e = "a string with a right side."

# the two string variables are joined via concatenation.
print(w + e)
