#setting variables for name
firstName = "Andrea"
lastName = "Jimenez"

#using f(format) to insert a variables value into a string
print(f"Hello, {firstName} {lastName}!\n")
print(f"{firstName}, would you like to learn some Python today?\n")

#assigning it to a new varible
newMessage = (f"goodbye, {firstName} {lastName}!\n")
print(newMessage)

#adding the tile method to change the case
print(newMessage.title())
