cm, kg = map(int, input().split(" "))

bmi = (kg * 10000) // (cm * cm)

if bmi >= 25:
    print(bmi)
    print("Obesity")
else:
    print(bmi)