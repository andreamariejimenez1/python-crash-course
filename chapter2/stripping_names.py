# GOAL: REMOVE WHITESPACE CHARACTERS FROM A NAME

firstName = "\tAndrea \n"

#printing the original variable with whitespaces
print(firstName)

#this is going to remove the newline after Andrea
print(firstName.rstrip())

#this is going to remove the tab at the front of Andrea
print(firstName.lstrip())

#this is going to remove the tab at the front and newline at the end
print(firstName.strip())
