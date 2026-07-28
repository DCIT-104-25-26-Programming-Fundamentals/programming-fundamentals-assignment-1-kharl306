
# TASK: Console-Based Simple Calculator


# Arithmetic Functions

# Addition function
def add(num1, num2):
    return num1 + num2


# Subtraction function
def subtract(num1, num2):
    return num1 - num2


# Multiplication function
def multiply(num1, num2):
    return num1 * num2


# Division function
def divide(num1, num2):

    if num2 == 0:
        return None

    return round(num1 / num2, 2)


# Modulus function
def modulus(num1, num2):

    if num2 == 0:
        return None

    return num1 % num2


# Exponentiation function
def exponent(num1, num2):
    return num1 ** num2



# Function to display menu

def display_menu():

    print("\n============================")
    print("       SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")



# MAIN PROGRAM

def main():

    while True:

        display_menu()

        choice = input("Select an operation (1-7): ")


        if choice == "7":
            print("Goodbye!")
            break


        elif choice in ["1", "2", "3", "4", "5", "6"]:

            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))


            if choice == "1":

                result = add(num1, num2)
                print("Result:", num1, "+", num2, "=", result)


            elif choice == "2":

                result = subtract(num1, num2)
                print("Result:", num1, "-", num2, "=", result)


            elif choice == "3":

                result = multiply(num1, num2)
                print("Result:", num1, "*", num2, "=", result)


            elif choice == "4":

                result = divide(num1, num2)

                if result is None:
                    print("Error: Cannot divide by zero.")

                else:
                    print("Result:", num1, "/", num2, "=", result)


            elif choice == "5":

                result = modulus(num1, num2)

                if result is None:
                    print("Error: Cannot calculate modulus by zero.")

                else:
                    print("Result:", num1, "%", num2, "=", result)


            elif choice == "6":

                result = exponent(num1, num2)
                print("Result:", num1, "**", num2, "=", result)


        else:

            print("Error: Invalid menu choice. Please select 1-7.")



# Run calculator
main()