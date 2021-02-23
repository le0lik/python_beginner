from itertools import cycle
from time import sleep


class TrafficLight:
    __timings = {'red': 7, 'yellow': 2, 'green': 5}

    def __init__(self):
        self.__color = ['red', 'yellow', 'green', 'yellow']

    def __rotate(self):
        self.__color.append(self.__color.pop(0))

    def running(self, turns):
        for i in range(turns):
            print(self.__color[0])
            sleep(TrafficLight.__timings[self.__color[0]])
            self.__rotate()


tr = TrafficLight()
tr.running(4)
tr.running(2)