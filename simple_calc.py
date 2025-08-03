#!/usr/bin/env python3
"""
Simple Calculator Module
Basic arithmetic operations that can be imported and used in other scripts
"""

class Calculator:
    """A simple calculator class with basic arithmetic operations"""
    
    @staticmethod
    def add(x, y):
        """Add two numbers"""
        return x + y
    
    @staticmethod
    def subtract(x, y):
        """Subtract second number from first"""
        return x - y
    
    @staticmethod
    def multiply(x, y):
        """Multiply two numbers"""
        return x * y
    
    @staticmethod
    def divide(x, y):
        """Divide first number by second"""
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y
    
    @staticmethod
    def calculate(expression):
        """
        Calculate a simple expression string
        Example: calculate("5 + 3") returns 8
        Supports +, -, *, / operators
        """
        try:
            # Simple evaluation for basic expressions
            # Note: This is safe for simple arithmetic but shouldn't be used with untrusted input
            allowed_chars = set('0123456789+-*/.() ')
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")
            
            result = eval(expression)
            return result
        except ZeroDivisionError:
            raise ValueError("Division by zero is not allowed")
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")

# Convenience functions for direct use
def add(x, y):
    return Calculator.add(x, y)

def subtract(x, y):
    return Calculator.subtract(x, y)

def multiply(x, y):
    return Calculator.multiply(x, y)

def divide(x, y):
    return Calculator.divide(x, y)

def calculate(expression):
    return Calculator.calculate(expression)

# Demo function
def demo():
    """Demonstrate calculator functionality"""
    print("Calculator Demo:")
    print("-" * 20)
    
    # Test basic operations
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    
    # Test expression calculation
    print(f"(5 + 3) * 2 = {calculate('(5 + 3) * 2')}")
    print(f"10 / 2 + 3 = {calculate('10 / 2 + 3')}")
    
    # Test error handling
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    demo()
