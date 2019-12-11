from serialutil import GcodeSender
from pointutil import inverseKinematics, interpolatePoints, convertWaypoints
from operator import itemgetter
import math
import time


def square():
    a = convertWaypoints([100,100], [100, 150])
    b = convertWaypoints([100, 150], [150, 150])
    c = convertWaypoints([150, 150], [150, 100])
    d = convertWaypoints([150, 100], [100, 100])
    points = []
    points.append(a)
    points.append(b)
    points.append(c)
    points.append(d)
    sender.sendangle(*inverseKinematics(100,100))
    time.sleep(3)
    t=0.1
    for n in a:
        sender.sendangle(*n)
        print(*n)
        time.sleep(t)

    for n in b:
        sender.sendangle(*n)
        print(*n)
        time.sleep(t)

    for n in c:
        sender.sendangle(*n)
        print(*n)
        time.sleep(t)


    for n in d:
        sender.sendangle(*n)
        print(*n)
        time.sleep(t)


def circle():
    a = inverseKinematics(150, 150)
    b = inverseKinematics(100, 140)
    c = inverseKinematics(50, 130)
    d = inverseKinematics(0, 120)
    e = inverseKinematics(50, 130)
    f = inverseKinematics(100, 140)
    g = inverseKinematics(150, 150)

    sender.sendangle(*a)
    time.sleep(1)
    sender.sendangle(*b)
    time.sleep(1)
    sender.sendangle(*c)
    time.sleep(1)
    sender.sendangle(*d)
    time.sleep(1)
    sender.sendangle(*e)
    time.sleep(1)
    sender.sendangle(*f)
    time.sleep(1)
    sender.sendangle(*g)
    time.sleep(1)


def star():
    # theta = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    theta = []
    t = 0
    while t < 360 * 29:
        theta.append(t)
        t += 174
    center_point_x = 100
    center_point_y = 100
    scale = 50
    print(theta)
    for n in theta:
        x = scale * math.cos(n * math.pi / 180) + center_point_x
        y = scale * math.sin(n * math.pi / 180) + center_point_y
        #print(x, y)
        a = inverseKinematics(x, y)
        sender.sendangle(*a)
        time.sleep(1)
def spiral():
    theta = []
    t = 0
    while t < 1980:
        theta.append(t)
        t +=50
    center_point_x = 100
    center_point_y = 100
    scale = 100
    print(theta)
    for n in theta:
        x = scale * math.cos(n * math.pi / 180) + center_point_x
        y = scale * math.sin(n * math.pi / 180) + center_point_y
        print(x, y)
        a = inverseKinematics(x, y)
        sender.sendangle(*a)
        time.sleep(1)


if __name__ == "__main__":
    sender = GcodeSender()
    print(sender.serialConnection)
    sender.setup()
    sender.initializePosition(-90, 0)
    star()
    time.sleep(0.1)
    #for n in convertWaypoints([200,200],[0,200]):
    #    sender.sendangle(*n)
    #    time.sleep(.1)



# points = square()
# for n in points:
# sender.sendangle(*n)
# time.sleep(2)
