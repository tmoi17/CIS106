# Allow user to enter quantities and prices in while loop. Function to compute total. Display quantity, price, and total. Sum and display total extended price. 

# prompt user on whether or not they want to do this program
response = input("Do you want to do this program? Enter Yes or No: ")

# intitially set the total extended price value to 0 
total_extended_price = 0 

# function to compute and return total which is quantity times price, if total greater than 100000, then apply a 10% discount
def compute_total(quantity, price):
    total = quantity * price
    if total > 100000:
        total = 0.90 * total
    else: 
        total = total 
        
    # sends total back to where the function is called 
    return total

# enter while loop if response is Yes, and iterate until response is not Yes
while response == "Yes":
    # prompt the user to enter quantity and price
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: $"))
    
    # function compute_total is called and python now substituites quantity and price entered and goes back into the function and calculates the total
    total = compute_total(quantity, price)
        
    # update total extended price value 
    total_extended_price = total_extended_price + total
    
    # display quantity, price, and total of item
    print(f"Quantity is {quantity}")
    print(f"Price is ${price:.2f}")
    print(f"Total is ${total:.2f}")
    
    # ask user if they want to do this program again for the next iteration
    response = input("Do you want to do this program? Enter Yes or No: ")

# display the total extended price for all items 
print(f"Total extended price is ${total_extended_price:.2f}")