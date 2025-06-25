# PROJECT NAME: SIMPLE ATM SIMULATION

# 1. Initialization
# We define the initial balance. In a real application, this would come from a database.
balance = 1000

# 2. Main Loop
# This loop will run until the user presses 'q' to quit.
while True:
    # The '\n' character ensures each print starts on a new line, making the menu more readable.
    print("\n--- Financial Control Simulator ---")
    print("1: Check Balance")
    print("2: Deposit Money")
    print("3: Withdraw Money")
    print("q: Quit")

    # Get the user's choice.
    choice = input("Please select an operation (1, 2, 3, or q): ")

    # 3. Process User's Choice
    # We use an if-elif-else block to analyze the user's choice.
    
    if choice == '1':
        print(f"\nYour current balance is: ${balance}") # More professional currency symbol

    elif choice == '2':
        print("\n--- Deposit Money ---")
        deposit_str = input("Enter amount to deposit: ")
        
        try:
            # Try to convert the user input to an integer.
            amount = int(deposit_str)
            
            # Check if the amount is a positive number.
            if amount > 0:
                # Update the balance.
                balance += amount  # Shorter and more standard way to write: balance = balance + amount
                print(f"Deposit successful. New balance is: ${balance}")
            else:
                print("\nInvalid amount. Please enter a positive number.")
        except ValueError:
            # This block runs if the conversion to int fails (e.g., user enters text).
            print("\nError! Please enter only numbers.")

    elif choice == '3':
        print("\n--- Withdraw Money ---")
        withdraw_str = input("Enter amount to withdraw: ")
        
        try:
            amount = int(withdraw_str)
            
            # First, check if the requested amount is positive.
            if amount > 0:
                # Then, check for sufficient balance (nested if).
                if amount <= balance: # Using <= is safer than >
                    balance -= amount # Shorter and more standard way: balance = balance - amount
                    print(f"Withdrawal successful. New balance is: ${balance}")
                else:
                    print(f"\nInsufficient balance! You only have ${balance}.")
            else:
                print("\nInvalid amount. Please enter a positive number.")
        except ValueError:
            print("\nError! Please enter only numbers.")

    elif choice == 'q':
        print("\nExiting the simulator...")
        break  # Exit the loop

    else:
        print("\nInvalid operation. Please try again.")

# 4. Final Message
# This line will run after the loop is broken.
print("\nSimulator session finished. Thank you.")    
