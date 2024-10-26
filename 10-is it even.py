def check_even_odd(number):
    """Determine if a number is even or odd and return a message."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():#main funtion
    # Ask the user for a number
    user_input = input("Enter a number: ")
    
    # Convert the input to an integer
    try:
        number = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Call the function and get the result
    result = check_even_odd(number)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()