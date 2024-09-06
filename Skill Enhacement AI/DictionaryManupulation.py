# Create initial dictionary
students = {"John": 85, "Alice": 92, "Bob": 78}

# Add a new student
students["Diana"] = 88

# Remove a student
students.pop("Bob")

# Update a student's score
students["Alice"] = 95

# Print all student names and scores
for name, score in students.items():
    print(f"{name}: {score}")
