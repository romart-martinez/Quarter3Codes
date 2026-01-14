import numpy as np

names = ["Givi", "Akhmat", "Motorola"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],   # Givi
    [4000, 4100, 3900, 4200, 4600],   # Akhmat
    [6000, 5800, 5900, 6100, 6200]    # Motorola
])


givi = 0
akhmat = 1
motorola = 2
wednesday = 2
thursday = 3

print("Motorola's steps on Wednesday:", steps[motorola][wednesday])

print("Givi's steps:", steps[givi].tolist())

print("Updating Givi's Thursday steps to 5500.")
steps[givi][thursday] = 5500

print("Updated steps:", steps[givi].tolist())
