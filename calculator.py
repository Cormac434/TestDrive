#!/usr/bin/env python3
"""
Simple Calculator with Basic Arithmetic Operations
Supports addition (+), subtraction (-), multiplication (*), and division (/)
"""

def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error: Division by zero is not allowed"
    return x / y

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("         SIMPLE CALCULATOR")
    print("="*40)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("="*40)

def main():
    """Main calculator function"""
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            # Get numbers from user
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            # Perform calculation based on choice
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            # Display result
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            
            # Ask if user wants to continue
            continue_calc = input("\nDo you want to perform another calculation? (y/n): ").lower().strip()
            if continue_calc != 'y' and continue_calc != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
        else:
            print("Invalid choice! Please select a valid option (1-5).")

if __name__ == "__main__":
    main()
