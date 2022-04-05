#GOAL: CREATE A LIST AND PRINT EACH ELEMENT WITH A MESSAGE

names = ['Andrea', 'Jesus', 'Dani', 'Janet', 'Flor']
message = "Hello,"

print(f"{message} {names[0]}!")
print(f"{message} {names[1]}!")
print(f"{message} {names[2]}!")
print(f"{message} {names[3]}!")
print(f"{message} {names[4]}!")
print()

#modifying elements in a list
# names[0] = 'me'
# print(f"{message} {names[0]}!")
# print(f"{message} {names[1]}!")
# print(f"{message} {names[2]}!")
# print(f"{message} {names[3]}!")
# print(f"{message} {names[4]}!")
# print()

#appending elements to the end of a list
names.append('Alicia')
print(f"{message} {names[0]}!")
print(f"{message} {names[1]}!")
print(f"{message} {names[2]}!")
print(f"{message} {names[3]}!")
print(f"{message} {names[4]}!")
print(f"{message} {names[-1]}!")
print()

#inserting elements into a list
#all elements shift to the right since I am adding Jesie to index 0
names.insert(0, 'Jesie')
print(names)

del names[0]
print(names)
