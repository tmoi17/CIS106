# while loop to ask user if they want to do the program, and use function to calculate next month's forecast based on the users input of month and sales, and display the value each time

# prompt user on whether or not they want to do this program
response = input("Do you want to do this program? Enter Yes or No: ")

# function to compute and return next month's forecast 
def next_month_forecast(month, sales):
    # determine the forecast percent based on the month 
    if month == "Jan" or month == "Feb" or month == "Mar":
        forecast_percent = 0.10
    elif month == "Apr" or month == "May" or month == "Jun":
        forecast_percent = 0.15
    elif month == "Jul" or month == "Aug" or month == "Sep":
        forecast_percent = 0.20
    elif month == "Oct" or month == "Nov" or month == "Dec":
        forecast_percent = 0.25
    
    # calculate next month's sales 
    next_month_sales = sales * (1 + forecast_percent)
    
    # sends next_month_sales value back to where the function is called 
    return next_month_sales 
    
# enter while loop if response is Yes, and iterate until response is not Yes
while response == "Yes":
    # prompt user for last name, month, and sales 
    last_name = input("What is your last name? ")
    month = input("What is the month? ")
    sales = float(input("What is the sales? $"))
    
    # function next_month_forecast is called and python now substitutes month and sales entered and goes back into the function and calculates next month's sales
    next_month_sales = next_month_forecast(month, sales)
    
    # display the value of next month's sales
    print(f"Next month's sales is {next_month_sales:.2f}")
    
    # ask user if they want to do this program again for the next iteration
    response = input("Do you want to do this program? Enter Yes or No: ")
    