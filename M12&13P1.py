# function to display 10 last names by first assigning them to an array, and another function to display those last names in reverse order  

# assign 10 last names to an array
last_names = ['Moi', 'Jordan', 'Mok', 'Wilson', 'Krieg', 'Smith', 'Miller', 'Lange', 'Dolen', 'Lee']

# function using a for loop to display last names by iterating through all the last names in the array
def display_names():
    for name in last_names:
        print(name)
            
# call function to display_names 
print("Last names displayed: ")
display_names()

# function to display last names in reverse order 
def reverse_names():
    # l stores the number of names that are in the list which is 10 
    l = len(last_names)
    # Since l is 10, the last index is 9, which is where it starts. l-1 is 9. -1 in the middle tells python to stop BEFORE reaching -1. -1 at the end means the loop moves backward by one each time. 
    for i in range (l-1, -1, -1):
        # i is the current index from the list. last_names[i] gets the name stored at that index
        print(last_names[i])
    
# call function reverse_names  
print("Last names displayed in reverse order: ")
reverse_names()