import math 
import classes

lines = []

n = int(input())
lines = []
for k in range(n):
    line = input()
    lines.append(line)

no_of_polygons = n

polygons = []

for polys in range(0,int(no_of_polygons)):
    polygons.append(classes.Polygon())

i = 0
j = 0
striped_line = []

for i in range(0,len(lines)):
    this_line = lines[i]
    striped_line = this_line.split()
    polygons[j].no_of_pairs = striped_line[0]
    polygons[j].x_vals = []  
    polygons[j].y_vals = []
    for xvals in range(1,len(striped_line),2):
        polygons[j].x_vals.append(striped_line[xvals])
    for yvals in range(2,len(striped_line),2):
        polygons[j].y_vals.append(striped_line[yvals])
    j += 1

result = []

for l in range(0, int(no_of_polygons)):
  result.append(classes.polygon_area(polygons[l].x_vals,polygons[l].y_vals,int(polygons[l].no_of_pairs)))
  print(f"{result[l]}")






     


