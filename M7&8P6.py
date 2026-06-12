# display count of students who entered data to find their average exam scores

# prompt user on whether or not they want to do this program
response = input("Do you want to do this program? Enter Yes or No: ")

# initially set the count of students to be 0 
count_of_students = 0

# ask for last name, and 2 exam scores if response is yes and increase count of students value through each iteration
while response == "Yes":
    last_name = input("What is your last name? ")
    first_exam = float(input("Enter your first exam score: "))
    second_exam = float(input("Enter your second exam score: "))
    average_exam_score = (first_exam + second_exam)/2
    print(f"{last_name}, your average exam score is {average_exam_score}")
    count_of_students += 1
    response = input("Do you want to do this program? Enter Yes or No: ")

# display count of students 
print(f"{count_of_students}")

