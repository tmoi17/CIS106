# number of tickets, price per ticket, and total cost

# prompt user to enter number of concert tickets 
concert_tickets = int(input("Enter the number of concert tickets: "))

# Determines the price per ticket based on quantity of concert tickets 
if concert_tickets >= 5:
    if concert_tickets <= 9:
        price_per_ticket = 70
    elif concert_tickets >= 10 and concert_tickets <= 24:
        price_per_ticket = 60
    elif concert_tickets >= 25:
        price_per_ticket = 50
else: 
    price_per_ticket = 75

# calculates total cost
total_cost = concert_tickets * price_per_ticket

# Display result 
print(f"There are {concert_tickets} tickets")
print(f"Price per ticket is ${price_per_ticket:.2f}")
print(f"Total cost is ${total_cost:.2f}")