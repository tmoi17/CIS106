# part number, cost per unit, and total cost 

# prompt user to enter a part number 
part_number = input("Enter a part number: ")

# prompt user to enter a quantity
quantity = int(input("Enter the quantity of an item: "))

# determine unit cost based on part number 
if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00 
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00
    
# calculate total cost 
total_cost = quantity * unit_cost 

# display result 
print(f"part number is {part_number}")
print(f"cost per unit is ${unit_cost:.2f}")
print(f"total cost is ${total_cost:.2f}")
