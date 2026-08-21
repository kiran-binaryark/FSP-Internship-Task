salary = int(input("salary ="))

HRA = (salary * 20) / 100
DA = (salary * 10) / 100

print("House Rent allowence = ",HRA)
print("Dearness Allowance = ",DA)

print(" Gross Salary = ",salary + HRA + DA)