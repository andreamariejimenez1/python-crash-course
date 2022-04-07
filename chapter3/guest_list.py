# GOAL: MAKE A LIST OF PEOPLE AND PRINT A MESSAGE TO EACH PERSON INVITING THEM TO DINNER

myGuest = ['Ana', 'Jackie', 'Blaine', 'Andrea']
firstPart = "Hello "
secondPart = ", I would like to invite you to dinner."

print(firstPart + myGuest[0] + secondPart)
print(firstPart + myGuest[1] + secondPart)
print(firstPart + myGuest[2] + secondPart)
print(firstPart + myGuest[3] + secondPart)

print()

print(f'Goodbye {myGuest[0]}')
print(f'Goodbye {myGuest[1]}')
print(f'Goodbye {myGuest[2]}')
print(f'Goodbye {myGuest[3]}')

# OPTIONAL: USE A FOR LOOP
# for name in myGuest:
#   print("Hello " + name + ".")
