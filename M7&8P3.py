# displaying employee last names, salaries, and bonuses 

# create a text file including 5 employee's last names with their respective salary
with open('employee_info.txt', 'w') as file:
    file.write('Moi\n')
    file.write('95000.00\n')
    file.write('Krieg\n')
    file.write('50000.00\n')
    file.write('Colleran\n')
    file.write('170000.00\n')
    file.write('Mishra\n')
    file.write('23000.00\n')
    file.write('Pederson\n')
    file.write('371000.00\n')

# open file for reading employee data
f = open('employee_info.txt', 'r')

# intitially set the sum of bonuses value to 0 
sum_of_bonuses = 0

# get first data line
last_name = str(f.readline().rstrip('\n'))

# process each employee in the file until the end of the file is reached
while last_name != "":
    # read the salary for the current employee 
    salary = float(f.readline())
    
    # determine the bonus based on the salary 
    if salary >= 100000.00:
        bonus_rate = 0.20
    elif salary == 50000.00:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10 
    
    # calculate the bonus 
    bonus = bonus_rate * salary 
    
    # update the sum of bonuses value 
    sum_of_bonuses = sum_of_bonuses + bonus
    
    # display employee's last name, salary, and bonus
    print(f"Employee's last name: {last_name}")
    print(f"Salary is ${salary:.2f}")
    print(f"Bonus is ${bonus:.2f}")
    
    # read the next employee last name for the next loop iteration
    last_name = str(f.readline().rstrip('\n'))
    
# display the sum of all bonuses paid out
print(f"Sum of all bonuses paid out is: ${sum_of_bonuses:.2f}")
    

