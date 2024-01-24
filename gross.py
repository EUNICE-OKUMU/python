# Get user input for hours and rate
hours_worked = float(input("Enter the number of hours worked: "))
rate_per_hour = float(input("Enter your hourly rate: "))

# Calculate gross pay
gross_pay = hours_worked * rate_per_hour

# Print the gross pay
print(f"Your gross pay is: ${gross_pay:.2f}")
