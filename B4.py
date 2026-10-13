voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

max_streak = 1
current_streak = 1
start_val = voltages[0]
end_val = voltages[0]

curr_start = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        current_streak += 1
        end_val = voltages[i]
    else:
        if current_streak > max_streak:
            max_streak = current_streak
            start_val = curr_start
        
        current_streak = 1
        curr_start = voltages[i]
        end_val = voltages[i]

if current_streak > max_streak:
    max_streak = current_streak
    start_val = curr_start

print(f"Longest continuous drop: {max_streak} minutes")
print(f"Started at: {start_val} V")
print(f"Ended at: {end_val} V")
