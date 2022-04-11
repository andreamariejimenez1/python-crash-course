pizzas = ['cheese', 'pepperoni', 'supreme']

friends_pizzas = pizzas[:]

pizzas.append('veggie')
friends_pizzas.append('mushroom')

print('My favorite pizzas are:')
for pizza in pizzas:
  print(pizza.title())

print('\nMy freinds favorite pizzas are:')
for pizza in friends_pizzas:
  print(pizza.title())
