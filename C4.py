def loaded_divider(source_v, r_upper, r_lower, r_load):
    parallel_comb = (r_lower * r_load) / (r_lower + r_load)
    
    actual_voltage = source_v * (parallel_comb / (r_upper + parallel_comb))
    
    ideal_voltage = source_v * (r_lower / (r_upper + r_lower))
    
    return (float(ideal_voltage), float(actual_voltage))

if __name__ == "__main__":
    test_output = loaded_divider(12, 1000, 1000, 500)
    print(f"loaded_divider(12, 1000, 1000, 500) -> {test_output}")
