# Changelog

All notable changes to this Python Calculator project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2025-08-03

### Added
- **Power operation (**)** to `calculator.py`
  - Raises a number to any power (including negative and fractional exponents)
  - Handles overflow errors for very large results
  - User-friendly prompts for base and exponent input
- **Root operation (nth root)** to `calculator.py`
  - Calculates any root of a number (square root, cube root, etc.)
  - Handles negative numbers correctly for odd roots
  - Prevents calculation of even roots of negative numbers
  - Prevents calculation of 0th roots
- Enhanced error handling for mathematical edge cases
- Updated menu interface to accommodate new operations (1-7 options)
- Improved user input prompts with context-specific messages

### Changed
- Updated menu display width from 40 to 50 characters for better formatting
- Modified exit option from choice 5 to choice 7
- Enhanced result display formatting for root operations
- Updated docstring to reflect new supported operations

### Fixed
- Improved error handling for overflow scenarios
- Better handling of mathematical edge cases

## [1.0.0] - 2025-08-03

### Added
- **Interactive Calculator (`calculator.py`)**
  - Menu-driven interface for basic arithmetic operations
  - Addition (+), subtraction (-), multiplication (*), and division (/)
  - Input validation and error handling
  - Division by zero protection
  - Continuous operation until user chooses to exit
  - User-friendly prompts and result display

- **Calculator Module (`simple_calc.py`)**
  - Modular calculator that can be imported into other Python scripts
  - Calculator class with static methods for arithmetic operations
  - Convenience functions for direct use
  - Expression evaluation capability using `calculate()` method
  - Demo function to showcase functionality
  - Proper error handling with exceptions

- **Documentation**
  - Comprehensive README.md with detailed explanations
  - Code documentation with docstrings
  - Usage examples for both standalone and module usage
  - Error handling documentation

- **Project Setup**
  - Git repository initialization
  - GitHub integration with SSH authentication
  - Proper project structure and organization

### Technical Details
- Python 3 compatibility
- Clean, readable code structure
- Comprehensive error handling
- User input validation
- Cross-platform compatibility

---

## Legend
- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** for vulnerability fixes
