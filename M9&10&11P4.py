# displaying the out the door price of a car given the make, model, electric vehicle code, and MSRP. Also display the sum of all MSRP's and sum of all sale price of the cars

# prompt user on whether or not they want to do this program
response = input("Do you want to do this program? Enter Yes or No: ")

# intitially set the value of the sum of all MSRP's and sum of all sales price of the cars to 0 
sum_all_MSRP = 0
sum_all_sale_price = 0 

# function to compute and return the out the door price
def compute_door_price(MSRP, make, model, electric_vehicle_code):
    if make == "Honda" and model == "Accord" and electric_vehicle_code == "N":
        percent_off_MSRP = 0.10
    elif make == "Toyota" and model == "Rav4" and electric_vehicle_code == "N":
        percent_off_MSRP = 0.15
    elif electric_vehicle_code == "Y":
        percent_off_MSRP = 0.30
    elif electric_vehicle_code == "N":
        percent_off_MSRP = 0.05
    
    # calculate the new MSRP
    new_MSRP = MSRP * (1 - percent_off_MSRP)
    
    # calculate the sales tax
    sales_tax = new_MSRP * 0.07
    
    # add 7% sales tax to the total
    out_the_door_price = new_MSRP + sales_tax
    
    # sends the out_the_door_price value back to where the function is called
    return out_the_door_price

# enter while loop if response is Yes, and iterate until response is not Yes
while response == "Yes":
    # prompt user for the make, model, electric_vehicle_code, and MSRP
    make = input("What is the make? ")
    model = input("What is the model? ")
    electric_vehicle_code = input("What is the electric vehicle code? Y or N? ")
    MSRP = float(input("What is the sticker price of the automobile? $"))
    
    # function compute_door_price is called and python now substitutes MSRP, make, model, electric_vehicle_code entered and goes back into the function and calculates the out the door price
    out_the_door_price = compute_door_price(MSRP, make, model, electric_vehicle_code)
    
    # update the sum of all MSRP's and sum of all sale prices of the cars
    sum_all_MSRP = sum_all_MSRP + MSRP
    sum_all_sale_price = sum_all_sale_price + out_the_door_price
    
    # display the total
    print(f"The total is ${out_the_door_price:.2f}")
    
    # ask user if they want to do this program again for the next iteration
    response = input("Do you want to do this program? Enter Yes or No: ")
    
# display the sum of all MSRP's and the sum of all sales price of the cars
print(f"Sum of all MSRP's is ${sum_all_MSRP:.2f}")
print(f"Sum of all sale price of the cars is ${sum_all_sale_price:.2f}")
