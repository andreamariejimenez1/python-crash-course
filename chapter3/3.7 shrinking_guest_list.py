# GOAL: use pop to remove people from list and print a message to them
# then use delete to make your list empty

# creating my list
myGuest = ['Ana', 'Jackie', 'Blaine', 'Andrea']

# priting invitation for each guest
for people in myGuest:
  print('Hello ' + people + ', join me for dinner.')
print()

# using pop and printing a message to them
print(f'Hello {myGuest.pop()}, you cannot come lol.')
print(f'Hello {myGuest.pop()}, you cannot come lol.')
print()

# printing invitation to the people left in my list
for people in myGuest:
  print('Hello ' + people + ', join me for dinner.')
print()

# using delete and printing my list to check if its empty
del myGuest[1]
del myGuest[0]
print(myGuest)

# NOTES:
#
#  does not work: 
# del myGuest[0]
# del myGuest[1]
#
# does work:
# del myGuest[0]
# del myGuest[0]
#
# does work:
# del myGuest[0:2]
