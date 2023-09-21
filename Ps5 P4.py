# Input the name and cost of the appliance
appliance_name = input("Enter the name of the appliance: ")
appliance_cost = float(input("Enter the cost of the appliance: "))

# Calculate the warranty cost based on the appliance cost
if appliance_cost > 1000.00:
    warranty_cost = 0.10 * appliance_cost  # 10% warranty cost for appliances over $1,000
else:
    warranty_cost = 0.05 * appliance_cost  # 5% warranty cost for appliances $1,000 or less

# Calculate the total cost (appliance cost + warranty cost)
total_cost = appliance_cost + warranty_cost

# Display the name, cost of the appliance, warranty cost, and total cost
print(f"Appliance Name: {appliance_name}")
print(f"Cost of Appliance: ${appliance_cost:.2f}")
print(f"Warranty Cost: ${warranty_cost:.2f}")
print(f"Total Cost: ${total_cost:.2f}")




