def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        choice = input("Enter choice (1/2/3/4) or 'exit' / 'Exit' to quit: ")
        
        if choice.lower() == "exit":
            print("Exiting the calculator.")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    print(f"The result is: {result}")

                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"The result is: {result}")

                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"The result is: {result}")

                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"The result is: {result}")

            except ValueError:
                print("Invalid input. Please enter numeric values.")

        else:
            print("Invalid choice. Please select a valid operation.")

calculator()
