# Task 1: Check if a Number is Even or Odd

# Taking an integer input from the user
try:
    number = int(input("Enter an integer: "))
    
    # Checking whether the number is even or odd
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
        
except ValueError:
    print("Invalid input. Please enter a valid integer.") 