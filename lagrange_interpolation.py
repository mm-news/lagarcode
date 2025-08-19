from fractions import Fraction

def L(x:Fraction, known_points:list[tuple[Fraction, Fraction]]) -> Fraction:
    """The main Lagrange Interpolation function. """
    return sum([known_points[j][1]*l(j, x, known_points) for j in range(len(known_points))], Fraction(0))

def l(j:int, x:Fraction, known_points:list[tuple[Fraction, Fraction]]) -> Fraction:
    """The adjustment function in Lagrange Interpolation"""
    result = Fraction(1)
    for i in range(len(known_points)):
        x_i = known_points[i][0]
        x_j = known_points[j][0]
        result *= (x-x_i)/(x_j-x_i) if (x_j!=x_i) else Fraction(1)
    
    return result


known_points: list[tuple[Fraction, Fraction]] = list(zip(
    [Fraction(i) for i in "76 97 103 114 97 32 67 111 100 101".split(" ")], [Fraction(k) for k in range(10)]))

for i in range(9):
    print(f"({10+i}, {L(Fraction(10+i), known_points)})")

del known_points