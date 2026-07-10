# Develop an application to store information for each dog taken in by the rescue group since I work for a non-profit dog rescue
# includes 5 functions, (main(), menu(), addDogs(), findDog(), viewDogs())

# Import the PrettyTable library so I can create and display a formatted table of dogs
from prettytable import PrettyTable

# create a new PrettyTable object to store dog information
table = PrettyTable()

# set the column names for the table
table.field_names = ["Dog", "Breed", "Age", "Weight"]

# intitially define an empty list dog_names and set the number of dogs to be 0
dog_names = [] 
num_dogs = 0 

# define function addDogs()
def addDogs():
    
    # use the global variable so I can update the total number of dogs 
    global num_dogs
    
    # prompt user for dog name, breed, age, and weight
    dog_name = input("Dog name: ")
    dog_breed = input("Dog Breed: ")
    age = int(input("Age: "))
    weight = float(input("Weight: "))
    
    # add a blank line
    print()
        
    # adds the information inputted for the dog as a list/row to the pretty table 
    table.add_row([dog_name, dog_breed, age, weight])
    
    # add the dog name inputted to a seperate list dog_names
    dog_names.append(dog_name)
    
    # increases the count of num_dogs by 1 
    num_dogs += 1

# define function findDog()
def findDog():
    # prompt the user for the name of the dog they are looking for
    search = input("Enter dog name to search: ")
    
    # initially set variable found to be False
    found = False
    
    # for loop to iterate through each index/dogs in the dog_names list
    for i in range(num_dogs):
        # if statement to find if the search is equal to a dog name in the list, then found will be set to true and it will end the loop through my break statement.
        if search == dog_names[i]:
            found = True
            print(f"Found {dog_names[i]}")
            break
    
    # if no dog was found in the dog_names list, then display that we were not able to find that dog
    if found == False:
        print(f"Sorry unable to find {search}")

# define function viewDogs()
def viewDogs():
    # print "Rescue Dogs" and then display the table/information of dogs that were added to it right under
    print("Rescue Dogs")
    print(table)
    
# define the function menu()
def menu():
    # create the dog rescue menu 
    print("Dog Rescue")    
    print("----------")

    print()
       
    print("1. Add a dog")
    print("2. View Dogs")
    print("3. Find Dog")
    print("4. Quit")

    print()

# define function main() 
def main():
    # "while True" just means that it is an infinite loop and will keep asking the user for their choice until they choose choice 4
    # Then I call the menu function to display it and ask for a choice
    # I then proceed with if statements to call a certain function (add, view, find dogs, or print goodbye) based on the choice that was inputted
    while True:
        menu()
        choice = input("Select a choice: ")
        if choice == "1":
            addDogs()
        elif choice == "2":
            viewDogs()
        elif choice == "3":
            findDog()
        elif choice == "4":
            print("Goodbye")
            break
        
# call function main()
main()
    
    
