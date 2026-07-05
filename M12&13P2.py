# 2 arrays(parallel arrays), first for last names, second for exam scores, then display the last names and their respective exam scores

# assign 10 last names to an array and assign the corresponding exam scores in another array
last_names = ['Moi', 'Jordan', 'Mok', 'Wilson', 'Krieg', 'Smith', 'Miller', 'Lange', 'Dolen', 'Lee']
exam_score = [97, 85, 90, 93, 82, 85, 76, 54, 63, 91]

# function using a for loop with last_names and exam_score as parameters to display last names by iterating through all the last names in the array and their respective exam score 
def display_name_score(last_names, exam_score):
    # goes through each item in the last_names and exam_score arrays and outputs the last name and exam score given the same exact index. len(last_names) is equal to 10 which means range(10) goes from 0 to 9. 
    for index in range(len(last_names)):
        print(last_names[index] + "'s score is", exam_score[index])
        
# call function display_name_score
print("Last names and their respective exam score displayed: ")  
display_name_score(last_names, exam_score)

# add a blank line 
print()

# function to display last names with their respective exam scores in reverse order 
def reverse_names_score(last_names, exam_score):
    # l stores the number of names that are in the list which is 10 
    l = len(last_names)
    # Since l is 10, the last index is 9, which is where it starts. l-1 is 9. -1 in the middle tells python to stop BEFORE reaching -1. -1 at the end means the loop moves backward by one each time. 
    for i in range (l-1, -1, -1):
        # i is the current index from the list. last_names[i] and exam_score[i] gets the name and exam score stored at that index
        print(last_names[i] + "'s score is", exam_score[i])
    
# call function reverse_names_score  
print("Last names with respective exam scores displayed in reverse order: ")
reverse_names_score(last_names, exam_score)