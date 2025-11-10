import sys

# If user provides salary input
if len(sys.argv) == 2:
    salary = float(sys.argv[1])
else:
    # Default salary if no input is given
    print("No input provided. Using default salary: 50000")
    salary = 50000.0

# Calculate 10% bonus
bonus = salary * 0.10
total_salary = salary + bonus

# Display results
print("Bonus Amount:", bonus)
print("Total Salary after adding Bonus:", total_salary)
