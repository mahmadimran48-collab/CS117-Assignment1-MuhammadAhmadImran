voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (ohm): "))

if resistance <= 0:
    print("Invalid resistance")
else:
    current = voltage / resistance
    print(f"Current = {current:.1f} A")
    
    if current > 2.0:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
