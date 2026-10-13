def parallel_resistance(resistor_list):
    reciprocal_accumulator = 0.0
    for resistor in resistor_list:
        reciprocal_accumulator += 1.0 / resistor
    
    equivalent_resistance = 1.0 / reciprocal_accumulator
    return equivalent_resistance

if __name__ == "__main__":
    case_one = parallel_resistance([10, 10])
    case_two = parallel_resistance([100, 200, 300])
    
    print(f"parallel_resistance([10, 10]) -> {case_one:.1f}")
    print(f"parallel_resistance([100, 200, 300]) -> {case_two:.2f}")
