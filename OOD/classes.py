def polygon_area(x, y, n):
    area = 0.0

    j = n - 1
    for i in range(0,n):
        area += (float(x[j])+float(x[i])) * (float(y[j])-float(y[i]))
        j = i
    
    return float(abs(area/2.0))

class Polygon:
    no_of_pairs = 0
    x_vals = []
    y_vals = []