import numpy as np

# 2D array: rows = people, columns = days (Mon–Fri)
steps = np.array([
    [4500, 5200, 4800, 5500, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
])

# Loop through each person and summarize data
for i in range(steps.shape[0]):
    total_steps = np.sum(steps[i])
    average_steps = np.mean(steps[i])
    min_steps = np.min(steps[i])
    max_steps = np.max(steps[i])

    print(
        f"Friend {i + 1} - Total Steps: {total_steps} | "
        f"Average: {average_steps:.1f} | "
        f"Min: {min_steps} | "
        f"Max: {max_steps}"
    )
