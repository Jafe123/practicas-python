temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "fueron los días calurosos.")

#temperatura mas alta
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("La temperatura más alta fue:", highest)

