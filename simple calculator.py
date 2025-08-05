# Define the calculator function
def calculator():
    # Start an infinite loop so the calculator keeps running
    while True:
        # Ask the user to choose an operation or quit
        op = input("\nChoose (+, -, *, /) or 'q' to quit: ")

        # If the user types 'q', exit the loop
        if op == 'q':
            print("Goodbye!")
            break  # Exit the while loop

        # Check if the entered operation is valid
        if op not in ['+', '-', '*', '/']:
            print("Invalid operation!")
            continue  # Go back to the top of the loop

        # Try to get two numbers from the user
        try:
            num1 = float(input("First number: "))  # Get the first number
            num2 = float(input("Second number: ")) # Get the second number
        except:
            # If the input isn't a valid number, show error
            print("Invalid number input!")
            continue

        # Perform the selected operation
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            # Handle divide-by-zero error
            if num2 == 0:
                print("Can't divide by zero!")
                continue
            result = num1 / num2

        # Display the result
        print("Result:", result)

# Call the calculator function to run the program
calculator()