# Calorie Calculator Program
# Author: Ayush Biswal
# Description: Calculates daily calorie needs based on user input.

def calorie_calculator(weight, height, age, gender):
    """
    Calculates BMR (Basal Metabolic Rate)
    weight: in kilograms
    height: in centimeters
    age: in years
    gender: 'male' or 'female'
    """
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == "female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return "Invalid gender. Please enter 'male' or 'female'."

    return bmr


def daily_calorie_needs(bmr, activity_level):
    """
    Adjusts BMR based on activity level.
    1. Sedentary (little or no exercise): BMR × 1.2
    2. Lightly active (1-3 days/week): BMR × 1.375
    3. Moderately active (3-5 days/week): BMR × 1.55
    4. Very active (6-7 days/week): BMR × 1.725
    5. Super active (twice/day workouts): BMR × 1.9
    """
    activity_factors = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }

    if activity_level not in activity_factors:
        return "Invalid activity level (choose 1-5)."

    return bmr * activity_factors[activity_level]


# --- Main Program ---
print("🔥 Calorie Calculator 🔥")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
age = int(input("Enter your age (years): "))
gender = input("Enter your gender (male/female): ")

bmr = calorie_calculator(weight, height, age, gender)
if isinstance(bmr, str):
    print(bmr)
else:
    print(f"\nYour Basal Metabolic Rate (BMR) is: {bmr:.2f} calories/day")

    print("\nChoose your activity level:")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly active (1–3 days/week)")
    print("3. Moderately active (3–5 days/week)")
    print("4. Very active (6–7 days/week)")
    print("5. Super active (twice/day workouts)")

    level = int(input("Enter your activity level (1–5): "))
    total_calories = daily_calorie_needs(bmr, level)

    if isinstance(total_calories, str):
        print(total_calories)
    else:
        print(f"\n✅ You need approximately {total_calories:.2f} calories/day to maintain your weight.")