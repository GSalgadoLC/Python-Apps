# List comprehension

data = [3, 5, 7, 9]

data = [x+3 for x in data]
print("Creating a new list", data)


# Dictionary comprehension

months = ["Jan", "Feb", "Mar", "Apr", "May", "June",
          "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

numdict = {x: x**2 for x in number}
print("Using one input list to create dict: ", numdict)

calendar = {key: value for (key, value) in zip(number, months)}
print("Using two lists: ", calendar)


# Set comprehension

set_a = {x for x in range(10, 20) if x not in [11, 13, 14, 16, 17, 19]}
print(set_a)


# Generator comprehension

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")


# Other
print()
z = ["alpha", "bravo", "charlie"]
new_z = [i[0]*2for i in z]
print(new_z)


print()
a = [[96], [69]]

print(''.join(list(map(str, a))))
