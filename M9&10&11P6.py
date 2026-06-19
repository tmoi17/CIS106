# display student's last name, total points, and average exam score

# function to compute and return the average and total points of the exams
def compute_average_total(first_exam, second_exam, third_exam):
    average = (first_exam + second_exam + third_exam)/3
    total_points = first_exam + second_exam + third_exam 
    return average, total_points

# prompt user on whether or not they want to do this program
response = input("Do you want to do this program? Enter Yes or No: ")

# enter while loop if response is Yes, and iterate until response is not Yes
while response == "Yes":
    # enter the student's last name and 3 exam scores 
    student_last_name = input("Enter student last name: ")
    first_exam = float(input("Enter first exam score: "))
    second_exam = float(input("Enter second exam score: "))
    third_exam = float(input("Enter third exam score: "))

    # function compute_average_total is called and python now substituites first_exam, second_exam, and third_exam entered and goes back into the function and calculates both the average and total points
    average, total_points = compute_average_total(first_exam, second_exam, third_exam)
    
    # display student's last name, total points, and average exam score
    print(f"Student's last name is {student_last_name}")
    print(f"Total points is {total_points:.1f}")
    print(f"Average exam score is {average:.1f}")
    
    # ask user if they want to do this program again for the next iteration
    response = input("Do you want to do this program? Enter Yes or No: ")




