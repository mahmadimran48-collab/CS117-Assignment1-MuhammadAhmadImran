readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

above_3_2_count = 0
highest = readings[0]
lowest = readings[0]
total_sum = 0.0
count = 0

for r in readings:
    if r > 3.2:
        above_3_2_count += 1

    if r > highest:
        highest = r
        
    if r < lowest:
        lowest = r
        
    total_sum += r
    count += 1

average = total_sum / count

print(f"Readings above 3.2 V: {above_3_2_count}")
print(f"Highest: {highest} V")
print(f"Lowest: {lowest} V")
print(f"Average: {average:.2f} V")
