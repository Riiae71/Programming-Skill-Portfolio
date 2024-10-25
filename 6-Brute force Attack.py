#correct password
password="12345"
#the amount of attempts(fixed loop)
max_inputs=5
inputs=0
while inputs < max_inputs:
    user_input=input("Write you password:")
    #correct input
    if user_input==password:
        print("Welcome user!")
        break#stop the code after correct answer
    else:#wrong codes and amount of attempts
        inputs +=1
        remaining_tries=max_inputs - inputs
        print(f"Try again,You have {remaining_tries} tries left")
#if all attempts are done the authorities will be informed
        if inputs==max_inputs:
            print("All attempts are reached,Authority has been alerted!")