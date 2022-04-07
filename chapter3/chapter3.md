# INTRODUCING LISTS
- learn what list are and how to work with elements in a list
- list allow you to store sets of information in one place
- list: "a collectio of items in a particular order"

# NOTES

Adding to the end of a list:
list.append('element')

Inserting an element into a list (where 0 represents an index):
list.insert(0,'element')


Removing from a list:
del list[0] -- deletes an element and no longer have access 
list.pop -- removes or pops the last element in list
list.pop(#) -- pops an element from the specified index  
list.remove('element') -- remove when we don't know the index of the value -- removes only the first occurance of this value

Sorting a list alphabetically permanently:
list.sort -> print(list)

Sorting a list reversed alphabetically permanently:
list.sort(reverse=True) -> print(list)

Sorting a list temporarily: 
print(sorted(list))
- can also temporarily reverse alphabetically

Printing a list in reverse order:
list.reverse() -> print(list)

Finding the length: 
len(list) -> starts with 1 

