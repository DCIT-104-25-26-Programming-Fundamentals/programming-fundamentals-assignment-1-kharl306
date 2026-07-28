# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================

# Check whether a number is prime
def is_prime(number):
    # Numbers less than 2 are not prime numbers
    if number < 2:
        return False

    # Check for divisors from 2 up to the number - 1
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# Main block
if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT a prime number.")
