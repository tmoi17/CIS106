# create a Student class and calculate tuition owed given the district code and enrolled credits

# define the Student class
class Student:

    # defines what the object is going to receive. self is way of saying any instance created, receive first, last, districtcode, and credit
    def __init__(self, first, last, districtcode, credit):

        # store the student's first name
        self.first = first  

        # store the student's last name
        self.last = last

        # store the student's district code
        self.districtcode = districtcode

        # store the student's enrolled credits
        self.credit = credit

    # method to calculate the tuition owed
    def tuition(self):
        # if/else statement to determine the tuition based on the given districtcode and enrolled credits
        if self.districtcode == "I":
            t = self.credit * 250.00
        else:
            t = self.credit * 500.00

        # return the tuition owed back to where the method was called 
        return t

# instantiates a Student object
stu1 = Student('Tyler', 'Moi', 'I', 6)

# display the tuition owed by Tyler Moi by calling the method tuition for stu1
print(f"Student 1 owes ${stu1.tuition():.2f} for tuition")