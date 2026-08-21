english = int(input("English = "))
maths = int(input("Maths = "))
science = int(input("Science = "))

total = english + maths + science
percantage = (total / 300) * 100

if english < 33 or maths < 33 or science < 33 :print(f"total marks = {total} and percantage = {percantage} fail")
elif percantage >= 33 :print(f"total marks = {total} and percantage = {percantage} pass")
else:print(f"total marks = {total} and percantage = {percantage} fail") 