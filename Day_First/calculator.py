def add(input1, input2):
    result = input1 + input2
    return result

def sub(input1, input2):
    result = input1 - input2
    return result

def multiply(input1, input2):
    if input2 == 0:
        return "Error: Cannot multiply by zero."
    result = input1 * input2
    return result

def division(input1, input2):
    if input2 == 0:
        return "Error: Cannot divide by zero."
    result = input1 / input2
    return result

# Main program with continuous loop
while True:
    try:
        input1 = float(input("Enter Your First Number: "))
        operator = input("Select your operator (+, -, *, /) or 'exit' to quit: ").strip()
        
        # Exit condition
        if operator.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        input2 = float(input("Enter Your Second Number: "))

        # Checking for the valid operator first
        if operator == '+':
            print("Result:", add(input1, input2))

        elif operator == '-':
            print("Result:", sub(input1, input2))

        elif operator == '*':
            result = multiply(input1, input2)
            if "Error" in result:  # Check if error occurred
                print(result)
            else:
                print("Result:", result)

        elif operator == '/':
            result = division(input1, input2)
            if "Error" in result:  # Check if error occurred
                print(result)
            else:
                print("Result:", result)

        else:
            print("Error: Enter a valid operation (+, -, *, /)")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
