# display all numbers from start value to stop value using given increment value

# prompt user to enter a start value 
start_value = int(input("Enter a start value: "))

# prompt user to enter a stop value 
stop_value = int(input("Enter an end value: "))

# prompt user to enter an increment value 
increment_value = int(input("Enter an increment value: "))

# display values from start to stop, increasing by the increment value each iteration
while start_value <= stop_value:
    print(f"{start_value}")
    start_value += increment_value 