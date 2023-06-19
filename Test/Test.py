from math import *


def coordinates(rad, interval):
    div = 360 // interval
    coordin = []
    for i in range(0, interval, 1):
        y = (sin(i*div*(pi/180))*rad)
        x = (cos(i * div * (pi / 180)) * rad)
        coordin.append((x, y))
    return coordin


print(coordinates(4, 5))


