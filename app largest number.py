largest = None
number_list = [1, 73, 8, 65, 83, 2, 86, 234, 76, 231, 23, 167]

for number in number_list:
    if largest is None or number > largest:
        print('loop', number, largest)
        largest = number

print("Largest number", largest)
print()
print(max(number_list))
print()

n = 5
while n != 0:
    print(n, "\n")
    n = n-1

print("Blastoff! \n")


while True:
    line = input('>')
    if line == ("done"):
        break
    print(line)
print("DONE!")
