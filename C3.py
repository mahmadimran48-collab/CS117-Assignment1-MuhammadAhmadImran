def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_accumulator = ""
    working_value = decimal_num
    
    while working_value > 0:
        remainder_bit = working_value % 2
        binary_accumulator = str(remainder_bit) + binary_accumulator
        working_value = working_value // 2
        
    return binary_accumulator

if __name__ == "__main__":
    print(f"decimal_to_binary(10) -> {decimal_to_binary(10)}")
    print(f"decimal_to_binary(25) -> {decimal_to_binary(25)}")
