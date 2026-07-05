# load last name and score from a file. Then display last name and highest score as well as last name and lowest score 

# create text file with last names and their respective scores 
with open('lastname_score.txt', 'w') as file:
    file.write('Moi\n')
    file.write('91.00\n')
    file.write('Gordon\n')
    file.write('87.00\n')
    file.write('Pratt\n')
    file.write('95.00\n')
    file.write('Johnson\n')
    file.write('78.00\n')
    file.write('Mok\n')
    file.write('83.00\n')
    file.write('Colleran\n')
    file.write('93.00\n')
    file.write('Smith\n')
    file.write('82.00\n')
    file.write('Thrall\n')
    file.write('98.00\n')
    file.write('Pederson\n')
    file.write('71.00\n')
    file.write('Black\n')
    file.write('66.00\n')
        
# open file for reading data on last name and their respective score
f = open("lastname_score.txt", "r")

# define arrays for last name and their respective scores
lastn = []
score = [] 

# get first data line
lastname = str(f.readline().rstrip('\n'))

# process each last name and score in the file by adding them to arrays until the end of the file is reached
while lastname != "":
    lastn.append(str(lastname).rstrip("\n"))
    s = float(f.readline())
    score.append(s)
    lastname = f.readline()
f.close()
        
# function to find highest and lowest score and display the name of the people with these scores
def hilow(lastn, score):
    l = len(lastn)
    
    # starts highest score to be 0 and lowest score to be 999
    hi_var = 0 
    low_var = 999 
    
    # loops through every student index in the list
    for y in range (0, l, 1):
        # checks if the current score is higher than the highest score found so far
        if score[y] > hi_var:
            # saves the position/index of the new highest score
            hiindex = y 
            # updates the highest score value
            hi_var = score[y]
        
        # checks if the current score is lower than the lowest score found so far
        if score[y] < low_var:
            # saves the position/index of the new lowest score
            lowindex = y 
            # updates the lowest score value
            low_var = score[y]
            
    print("Highest score", lastn[hiindex], score[hiindex])
    print("Lowest score", lastn[lowindex], score[lowindex])

# call function hilow 
hilow(lastn, score)