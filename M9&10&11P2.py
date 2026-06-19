# giving the count of the number of players entered along with their last name and batting average

# intitially set the count of the number of players to 0
number_of_players = 0 

# prompt user on whether or not they want to do this program
response = input("Do you want to do this program? Enter Yes or No: ")

# function to compute and return the batting average 
def compute_batting_average(hits, at_bats):
    batting_average = hits / at_bats 
    
    # sends batting_average value back to where the function is called 
    return batting_average

# enter while loop if response is Yes, and iterate until response is not Yes
while response == "Yes":
    # enter the players last name, number of hits and at bats
    last_name = input("Enter players last name: ")
    hits = int(input("Enter players number of hits: "))
    at_bats = int(input("Enter players number of at bats: "))
    
    # function compute_batting_average is called and python now substituites hits and at_bats entered and goes back into the function and calculates the batting average
    batting_average = compute_batting_average(hits, at_bats)
    
    # display the players last name and batting average 
    print(f"Players last name is: {last_name}")
    print(f"Players batting average is {batting_average:.3f}")
    
    # update the count of the number of players by 1
    number_of_players += 1
    
    # ask user if they want to do this program again for the next iteration
    response = input("Do you want to do this program? Enter Yes or No: ")
    
# display count of number of players entered
print(f"Count of the number of players entered is {number_of_players}")
    
    




    