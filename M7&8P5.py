# display students last name, credits taken, tuition owed, the sum of all tuition owed, and number of students

# create text file with student last names and their respective district code and number of credits taken
with open('student_info.txt', 'w') as file:
    file.write('Moi\n')
    file.write('I\n')
    file.write('13\n')
    file.write('Gordon\n')
    file.write('O\n')
    file.write('15\n')
    file.write('Pratt\n')
    file.write('O\n')
    file.write('12\n')
    file.write('Johnson\n')
    file.write('I\n')
    file.write('14\n')
    

# open file for reading student data
f = open("student_info.txt", "r")

# intitially set the sum of tuition owed and number of students equal to 0
sum_tuition_owed = 0
number_of_students = 0

# get first data line
student_last_name = str(f.readline().rstrip('\n'))

# process each student in the file until the end of the file is reached
while student_last_name != "":
    # read the district code and credits taken for each student
    district_code = str(f.readline().rstrip('\n'))
    credits_taken = int(f.readline())
    
    # determine the cost per credit based on the district code
    if district_code == "I":
        cost_per_credit = 250.00
    elif district_code == "O":
        cost_per_credit = 500.00
    
    # calculate the tuition owed 
    tuition_owed = credits_taken * cost_per_credit
    
    # update the sum of tuition owed and increase the number of students by 1 
    sum_tuition_owed = sum_tuition_owed + tuition_owed
    number_of_students += 1
    
    # display students last name, credits they have taken, and tuition they owe
    print(f"Student last name is: {student_last_name}")
    print(f"Credits taken is: {credits_taken}")
    print(f"Tuition owed is ${tuition_owed:.2f}")
    
    # read the next student for the next loop iteration
    student_last_name = str(f.readline().rstrip('\n'))

# display the sum of all tuition owed and the number of students
print(f"Sum of all tuition owed is: ${sum_tuition_owed:.2f}")
print(f"Number of students is: {number_of_students}")