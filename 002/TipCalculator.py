# Printing the welcome message.
print("Welcome to the tip calculator.")

# Getting the bill total minus the tip.
bill_minus_tip = float(input("What was the total bill? "))

# Dividing the tip percentage by 100, resulting in the value 0.12 and the addition of 1 is accounting for the bill amount without the tip. Resulting value is 1.12.
tip_percentage = float(input("How much tip would you like to give? 10, 12 or 15 percent? ")) / 100 + 1

# Getting the number of people to split the bill between
number_of_people = int(input("How many people to split the bill? "))

# Calculating the total each person should pay and spitting out the value with two decimal places.
bill_total_per_person = bill_minus_tip * tip_percentage / number_of_people
print(f"Each person should pay: {bill_total_per_person:0.2f}")
