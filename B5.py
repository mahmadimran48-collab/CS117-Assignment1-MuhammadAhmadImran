def ohms_current(v, r):
    """Calculate current using Ohm's Law: I = V / R"""
    return v / r

def power_dissipated(i, r):
    """Calculate power dissipation: P = I^2 * R"""
    return (i ** 2) * r

v_val = 12.0
r_val = 6.0

current = ohms_current(v_val, r_val)
power = power_dissipated(current, r_val)

print(f"Current = {current:.1f} A")
print(f"Power = {power:.1f} W")
