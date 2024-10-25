#the dictionary which displays the name,hometown and age.
biography = { 'Name' : 'Rida',
              'Hometown' : 'Islamabad',
               'Age' : 18}
for key, value in biography.items():
    print(f"{key}:{value}")#all the keys and their respective values will pe printed!
#Advanced requirements
#user will input their first and second names
name1=input("Write your first name: ")
name2=input("Write your second name: ")
#user will input their hometowns
hometown=input("write your hometown: ")
#If the user does not put integer value error will be displayed
#the try-except blocks help identify an error
try:
   age=int(input("Write your age: "))
   print(f"Your name is {name1} {name2} who is {age} years old living in {hometown}")
except ValueError:
    print("Age should be numeric")