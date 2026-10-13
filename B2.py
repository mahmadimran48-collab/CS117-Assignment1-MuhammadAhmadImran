n = int(input("How many resistors? "))
total_resistance = 0.0

for i in range(1, n + 1):
    r = float(input(f"Enter R{i}: "))
    total_resistance += r

print(f"Total resistance = {total_resistance} ohm")
