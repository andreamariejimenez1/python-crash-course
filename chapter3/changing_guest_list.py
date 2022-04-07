# GOAL: MAKE A LIST OF PEOPLE AND PRINT A MESSAGE TO EACH
# PERSON INVITING THEM TO DINNER. BUT THIS TIME YOU JUST 
# FOUND OUT THAT ONE OF THE GUEST CAN'T MAKE IT.
# PRINT A MESSAGE ABOUT THAT PERSON.
# MODIFIY THE LIST AND PRINT NEW INVITATIONS AGAIN

# creating list and messages 
myGuest = ['Ana', 'Jackie', 'Blaine', 'Andrea']
firstPart = "Hello "
secondPart = ", I would like to invite you to dinner."

# printing invitation
print(firstPart + myGuest[0] + secondPart)
print(firstPart + myGuest[1] + secondPart)
print(firstPart + myGuest[2] + secondPart)
print(firstPart + myGuest[3] + secondPart)
print()

# printing the person that cannot make it 
print(f'{myGuest[3]} cannot make it to dinner.\n')

# removing Andrea assuming we don't know the index
myGuest.remove('Andrea')

# or we can delete with the index
# del myGuest[3]

# modifiying the list 
myGuest.append('Somebody else')

# printing new invitations
print(firstPart + myGuest[0] + secondPart)
print(firstPart + myGuest[1] + secondPart)
print(firstPart + myGuest[2] + secondPart)
print(firstPart + myGuest[3].title() + secondPart)
