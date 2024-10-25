#this is a dictionary of months in a year
months={"January": 31,
        "February": 28,
       "March": 31,
       "April":30,
       "May": 31,
       "June":30,
       "July":31,
       "August":31,
       "September":30,
       "October":31,
       "November":30,
       "December":31,
}
#asking user to choose a month
choose=input("choose a month of the year:")
if choose in months:#connecting the user input and our dictionary
   if choose=="February":#leap year code
     leap=input("is it a leap year")#leap year variable
     if leap=="yes":
       print("February has 29 days in a leap year")
     else:
       print("february has 28 days in a normal year")
if choose in months:#normal year
    print(f"The month of {choose} has {months[choose]} days in a year")
else:
  print("This not a valid month")