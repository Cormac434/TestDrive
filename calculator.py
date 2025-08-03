#!/usr/bin/env python3
"""
Simple Calculator with Basic Arithmetic Operations
Supports addition (+), subtraction (-), multiplication (*), division (/),
power (**), and root operations
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

def power(x, y):
    """Power function - raises x to the power of y"""
    try:
        return x ** y
    except OverflowError:
        return "Error: Result too large to calculate"
    except Exception as e:
        return f"Error: {str(e)}"

def root(x, y):
    """Root function - calculates the y-th root of x"""
    if y == 0:
        return "Error: Cannot calculate 0th root"
    
    try:
        # For even roots of negative numbers, return error
        if x < 0 and y % 2 == 0:
            return "Error: Cannot calculate even root of negative number"
        
        # Handle negative numbers for odd roots
        if x < 0 and y % 2 == 1:
            return -(abs(x) ** (1/y))
        
        return x ** (1/y)
    except OverflowError:
        return "Error: Result too large to calculate"
    except Exception as e:
        return f"Error: {str(e)}"

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*50)
    print("              SIMPLE CALCULATOR")
    print("="*50)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (**)")
    print("6. Root (nth root)")
    print("7. Exit")
    print("="*50)

def main():
    """Main calculator function"""
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        
        choice = input("Enter choice (1-7): ").strip()
        
        if choice == '7':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            # Get numbers from user with appropriate prompts
            if choice == '5':  # Power operation
                num1 = get_number("Enter base number: ")
                num2 = get_number("Enter exponent: ")
            elif choice == '6':  # Root operation
                num1 = get_number("Enter number: ")
                num2 = get_number("Enter root (e.g., 2 for square root, 3 for cube root): ")
            else:
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
            elif choice == '5':
                result = power(num1, num2)
                operation = "**"
            elif choice == '6':
                result = root(num1, num2)
                operation = f"root({num2}) of"
            
            # Display result with appropriate formatting
            if choice == '6':  # Root operation has different display format
                print(f"\nResult: {operation} {num1} = {result}")
            else:
                print(f"\nResult: {num1} {operation} {num2} = {result}")
            
            # Ask if user wants to continue
            continue_calc = input("\nDo you want to perform another calculation? (y/n): ").lower().strip()
            if continue_calc != 'y' and continue_calc != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
        else:
            print("Invalid choice! Please select a valid option (1-7).")

if __name__ == "__main__":
    main()
