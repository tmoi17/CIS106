# quantity, unit price, extended price, tax and total

# prompt user to enter the quantity of an item
quantity = int(input("Enter the quantity of bananas: "))

# if statement to figure out unit price 
if quantity >= 1000:
    unit_price = 3.00
elif quantity < 1000:
    unit_price = 5.00

# calculate the extended price, tax, and total
extended_price = quantity * unit_price
tax = extended_price * 0.07 
total = extended_price + tax 

# Display the result 
print(f"There are {quantity} bananas")
print(f"Unit price is ${unit_price:.2f}")
print(f"Extended price is ${extended_price:.2f}")
print(f"Tax is ${tax:.2f}")
print(f"Total is ${total:.2f}")

