from math import *

def pi_sin_cos_list(x):
    y = []
    z = []

    for i in range(len(x)):
        y.append(round(pi/2 - x[i], 2))
        z.append(round(cos((radians(x[i]))) - sin((radians(x[i]))), 2))

    return y, z


