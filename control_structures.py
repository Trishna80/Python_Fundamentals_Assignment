def classify_number():
    while True:
        user_input = input("Enter a number to classify (or type 'exit' to quit): ")
        
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break  # Exit the loop if the user types 'exit'
        
        try:
            number = float(user_input)  # Convert input to a float
            if number > 0:
                print("The number is positive.")
            elif number < 0:
                print("The number is negative.")
            else:
                print("The number is zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")
classify_number()