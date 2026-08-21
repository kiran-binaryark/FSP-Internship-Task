name = input("Enter employee name = ")
salary = float(input("Enter monthly salary ="))
bonus_percentage = float(input("Enter bonus percentage = "))

bonus = (salary * bonus_percentage) / 100
Total = salary + bonus



print(f"Employee = {name}")
print(f"Monthly Salary = {salary:.2f}")
print(f"Bonus = {bonus:.2f}")
print(f"Total Salary = {Total:.2f}")

