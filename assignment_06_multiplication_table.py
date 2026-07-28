# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#



# PART A — Single Table


def generate_single_table(number):
    print("Multiplication Table for", number, ":")

    for i in range(1, 13):
        print(number, " x ", i, " = ", number * i)



# PART B — Tables from 1 to N


def generate_tables_up_to_n(n):

    for number in range(1, n + 1):

        print("\nMultiplication Table for", number, ":")

        for i in range(1, 13):
            print(number, " x ", i, " = ", number * i)

        print("---------------------------")



# MAIN PROGRAM


# Part A
number = int(input("Enter a number for multiplication table: "))

if number <= 0:
    print("Error: Number must be a positive integer.")

else:
    generate_single_table(number)


    # Part B
    n = int(input("\nEnter N to generate tables from 1 to N: "))

    if n <= 0:
        print("Error: N must be a positive integer.")

    else:
        generate_tables_up_to_n(n)