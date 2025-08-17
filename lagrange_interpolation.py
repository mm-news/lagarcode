def L(x:float, known_points:list[tuple[float, float]]) -> float:
    """The main Lagrange Interpolation function. """
    return sum([known_points[j][1]*l(j, x, known_points) for j in range(len(known_points))])

def l(j:int, x:float, known_points:list[tuple[float, float]]) -> float:
    """The adjustment function in Lagrange Interpolation"""
    result = 1
    for i in range(len(known_points)):
        x_i = known_points[i][0]
        x_j = known_points[j][0]
        result *= (x-x_i)/(x_j-x_i) if (x_j!=x_i) else 1
    
    return result

known_points: list[tuple[float, float]] = [(1, -4), (2, 48), (3, 188), (4, 458)]
print(L(8, known_points))

del known_points