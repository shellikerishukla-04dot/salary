def calculate_salary_with_bonus(basic_salary, bonus_rate=0.10):
    """
    Takes the basic salary and a bonus rate,
    returns a tuple (bonus_amount, total_salary).
    """
    bonus = basic_salary * bonus_rate
    total_salary = basic_salary + bonus
    return bonus, total_salary

# Input from user
basic_salary = int(input("Enter the basic salary of the employee: "))

# Call the function
bonus_amount, total_salary = calculate_salary_with_bonus(basic_salary)

# Print results
print(f"Bonus = {bonus_amount:.2f}")
print(f"Total salary after adding bonus = {total_salary:.2f}")
