str_to_reverse = "Limes are green"
iteration = len(str_to_reverse)-1

for letter in str_to_reverse:
    print(str_to_reverse[iteration])
    iteration -= 1

# This is my first though on how I would perform string reversal.
# I first find how many letters/characters are in the string and subtract 1
# We can now use to index the string without going out of the range
# Now we use a for loop and start with the last index of the string and print
# We subtract 1 until we have printed the entire string
