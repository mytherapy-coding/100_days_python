def life_in_weeks(age: int) -> int:
    return (90 - age) * 365 // 7


your_age = int(input("What is your age: "))
weeks_left = life_in_weeks(your_age)
print(f"You have {weeks_left} weeks left")
