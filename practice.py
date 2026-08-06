
salary = int(input("enter the salary amount: "))
rating = int(input("enter the rating: "))
years_experience = int(input("enter the years_experience: "))
attendance = float(input("enter the total attendance: "))
total_bonus = 0

if rating == 5:
    total_bonus += salary * 0.25
elif rating == 4:
    total_bonus += salary * 0.15
elif rating == 3:
    total_bonus += salary * 0.10
else:
    print("No performance Bonus")

if years_experience > 10:
    total_bonus += salary * 0.10
elif 5 <= years_experience <= 10:
    total_bonus += salary * 0.5
else:
    print("No additional bonus")

if attendance >= 95:
    total_bonus += salary + 5000
elif 85 <= attendance <= 94:
    total_bonus += salary + 2000
else:
    print("No attendance Bonus")

final_bonus = total_bonus
print(f"Final Bonus:  ₹{final_bonus}")

