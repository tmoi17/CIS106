# create text file with player names and their respective batting averages 
with open('name_batavg.txt', 'w') as file:
    file.write('Tyler Moi\n')
    file.write('0.267\n')
    file.write('Ramsey Gordon\n')
    file.write('0.453\n')
    file.write('Chris Pratt\n')
    file.write('0.349\n')
    file.write('Davis Johnson\n')
    file.write('0.489\n')
    file.write('Jordan Mok\n')
    file.write('0.634\n')
    file.write('Jeremy Bennet\n')
    file.write('0.217\n')
    file.write('Alex Krieg\n')
    file.write('0.325\n')
    file.write('Will Colleran\n')
    file.write('0.481\n')
    file.write('Ishhaan Mishra\n')
    file.write('0.312\n')
    file.write('Sam Pederson\n')
    file.write('0.599\n')

# open file for reading data on players and their batting averages
f = open("name_batavg.txt", "r")

# defines an empty dictionary for player data 
player = {}

# read the first player's name
key = str(f.readline().rstrip('\n'))
    
# process each player name and batting average in the file by adding them to the dictionary until the end of the file is reached
while key != "":
    value = float(f.readline())
    player[key] = value 
    key = str(f.readline().rstrip('\n'))
f.close()
        
# print the column headers. :<20 just means that it reserves 20 characters for the player name. Specifically, if the name is "Tyler Moi" which is 9 characters, Python automatically adds 11 spaces after it before printing the batting average
print(f"{'Player':<20}{'Batting Average':>20}")

# create a separator between the headers (Player and batting average)
print("-"*40)

# function to print dictionary contents
def print_contents():
    # display each player's name and batting average using a for loop
    for key, value in player.items():
        print(f"{key:<20}{value:>20}")
        
# call function print_contents()        
print_contents()
