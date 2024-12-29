
#menu of different noodles
Menu = {
    1 : {"Name":"Top Ramen", "Category":"Nissin", "Price":5.00,  "Stock":10},#stocks included
    2 : {"Name": "Indomie Chicken Curry Noodles", "Category":"Indomie", "Price":5.00,  "Stock":10},
    3 : {"Name": "Indomie Fried Noodles", "Category":"Indomie","Price":5.00,  "Stock":10},
    4 : {"Name": "Kikkoman Soba Ramen", "Category":"Kikkoman","Price":7.00,  "Stock":10},
    5 : {"Name": "Buldak Lime and chilly Ramen", "Category":"Samyang","Price":7.00,  "Stock":10},
    6 : {"Name": "Buldak Extra spicy Ramen", "Category":"Samyang","Price":6.00,  "Stock":10},
    7 : {"Name": "Buldak Carbonara Ramen ", "Category":"Samyang","Price":6.00,  "Stock":10},
    8 : {"Name": "Lacnor Chocolate Milk", "Category":"Drinks", "Price":1.00,  "Stock":10},
    9 : {"Name": "Alokozay Cappucino", "Category":"Drinks", "Price":1.00,  "Stock":10},
    10 : {"Name": "Al Ain Water", "Category":"Drinks", "Price":1.00,  "Stock":10},
    11 : {"Name": "Egg", "Category":"Topping", "Price":1.00,  "Stock":10},
    12 : {"Name": "Sausage", "Category":"Topping","Price":1.00,  "Stock":10},
    13 : {"Name": "String Cheese", "Category":"Topping","Price":1.00,  "Stock":10}
}
#display function
def display():
    print("Menu displayed:")
    for code, item in Menu.items():
        if item["Stock"] > 0:#check if item is in stock
         print(f"{code}. {item['Name']} -${item['Price']:.2f}")

#selection function
def select():
  while True: 
    try:
        choose=int(input("\nHello beautiful! Choose your desired Item!"))#user inputs their item
        if choose in Menu and Menu[choose]["Stock"]>0:
            return choose
        else:
          print("Sorry but this product is unavailable! Please choose another item.")
    except ValueError:
         print("Invalid code! Please try again.")

#money insertion function
def insertmoney():
   while True:
     try:
         money=float(input("\nEnter money: $"))#float datatype
         if money <=0:
            print("Please enter money") 
         else:
            return money    
     except ValueError:
        print("Please enter real money!")

#reciept or total function
def totalamt(code,money):
   item = Menu[code]
   if money>= item['Price']:
      change= money - item["Price"]
      item['Stock'] -=1#remove the item from stock each time
      return True,change
   else:
      return False, item['Price'] - money

#additional item function   
def additem(cart):
   while True:#while loop for additional items 
      try:
         new =input("\nDo you want to add another item? yes or no: ").lower()
         if new == 'no':
            break
         elif new == 'yes':
            display()
            item = select()
            cart.append(item)
         else:
            print('Please enter yes or no')
      except ValueError:
         print("Please try again.")

#overall vending machine's function 
def vending_machine():
   while True:
      cart=[]
      display()

      itemsel=select()
      cart.append(itemsel)

      moneyin=insertmoney()

      done,change=totalamt(itemsel,moneyin)

      if done:
         item= Menu[itemsel]
         print(f"\nDispensing {item['Name']}...")
         print(f"Enjoy your {item['Name']} pookie!") 
         print(f"Your change is: ${change:.2f}")
      else: 
         print(f"\nInsert more money. You lack ${change:.2f} more!")
         print(f"Money inserted: ${moneyin:.2f}") 
         continue

      again=input("\nDo you want to buy something else? yes/no").lower()
      if again !='yes':
         print("\nThank you for using our vending machine! Enjoy your day!") 
         break

#calling all functions in the code.
if __name__ =="__main__":
   vending_machine()


