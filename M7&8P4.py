# displaying items, with their respective quantity, price, and extended price. Also display sum of all extended prices, count of number of orders, and average order

# text file created with 4 items and their respective quantities and prices 
with open('item_info.txt', 'w') as file:
    file.write('wallet\n')
    file.write('5\n')
    file.write('12\n')
    file.write('lotion\n')
    file.write('8\n')
    file.write('3\n')
    file.write('neosporin\n')
    file.write('13\n')
    file.write('4\n')
    file.write('headphones\n')
    file.write('6\n')
    file.write('50\n')

# open file for reading item data
f = open("item_info.txt", "r")

# initially set the count of number of orders and sum of extended prices to 0 
count_of_orders = 0 
sum_extended_prices = 0

# get first data line
item = str(f.readline().rstrip('\n'))

# process each item in the file until the end of the file is reached
while item != "":
    # read the quantity and price for the current item
    quantity = int(f.readline())
    price = float(f.readline())
    
    # calculate the extended price
    extended_price = quantity * price
    
    # update the sum of extended prices and increase the count of number of orders by 1
    sum_extended_prices = sum_extended_prices + extended_price
    count_of_orders = count_of_orders + 1
    
    # display a line of data
    print(f"Item is: {item}")
    print(f"Quantity is: {quantity}")
    print(f"Price is: ${price:.2f}")
    print(f"Extended Price is: ${extended_price:.2f}")
    
    # read the next item for the next loop iteration
    item = str(f.readline().rstrip('\n'))

# display total extended price and number of orders
print(f"Total Extended Prices: ${sum_extended_prices:.2f}")
print(f"Number of Orders: {count_of_orders}")

# calculate the average order 
average_order = sum_extended_prices / count_of_orders

# display the cost of the average order
print(f"Average Order: ${average_order:.2f}")

