
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#



# Function to add a student


def add_student(students):

    name = input("Student name: ")

    student_id = int(input("Student ID: "))

    number_of_scores = int(input("How many scores? "))

    scores = []

    for i in range(number_of_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)


    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)

    print(f'Student "{name}" added successfully.')




# Function to calculate average score


def calculate_average(scores):

    total = 0

    for score in scores:
        total += score

    average = total / len(scores)

    return round(average, 2)




# Function to display all students


def display_students(students):

    if len(students) == 0:
        print("No student records available.")

    else:
        print("\n--------------------------------------------------")
        print("Name\t\tID\t\tScores\t\tAverage")
        print("--------------------------------------------------")

        for student in students:

            average = calculate_average(student["scores"])

            score_list = ", ".join(map(str, student["scores"]))

            print(
                student["name"],
                "\t",
                student["id"],
                "\t",
                score_list,
                "\t",
                average
            )

        print("--------------------------------------------------")




# Function to find and calculate average for a specific student


def find_student_average(students):

    student_id = int(input("Enter student ID: "))

    found = False

    for student in students:

        if student["id"] == student_id:

            average = calculate_average(student["scores"])

            print(
                student["name"],
                "'s average score:",
                average
            )

            found = True
            break


    if found == False:
        print("Error: Student ID not found.")




# Function to display menu


def display_menu():

    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")




# MAIN PROGRAM


def main():

    students = []

    while True:

        display_menu()

        choice = input("Enter your choice (1-4): ")


        if choice == "1":

            add_student(students)


        elif choice == "2":

            display_students(students)


        elif choice == "3":

            find_student_average(students)


        elif choice == "4":

            print("Goodbye!")
            break


        else:

            print("Error: Invalid menu choice. Please select 1-4.")



# Start program
main()