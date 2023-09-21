 # Ask the user for an item and quantity
item = input("Enter an item (A or any other letter): ")
quantity = int(input("Enter the quantity: "))

# Determine the unit price based on the item
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

# Compute the extended price
extended_price = quantity * unit_price

# Display the item, unit price, and extended price
print(f"Item: {item}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")