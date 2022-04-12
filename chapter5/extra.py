# WRITE A SERIES OF CONDITIONAL TEST
# PRINT YOUR PREDICTION

requestedT = ['mushrooms', 'onions',                  'pineapple']
print('mushrooms' in requestedT)
print('pepperoni' in requestedT)

new = 'veggies'
if new not in requestedT:
  print(f'{new.title()} not found...')

if 'veggies' not in requestedT:
  print('veggies not found...\n')


# EQUALITY (==)
name = 'Andrea'

print("Is name == 'Andrea' ? \nI predict True.")
print(name == 'Andrea')

print("\nIs name != 'Andrea' ? \nI predict True.")
print(name != 'Andrea')

# USING LOWER
print("\nIs name.lower() == 'andrea' ? \nI predict True.")
print(name.lower() == 'andrea')
