myLocations = ['Arizona', 'New York', 'Colorado', 'Hawaii', 'Texas']

# printing orignal list
print(myLocations)

# temp. sorting A-Z
print(sorted(myLocations))

# printing orignal list again
print(myLocations)

# temp. sorting Z-A
print(sorted(myLocations, reverse=True))

# printing orignal list again
print(myLocations)

print()

# printing list in reverse
myLocations.reverse()
print(myLocations)
# why does this give none: print(myLocations.reverse())

# printing list in reverse (original)
myLocations.reverse()
print(myLocations)

print()

# sorting list permanently A-Z
myLocations.sort
print(myLocations)
# why this no work: print(myLocations.sort)

# sorting list permanently Z-A
myLocations.sort(reverse=True)
print(myLocations)
