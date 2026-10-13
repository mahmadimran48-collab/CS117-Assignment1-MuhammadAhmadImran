def compute_current(voltage_val, resistance_val):
   
    circuit_current = voltage_val / resistance_val
    return circuit_current

def compute_power(current_val, resistance_val):
    dissipated_power = (current_val ** 2) * resistance_val
    return dissipated_power

if __name__ == "__main__":
    v_source = 12.0
    r_load = 6.0
    
    current_result = compute_current(v_source, r_load)
    power_result = compute_power(current_result, r_load)
    
    print(f"Current = {current_result:.1f} A")
    print(f"Power = {power_result:.1f} W")
