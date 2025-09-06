'''
def calculate_love_score(name1: str, name2: str) -> int:
    
    name1 = name1.lower()
    name2 = name2.lower()
    count1 = 0
    count2 = 0
    couple = []

    for n in name1:
        couple.append(n)
    for n in name2:
        couple.append(n)
    print(couple)
    for c in couple:
        if c in "True".lower():
            count1 += 1

    for c in couple:
        if c in "Love".lower():
            count2 += 1
    print(count1)
    print(count2)

    res = str(count1) + str(count2)
    return res


print(calculate_love_score("Alena", "Amelie"))
'''

def calculate_love_score(name1: str, name2: str) -> str:
    name1 = name1.lower()
    name2 = name2.lower()
    combined = name1 + name2

    count1 = sum(1 for c in combined if c in "true")
    count2 = sum(1 for c in combined if c in "love")

    return str(count1) + str(count2)

print(calculate_love_score("Alena", "Amelie"))
