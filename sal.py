# Input the basic salary from the user
basic_salary = float(input("Enter the basic salary of the employee: "))

# Calculate the bonus (10%)
bonus = basic_salary * 0.10

# Calculate total salary after adding bonus
total_salary = basic_salary + bonus

# Print results
print(f"Bonus = {bonus:.2f}")
print(f"Total salary after adding bonus = {total_salary:.2f}")
