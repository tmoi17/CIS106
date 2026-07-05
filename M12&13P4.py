#  print student names and grades and class average grade in two columns with a header for each column by first creating a dictionary

# prompt user to enter the number of students they want to put in the dictionary
n = int(input("How many students? "))

# defines an empty dictionary for student data
studentdata = {}

# initially set the total_score to be 0 
total_score = 0 

# for loop to utilize the number of students inputted and ask the user to enter the student name and their grade
for i in range(n):
    # input the key (student) and the respective value (grade)
    key = input("Name of the student: ")
    value = int(input("Grade this student has:  "))
    
    # add the student's name and grade to the dictionary
    studentdata[key] = value
    
    # update the total score
    total_score = total_score + value 

# print the column headers. :<20 just means that it reserves 20 characters for the student name. Specifically, if the name is "Tyler Moi" which is 9 characters, Python automatically adds 11 spaces after it before printing the grade
print(f"{'Student':<20}{'Grade':>20}")

# create a separator between the headers (student and grade)
print("-"*40)

# display each student's name and grade using a for loop
for key, value in studentdata.items():
    print(f"{key:<20}{value:>20}")
    
# calculate the class average
class_average = total_score/n

# add a blank line
print()

# display the class average 
print(f"Class average is: {class_average:.1f}")