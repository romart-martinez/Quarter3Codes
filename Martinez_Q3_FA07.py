import numpy as np

names = ["Givi", "Akhmat", "Motorola"]

steps = np.array([
    [4500, 5200, 4800, 5500, 5300],   # Givi (Thursday updated to 5500)
    [4000, 4100, 3900, 4200, 4600],   # Akhmat
    [6000, 5800, 5900, 6100, 6200]    # Motorola
])

print("=== Weekly Step Summary ===\n")

# Print each row clearly and calculate totals and averages
for i in range(len(names)):
    print(names[i], "daily steps:", steps[i].tolist())
    
    total = np.sum(steps[i])
    average = np.mean(steps[i])
    
    print("Total steps:", total)
    print("Average steps:", round(average, 2))
    print()

# Find maximum and minimum in the entire dataset
max_steps = np.max(steps)
min_steps = np.min(steps)

print("Highest step count in the dataset:", max_steps)
print("Lowest step count in the dataset:", min_steps)