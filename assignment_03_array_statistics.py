# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#

# Function to calculate the sum of numbers
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Function to calculate the average of numbers
def calculate_average(numbers):
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return average


# Function to find the maximum number
def calculate_maximum(numbers):
    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


# Function to find the minimum number
def calculate_minimum(numbers):
    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num

    return minimum


# Main program
n = int(input("How many numbers? "))

# Check if the N is positive
if n <= 0:
    print("Error: Number of values must be positive.")
else:
    numbers = []

    # Read numbers from user
    for i in range(n):
        value = float(input(f"Enter number {i + 1}: "))
        numbers.append(value)

    # Display results
    print("\nResults:")
    print("Sum:    ", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Maximum:", calculate_maximum(numbers))
    print("Minimum:", calculate_minimum(numbers))