# GOAL: ADD MORE PEOPLE TO THE LIST 
# ADD TO THE BEGINNING, MIDDLE, END

myGuest = ['Ana', 'Jackie', 'Blaine', 'Andrea']

for people in myGuest:
  print('Hello ' + people + ', join me for dinner.')

print('\nI have found a bigger dinner table, so I will be inviting more people\n')

myGuest.insert(0, 'Bob')
myGuest.insert(3, 'Jack')
myGuest.append('Jill')

for people in myGuest:
  print('Hello ' + people + ', join me for dinner.')
