def get_grade(subject):
    """
    Prompts the user to enter a grade for a specified subject.

    Parameters:
    subject (str): The name of the subject for which to enter the grade.

    Returns:
    float: The grade entered by the user.

    Raises:
    ValueError: If the input is not a valid float.
    """
    while True:
        try:
            return float(input(f"Pls enter your {subject} grade: "))
        except ValueError as e:
            print("Pls enter a valid grade")
            continue


def get_name():
    """
    Prompts the user to enter a student's name.

    Returns:
    str: The name entered by the user.
    """
    return input("Pls enter the name: ")


def get_student_info(index):
    """
    Collects the information for a student including their name and grades.

    Parameters:
    index (int): The student's index number for identification in the input process.

    Returns:
    dict: A dictionary containing the student's name, English grade, and Math grade.
    """
    print()
    print(f"Enter details for student {index}")
    name = get_name()
    englis_grade = get_grade("English")
    math_grade = get_grade("Math")
    return {"Name": name, "English": englis_grade, "Math": math_grade}


def enter_number_students():
    """
    Prompts the user to enter the number of students for whom to gather information.

    Returns:
    int: The number of students.

    Raises:
    ValueError: If the input is not a valid integer.
    """
    while True:
        try:
            return int(input("Enter the number of students: "))
        except ValueError as e:
            print("Pls enter a valid integer")
            continue


def get_students_info():
    """
    Collects information for all students specified by the user.

    Returns:
    list: A list of dictionaries, each containing the information for one student.
    """
    students = []
    number_students = enter_number_students()
    for i in range(number_students):
        student = get_student_info(i + 1)
        students.append(student)
    return students


def print_student_info(students):
    """
    Prints the information of all students, including their names, best grades,
    and average grades.

    Parameters:
    students (list): A list of dictionaries, each containing a student's information.
    """
    print()
    print("Studen Information:")
    for student in students:
        name, english, math = student.values()
        best_grade = max(english, math)
        avg = (math + english) / 2
        print(f"Student: {name}, Best Grade {best_grade}, Average Grade {avg}")


def calculate_average_grades(students):
    """
    Calculates the average grades per subject and the overall average grade across all subjects.

    Parameters:
    students (list): A list of dictionaries, each containing a student's information.

    Returns:
    tuple: A tuple containing a dictionary of average grades per subject and the overall average grade.
    """
    english_sum = 0
    math_sum = 0
    student_count = len(students)

    # Iterate over the list of students and sum the grades for each subject
    for student in students:
        english_sum += student["English"]
        math_sum += student["Math"]

    # Calculate average grades per subject
    average_grades_per_subject = {
        "English": english_sum / student_count,
        "Math": math_sum / student_count,
    }

    # Calculate the overall average grade across all subjects
    overall_average_grade = (english_sum + math_sum) / (student_count * 2)

    return average_grades_per_subject, overall_average_grade


def print_average_grades(average_grades_per_subject, overall_average_grade):
    """
    This function receives the average grades for each subject and the overall
    average grade across all subjects. It then prints these averages in a formatted
    manner.

    Parameters:
    average_grades_per_subject (dict):  A dictionary where the keys are subject
                                        names (e.g., "English", "Math") and the
                                        values are the corresponding average grades.

    overall_average_grade (float):  The overall average grade calculated by averaging
                                    the grades across all subjects for all students.
    """
    for subject, average_grade in average_grades_per_subject.items():
        print(f"{subject}: {average_grade:.2f}")

    print(f"\nOverall average grade across all subjects: {overall_average_grade:.2f}")


def main():
    """
    Main function to execute the student information collection and display process.
    """
    students = get_students_info()
    print_student_info(students)

    average_grades_per_subject, overall_average_grade = calculate_average_grades(
        students
    )
    print_average_grades(average_grades_per_subject, overall_average_grade)
    print("\nAverage grades per subject:")


main() if __name__ == "__main__" else None
