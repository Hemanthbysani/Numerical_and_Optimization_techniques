class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# xi--> corresponds to the new data point whose value is to be obtained
# n--> represents the number of known data points
def interpolate(f: list, xi: int, n: int) -> float:
    result = 0.0
    for i in range(n):
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)
        result += term
    return result

# creating an array of 4 known data points
f = [Data(0, 2), Data(1, 3), Data(2, 12), Data(5, 147)]
# Using the interpolate function to obtain a data point
# corresponding to x=3
# xi--> corresponds to the new data point whose value is to be obtained
# n--> represents the number of known data points defined in f
print("Value of f(6) is ", interpolate(f, 6, 4))