# employee last name and bonus 

# prompt user to enter employee last name 
employee_last_name = input("Enter employee last name: ")

# prompt user to enter salary 
salary = float(input("Enter employee salary: "))

# prompt user to enter job level 
job_level = int(input("Enter employee job level: "))

# determine bonus rate based on job level 
if job_level >= 5:
    if job_level <= 9:
        bonus_rate = 0.20
    else: 
        bonus_rate = 0.25
else: 
    bonus_rate = 0.10

# calculate bonus 
bonus = salary * bonus_rate 

# display result 
print(f"{employee_last_name}, your bonus is ${bonus:.2f}")

