# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================

# To determine the student's grade
def get_grade(score):
    # Validate the score range
    if score < 0 or score > 100:
        return None

    # Determine grade using if / elif / else
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


# Main block
if __name__ == "__main__":
    score = int(input("Enter student score (0-100): "))

    grade = get_grade(score)

    if grade is None:
        print("Error: Score must be between 0 and 100.")
    else:
        print(f"Grade: {grade}")