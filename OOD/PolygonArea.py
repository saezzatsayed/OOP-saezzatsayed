import math 
import classes

lines = []

while True:
    line = input()
    if not line:
        break
    lines.append(line)

no_of_Polys = int(lines[0])
polygons_array = []

k = 0
counter = 0
while k < no_of_Polys:
    polygons_array = classes.Polygon(0,0)
    k += 1
    counter += 1

i = 0

nums = len(lines)

for nums in lines:
    if i + 1 <= len(lines):
        this_line = lines[i]
        for p in polygons_array:
            polygons_array[i].no_of_pairs = this_line[0]
        if len(this_line) % 2 == 0:
            this_line = this_line[:-1]
        else:
            continue
    else:
        break
    i += 1

print(polygons_array[0].no_of_pairs)







     


