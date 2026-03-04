
student = {}

# Collect student info
name = input("Enter your name: ")
age = input("Enter your age: ")
subject = input("Enter your favorite subject: ")

# Store the info in the dictionary
student["name"] = name
student["age"] = age
student["subject"] = subject

# Display the student record
print("\nStudent Record:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Favorite Subject:", student["subject"])