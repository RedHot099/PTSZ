import sys
import math
import random


class Generator:
    def __init__(self, range, maxDuration = 5, maxReady = 20, maxDuedate = 8, maxWeight = 10, name = 'test'):
        self.range = range
        self.result = [range]
        self.name = name
        self.maxDuration = maxDuration
        self.maxReady = maxReady
        self.maxDuedate = maxDuedate
        self.maxWeight = maxWeight
        self.generate()
        self.print()
        self.save2file()

    def print(self):
        for i in self.result:
            print(i)

    def generate(self):
        for i in range(0,self.range):
            #wylosowanie czasu gotowości
            ready = random.randint(0, self.maxReady)
            #wyznaczenie limitu zakończenia zadania
            duedate = ready + random.randint(0, self.maxDuedate)
            #wyznaczenie długości trwania zadania
            duration = random.randint(1, self.maxDuration)
            while not(duration <= (duedate - ready)):
                duration = random.randint(1, self.maxDuration)
            #wyznaczenie wagi zadania
            weight = random.randint(1, self.maxWeight)
            self.result.append([duration, ready,duedate,weight])

    def save2file(self):
        file = open('./' + self.name + '.txt', 'w')
        file.write(str(self.result[0]) + ' \n')
        for i in self.result[1:]:
            for j in i:
                file.write(str(j) + ' ')
            file.write('\n')
        file.close()


if __name__ == '__main__':
    gen = Generator(10)