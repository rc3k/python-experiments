import time
from collections import deque


class TrainCompositionList:

    def __init__(self):
        self.wagons = []

    def attach_wagon_from_left(self, wagonId):
        self.wagons.insert(0, wagonId)

    def attach_wagon_from_right(self, wagonId):
        self.wagons.append(wagonId)

    def detach_wagon_from_left(self):
        return self.wagons.pop(0)

    def detach_wagon_from_right(self):
        return self.wagons.pop()


class TrainCompositionDeque:

    def __init__(self):
        self.wagons = deque()

    def attach_wagon_from_left(self, wagonId):
        self.wagons.appendleft(wagonId)

    def attach_wagon_from_right(self, wagonId):
        self.wagons.append(wagonId)

    def detach_wagon_from_left(self):
        return self.wagons.popleft()

    def detach_wagon_from_right(self):
        return self.wagons.pop()


def attach_then_detach(train, number):
    for i in range(0, number, 2):
        train.attach_wagon_from_right(i)
        train.attach_wagon_from_left(i + 1)
    for i in range(0, number, 2):
        train.detach_wagon_from_right()
        train.detach_wagon_from_left()


if __name__ == "__main__":
    start_time = time.time()

    train = TrainCompositionDeque()
    print("--- Using deque (One hundred thousand attached and detached) ---")
    attach_then_detach(train, 100000)
    print("--- {} seconds ---".format(time.time() - start_time))

    train = TrainCompositionList()
    print("--- Using list (One hundred thousand carriages attached and detached) ---")
    attach_then_detach(train, 100000)
    print("--- {} seconds ---".format(time.time() - start_time))
