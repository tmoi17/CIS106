# principle, interest rate, and interest amount for first year 

# prompt user to enter principle amount of a CD
principle = float(input("Enter principle amount of a CD: "))

# prompt user to enter year to maturity of CD
year_to_maturity = int(input("Enter the amount of years to maturity: "))

# determine the interest rate based on the principle and years to maturity
if principle >= 50000.00 and principle <= 100000.00:
    if year_to_maturity == 10:
        interest_rate = 0.05
    elif year_to_maturity == 5:
        interest_rate = 0.04
    else: 
        interest_rate = 0.02
elif principle > 100000.00:
    if year_to_maturity == 5:
        interest_rate = 0.06
    else: 
        interest_rate = 0.02
else:
    interest_rate = 0.02

# calculate first year interest
first_year_interest = principle * interest_rate 

# display result
print(f"Principle is ${principle:.2f}")
print(f"Interest rate is {interest_rate * 100}%")
print(f"Interest amount for the first year is ${first_year_interest:.2f}")

