# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#


# PART A — Print the First N Terms

def generate_fibonacci(n):
    fibonacci = []

    first = 0
    second = 1

    for i in range(n):
        fibonacci.append(first)

        next_number = first + second
        first = second
        second = next_number

    return fibonacci


def print_fibonacci_terms(n):
    sequence = generate_fibonacci(n)

    print("Fibonacci sequence:", end=" ")

    for number in sequence:
        print(number, end=" ")

    print()


# PART B — Check if a Number Belongs to the Sequence

def is_fibonacci_number(number):
    first = 0
    second = 1

    # Generate Fibonacci numbers using a loop
    while first <= number:

        if first == number:
            return True

        next_number = first + second
        first = second
        second = next_number

    return False


# MAIN PROGRAM

# Part A
n = int(input("How many terms? "))

if n <= 0:
    print("Error: Number of terms must be a positive integer.")

else:
    print_fibonacci_terms(n)


    # Part B
    number = int(input("\nEnter a number to check: "))

    if is_fibonacci_number(number):
        print(number, "is a Fibonacci number.")
    else:
        print(number, "is NOT a Fibonacci number.")