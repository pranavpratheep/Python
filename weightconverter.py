Weight = input("Enter your weight: ")
unit = input('L(bs) or K(g): ')
if unit.upper() == "L":
    converted = int(Weight) * 0.45
    print(f"You are {converted} kilos ")
else:
    converted = int(Weight) / 0.45
    print(f"You are {converted} kilos ")