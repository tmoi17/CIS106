# price to charge based on varying quantities of widgets 

# prompt user to enter quantity of widgets 
quantity_of_widgets = int(input("Enter the quantity of widgets: "))

# determine price based on quantity of widgets 
if quantity_of_widgets >= 5000:
    if quantity_of_widgets <= 10000:
        price = 20
    else:
        price = 10
else: 
    price = 30
    
# calculate extended price, tax, and total
extended_price = quantity_of_widgets * price  
tax = extended_price * 0.07
total = extended_price + tax

# Display result
print(f"extended price is ${extended_price:.2f}")
print(f"tax is ${tax:.2f}")
print(f"total is ${total:.2f}")

