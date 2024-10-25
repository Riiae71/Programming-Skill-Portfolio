#list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#user input
user_input = input("Enter the desired name to pick from the list: ")

#condition if it is present in the list or not
if user_input in names:
    print(f"{user_input} is in the list!")
else:
    print(f"{user_input} is not in the list.")