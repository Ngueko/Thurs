# Input user's last name, number of dependents, and gross income
last_name = input("Enter your last name: ")
num_dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter your gross income: "))

# Calculate adjusted gross income
adjusted_gross_income = gross_income - (num_dependents * 12000)

# Determine the income tax rate
if adjusted_gross_income > 50000:
    tax_rate = 0.20  # 20% tax rate for AGI over $50,000
else:
    tax_rate = 0.10  # 10% tax rate for AGI $50,000 or under

# Compute income tax
income_tax = adjusted_gross_income * tax_rate

# Check if income tax is less than 0, and set it to $100 if necessary
if income_tax < 0:
    income_tax = 100

# Display the user's last name, adjusted gross income, tax rate, and income tax
print(f"Last Name: {last_name}")
print(f"Adjusted Gross Income: ${adjusted_gross_income:.2f}")
print(f"Tax Rate: {tax_rate * 100}%")
print(f"Income Tax: ${income_tax:.2f}")