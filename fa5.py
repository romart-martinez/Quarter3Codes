import numpy as np

# 2D array: rows = people, columns = days (Mon–Fri)
steps = np.array([
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
])

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Calculate total steps per day (sum by column)
daily_totals = np.sum(steps, axis=0)

# Print total steps for each day
print("Total steps per day:")
for i in range(len(days)):
    print(f"{days[i]}: {daily_totals[i]} steps")

# Identify the most active day
most_active_index = np.argmax(daily_totals)
most_active_day = days[most_active_index]

print(f"\nMost active day overall: {most_active_day}")