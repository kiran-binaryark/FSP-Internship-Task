name = input("enter product name = ")
amount = int(input("amount = "))
Quantity = int(input("quantity = "))
Discount = int(input("discount = "))

discout = (amount * Discount) / 100
total = (amount - discout) * Quantity

print(f"\n\nproduct name = {name}")
print(f"amount = {amount}")
print(f"quantity = {Quantity}")
print(f"discount = {Discount}")
print(f"total = {total}")