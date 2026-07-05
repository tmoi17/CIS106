# print list of students and their grade averages. Also print the class average for each of the three grades. Layout the output for ease of readability by the user

# prompt user to enter the number of students they want to put in the dictionary
n = int(input("How many students? "))

# defines an empty dictionary for student data
studentdata = {}

# initially assign global variables to be 0 for the first grade, second grade, and third grade each student has
value1 = 0
value2 = 0
value3 = 0 

# for loop to utilize the number of students inputted and ask the user to enter the student name and their grade
for i in range(n):
    # input the key (student) 
    key = input("Name of the student: ")
    
    # define list for the three grades (That one student has)
    value = [] 
    
    # for loop to ask for the 3 grades EACH student has and adds those grades to the list. This makes SEPARATE lists of 3 grades for each respective student. 
    for y in range(3):
        # prompt the student for the grade 
        grade = int(input("Grade this student has:  "))
        # adds the grade to the value list
        value.append(grade)
        # if/elif utilized to add up all the first grades each student has, add up second grades, and add up third grades respectively in order to help us find out the class average for EACH particular grade. 
        if y == 0:
            value1 = value1 + value[0]
        elif y == 1:
            value2 = value2 + value[1]
        elif y == 2:
            value3 = value3 + value[2]
    
    # add the student's name and their respective three grades to the dictionary
    studentdata[key] = value 

# blank line
print()

# print the column headers. :<20 just means that it reserves 20 characters for the student name. Specifically, if the name is "Tyler Moi" which is 9 characters, Python automatically adds 11 spaces after it before printing the grade average
print(f"{'Student':<20}{'Grade Average':>20}")

# create a separator between the headers (student and grade average)
print("-"*40)

# display each student's name and their respective grade average using a for loop
for key, value in studentdata.items():
    print(f"{key:<20}{(value[0]+value[1]+value[2])/3:>20.1f}")
    
# blank line
print()

# function to create a list of three grade averages for the class and then display the result 
def class_gradeaverage():
    grade_averages = []
    grade_averages.append(value1/n)
    grade_averages.append(value2/n)
    grade_averages.append(value3/n)
    print(f"The class average for the first grade is {grade_averages[0]:.1f}")
    print(f"The class average for the second grade is {grade_averages[1]:.1f}")
    print(f"The class average for the third grade is {grade_averages[2]:.1f}")

# call function class_gradeaverage
class_gradeaverage()
        
