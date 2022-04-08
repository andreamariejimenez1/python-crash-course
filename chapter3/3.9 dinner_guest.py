# GOAL: USE LEN()

myGuest = ['Ana', 'Jackie', 'Blaine', 'Andrea']

# using a for loop to print greeting
for name in myGuest:
  print("Hello " + name + ".")

# using len() in format
print(f'\nI am inviting {len(myGuest)} people')

# assigning len() to a variable and casting numPeople to str
numPeople = len(myGuest)
print('I am inviting ' + str(numPeople) + ' people')

# using variable in format
print(f'I am inviting {numPeople} people')
