# Answer 1
with open('day1data.txt') as f:
    total = 0
    for mod in f.readlines():
        total += int(mod)//3 - 2
    print(total)


# Answer 2
def fuel_fuel(x):
   fuel = x//3-2
   return x + (fuel_fuel(fuel) if fuel > 0 else 0)

with open('day1data.txt') as f:
    total = 0
    for mod in f.readlines():
        total += fuel_fuel(int(mod)//3 - 2)
    print(total)