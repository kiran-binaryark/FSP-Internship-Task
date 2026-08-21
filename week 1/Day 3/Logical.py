name = input("enteer your name = ")
age = int(input("your age = "))
bjp_Supporter = str(input("are you a bjp supporter = "))


if age >= 18 and bjp_Supporter == "yes":
    drink_and_drive = True
    print(f"{name} is allowed to drive and drink")
else:
    print(f"{name} get out from here")
