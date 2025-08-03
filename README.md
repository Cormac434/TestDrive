# Simple Python Calculators

This repository contains two simple Python calculator implementations:

1. **`calculator.py`:** An interactive calculator with a user-friendly menu interface.
2. **`simple_calc.py`:** A modular calculator that can be imported and used in other Python scripts.

## 1. Interactive Calculator (`calculator.py`)

### Description
A command-line calculator that guides the user through various arithmetic operations using a menu-driven interface.

### Features
- **Addition (+)**
- **Subtraction (-)**
- **Multiplication (*)**
- **Division (/)**: Includes protection against division by zero.
- **Power (**)**: Raises a number to any power (including negative and fractional exponents)
- **Root (nth root)**: Calculates any root of a number (square root, cube root, etc.)
- **Continuous operation** until the user decides to exit.

### How It Works
- **Menu Driven:** Presents users with a menu of options to perform arithmetic operations or to exit the program.
- **User Input Handling:** Prompts the user to input numbers and select an operation, validating the inputs. For power operations, prompts for base and exponent. For root operations, prompts for the number and the root type.
- **Operations Execution:** Performs the selected arithmetic operation and displays the result.
- **Error Handling:** Handles special cases like division by zero, even roots of negative numbers, and overflow errors.

### Calculator Flow Diagram

```mermaid
flowchart TD
    A([Start Calculator]) --> B[Display Welcome Message]
    B --> C[Display Menu]
    C --> D{User Choice?}
    
    D -->|1| E[Addition]
    D -->|2| F[Subtraction]
    D -->|3| G[Multiplication]
    D -->|4| H[Division]
    D -->|5| I[Power]
    D -->|6| J[Root]
    D -->|7| K[Exit Program]
    D -->|Invalid| L[Show Error Message]
    
    E --> M[Get First Number]
    F --> M
    G --> M
    H --> M
    
    I --> N[Get Base Number]
    N --> O[Get Exponent]
    O --> P[Calculate Power]
    P --> Q{Overflow Error?}
    Q -->|Yes| R[Display Error]
    Q -->|No| S[Display Result]
    
    J --> T[Get Number]
    T --> U[Get Root Type]
    U --> V{Valid Root?}
    V -->|0th Root| W[Display Error: Cannot calculate 0th root]
    V -->|Even Root of Negative| X[Display Error: Even root of negative number]
    V -->|Valid| Y[Calculate Root]
    Y --> S
    
    M --> Z[Get Second Number]
    Z --> AA{Valid Numbers?}
    AA -->|No| AB[Display Input Error]
    AA -->|Yes| AC{Operation Type?}
    
    AC -->|Addition| AD[num1 + num2]
    AC -->|Subtraction| AE[num1 - num2]
    AC -->|Multiplication| AF[num1 * num2]
    AC -->|Division| AG{num2 == 0?}
    
    AG -->|Yes| AH[Display Division by Zero Error]
    AG -->|No| AI[num1 / num2]
    
    AD --> S
    AE --> S
    AF --> S
    AI --> S
    
    S --> AJ[Ask Continue?]
    R --> AJ
    W --> AJ
    X --> AJ
    AH --> AJ
    AB --> AJ
    L --> AJ
    
    AJ --> AK{Continue?}
    AK -->|Yes| C
    AK -->|No| AL([Thank You & Exit])
    
    K --> AL
    
    style A fill:#e1f5fe
    style AL fill:#ffebee
    style R fill:#ffcdd2
    style W fill:#ffcdd2
    style X fill:#ffcdd2
    style AH fill:#ffcdd2
    style AB fill:#ffcdd2
    style L fill:#ffcdd2
    style S fill:#c8e6c9
```

### Usage
Run the script using Python:
```bash
python3 calculator.py
```

## 2. Calculator Module (`simple_calc.py`)

### Description
A flexible module that can be easily imported into other Python scripts, providing basic arithmetic operations.

### Features
- **Arithmetic Methods:**
  - `add(x, y)`: Returns the sum of `x` and `y`.
  - `subtract(x, y)`: Returns the difference where `y` is subtracted from `x`.
  - `multiply(x, y)`: Returns the product of `x` and `y`.
  - `divide(x, y)`: Returns the division of `x` by `y`, raising an exception if `y` is zero.
- **Expression Evaluation:**
  - `calculate(expression)`: Evaluates a simple arithmetic expression passed as a string.

### How It Works
- **Class-Based Design:** The `Calculator` class encapsulates arithmetic operations as static methods.
- **Standalone Demo:** When executed, the module demonstrates its functionality via hardcoded examples.
- **Module Importing:** Allows other scripts or applications to import and utilize its arithmetic functions.

### Usage as a Standalone Script
Run the script to see demonstrations of the calculator's capabilities:
```bash
python3 simple_calc.py
```

### Usage as a Module
Import the module's functions or the `Calculator` class:
```python
from simple_calc import Calculator, add, subtract, multiply, divide

result = add(5, 3)
expression_result = Calculator.calculate("(10 + 5) * 2")
```

## Error Handling
- **Invalid Inputs:** Protects against invalid inputs and division by zero, providing relevant error messages.
- **Power Operations:** Handles overflow errors for very large results.
- **Root Operations:** Prevents calculation of even roots of negative numbers and 0th roots.
- **Mathematical Edge Cases:** Handles negative exponents, fractional powers, and complex mathematical scenarios.

---

These calculators demonstrate simple arithmetic operations while handling errors gracefully. Feel free to extend their functionality or integrate them into larger projects!
