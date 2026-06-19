# using function to compute discount price and discounted amount when given quantity, price, and discount rate. Display discounted price, discounted amount, quantity, and price

# function to compute and return the discount amount and discounted price
def discount_amount_price(quantity, price, discount_rate):
    # calculate the discount amount and discounted price
    discount_amount = quantity * price * discount_rate
    discounted_price = (quantity * price) - discount_amount
    
    return discount_amount, discounted_price
    
# prompt user on whether or not they want to do this program
response = input("Do you want to do this program? Enter Yes or No: ")

# enter while loop if response is Yes, and iterate until response is not Yes
while response == "Yes":
    # prompt user for quantity, price, and discount rate
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: $"))
    discount_rate = float(input("Enter the discount rate: "))
    
    # function discount_amount_price is called and python now substituites quantity, price, and discount_rate entered and goes back into the function and calculates both the discount amount and discounted price
    discount_amount, discounted_price = discount_amount_price(quantity, price, discount_rate)
    
    # display discounted price, discount amount, quantity, and price 
    print(f"Discounted price is ${discounted_price:.2f}")
    print(f"Discount amount is ${discount_amount:.2f}")
    print(f"Quantity is {quantity}")
    print(f"Price is ${price:.2f}")
    
    # ask user if they want to do this program again for the next iteration
    response = input("Do you want to do this program? Enter Yes or No: ")
