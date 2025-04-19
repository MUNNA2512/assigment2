# Python Control Structures Assignment

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

## Overview
This repository contains two Python scripts demonstrating fundamental control structures in Python as part of Assignment 2. These programs showcase the implementation of conditional statements (if-else) and loops (for loop) to solve simple programming problems.

## 📁 Repository Contents
- `task1.py`: Check if a number is even or odd
- `task2.py`: Calculate sum of integers from 1 to 50
- `README.md`: Documentation for the project

## 🔍 Task Descriptions

### Task 1: Check if a Number is Even or Odd

The `task1.py` script determines whether a user-provided integer is even or odd:

- Takes an integer input from the user
- Checks whether the number is even or odd using an if-else statement
- Displays the result accordingly
- Includes error handling for invalid input

#### Algorithm:
1. Get an integer input from the user
2. Use the modulo operator (%) to check if the number is divisible by 2
3. If number % 2 == 0, the number is even; otherwise, it's odd
4. Handle any potential ValueError if the user enters non-integer input

#### How to run:
```bash
python task1.py
```

#### Example Output:
```
Enter an integer: 7
7 is an odd number.
```

Or:
```
Enter an integer: 12
12 is an even number.
```

### Task 2: Sum of Integers from 1 to 50 Using a Loop

The `task2.py` script calculates the sum of all integers from 1 to 50:

- Uses a for loop to iterate over numbers from 1 to 50
- Calculates the sum of all integers in this range
- Displays the final sum

#### Algorithm:
1. Initialize a variable to store the sum (total_sum = 0)
2. Use a for loop to iterate through numbers 1 to 50
3. Add each number to the running sum
4. Display the final sum after the loop completes

#### How to run:
```bash
python task2.py
```

#### Example Output:
```
The sum of integers from 1 to 50 is: 1275
```

## 💻 Technology Used
- Python 3.x
- Control structures:
  - Conditional statements (if-else)
  - Loops (for loop)
- Exception handling (try-except)

## 📚 Learning Outcomes
- Understanding conditional logic with if-else statements
- Implementing loops to repeat operations
- Working with basic mathematical operations
- Handling user input and potential errors
- Using string formatting to display results

## 🚀 Getting Started
1. Clone this repository
2. Make sure Python is installed on your system
3. Run the scripts using the commands provided above

## 📄 License
This project is available for educational purposes. Feel free to use and modify the code for learning. 