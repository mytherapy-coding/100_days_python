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