def star_to_delta(r_a, r_b, r_c):
    sum_products = (r_a * r_b) + (r_b * r_c) + (r_c * r_a)

    r_ab = sum_products / r_c
    r_bc = sum_products / r_a
    r_ca = sum_products / r_b
    
    return (round(r_ab, 2), round(r_bc, 2), round(r_ca, 2))

if __name__ == "__main__":
    delta_result = star_to_delta(10, 20, 30)
    print(f"star_to_delta(10, 20, 30) -> {delta_result}")
