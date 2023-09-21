# Input the number of books and cost per book
num_books = int(input("Enter the number of books to order: "))
cost_per_book = float(input("Enter the cost per book: "))

# Calculate the order total
order_total = num_books * cost_per_book

# Calculate the shipping charge
if order_total > 50.00:
    shipping_charge = 0.00  # Free shipping
else:
    shipping_charge = 25.00

# Display the order total and shipping charge
print(f"Order Total: ${order_total:.2f}")
print(f"Shipping Charge: ${shipping_charge:.2f}")




