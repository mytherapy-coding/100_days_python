age = int(input("What is your age: "))

def life_in_weeks(age: int):
    return (90 - age) * 365 // 7

weeks_left = life_in_weeks(40)
print(f'You have {weeks_left} weeks left')
    
print((90 - age) * 52)    