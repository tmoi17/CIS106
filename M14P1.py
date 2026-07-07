# create simple class from video and add a method that accepts a bonus rate for the employee. Then compute employee bonus, return this value, then display bonus

# define the object through employee class
class Employee:

    # defining the __init__ method (constructor method). defines what the object is going to receive. self is way of saying any instance created, receive first, last, pay.
    def __init__(self, first, last, pay):
        # self.first, last, pay, and email all belong to the object
        
        # store the employee's first name
        self.first = first

        # store the employee's last name
        self.last = last

        # store the employee's salary
        self.pay = pay

        # create the employee's email address
        self.email = first + '.' + last + '@company.com'

    # method to calculate the employee's bonus
    def bonus(self, rate):
        # calculate the bonus
        Bonus = float(rate) * float(self.pay)

        # return the bonus 
        return Bonus

# class name Employee and then pass it data which instantiates the object and assigns it to variable emp11
emp11 = Employee('Corey', 'Schafer', 60000.00)

# display the employee's email
print(emp11.email)

# display the employee's first name
print(emp11.first)

# display the employee's last name
print(emp11.last)

# display the employee's salary
print(emp11.pay)

# prompt the user to enter a bonus rate
rate = float(input("Enter the bonus rate: "))

# call the bonus method and display the employee's bonus
print(emp11.bonus(rate))