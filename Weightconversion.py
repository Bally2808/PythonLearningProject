weight = int(input("Weight: "))
unit = input("(L)bs or (K): ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight // 0.45
    print(f"You are {converted} lbs")

print("Have a nice day")