import math
import classes
from typing import List

if __name__ == '__main__':
    lines: List[str] = []

    n: int = int(input())
    for k in range(n):
        line: str = input()
        lines.append(line)

    no_of_polygons: int = n

    polygons: List[classes.Polygon] = []

    for polys in range(0, int(no_of_polygons)):
        polygons.append(classes.Polygon())

    i: int = 0
    j: int = 0
    striped_line: List[str] = []

    for i in range(0, len(lines)):
        this_line: str = lines[i]
        striped_line = this_line.split()
        polygons[j].set_no_of_pairs(int(striped_line[0]))
        polygons[j].set_x_vals([])
        polygons[j].set_y_vals([])
        x_vals: List[int] = []
        y_vals: List[int] = []
        for k in range(1, len(striped_line), 2):
            x_vals.append(int(striped_line[k]))
        for k in range(2, len(striped_line), 2):
            y_vals.append(int(striped_line[k]))
        polygons[j].set_x_vals(x_vals)
        polygons[j].set_y_vals(y_vals)
        j += 1

    for l in range(0, int(no_of_polygons)):
        result: float = classes.polygon_area(
            (polygons[l].get_x_vals()), (polygons[l].get_y_vals()), polygons[l].get_no_of_pairs()
        )
        print(result)
    print("This file is being run directly")

else:
    print("This is an imported file")
     


