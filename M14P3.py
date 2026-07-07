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

    # method that contains a dictionary and utilizes it to calculate the tuition owed 
    def tuition(self):
        # creates a dictionary where the key is the district code and the price per credit is the value
        dictionary = {'I': 250.00, 'O': 500.00, 'X': 800.00, 'G': 250.00}
        
        # calculate the tuition owed 
        t = dictionary[self.districtcode] * self.credit
        
        # return the tuition owed back to where the method was called 
        return t
    
# instantiate student objects for each district code
stu1 = Student('Tyler', 'Moi', 'I', 6)
stu2 = Student('John', 'Smith', 'O', 16)
stu3 = Student('Edwin', 'Rogers', 'X', 14)
stu4 = Student('Will', 'Krieg', 'G', 9)

# display the tuition owed by calling the method tuition for stu1, stu2, stu3, and stu4
print(f"Student 1 owes ${stu1.tuition():.2f} for tuition")
print(f"Student 2 owes ${stu2.tuition():.2f} for tuition")
print(f"Student 3 owes ${stu3.tuition():.2f} for tuition")
print(f"Student 4 owes ${stu4.tuition():.2f} for tuition")


