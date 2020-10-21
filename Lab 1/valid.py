import sys


class Walidator:
    def __init__(self, nameIn = 'test.txt', nameOut = 'kolejka.txt'):    
        self.fileIn = open('./' + nameIn , 'r')
        self.fileOut = open('./' + nameOut, 'r')
        self.range = 0
        self.input = []
        self.score = 0
        self.order = []
        self.read()
        #self.check()
        self.valid()

    #odczyt plików
    def read(self):
        for i in self.fileIn:
            i = i.replace(' \n', '')
            i = i.replace('\n', '')
            i = i.replace(' ',',')
            tmp = [int(j) for j in i.split(',')]
            self.input.append(tmp)
        self.range = self.input[0][0]
        #print(self.input)
        self.score = self.fileOut.readline()
        self.order = self.fileOut.readline()
        self.order = [int(i) for i in self.order.split(' ')]
        #print(self.order)

    #sprawdzenie poprawności plików
    def check(self):
        for i in self.input:
            if (i[1] >= i[2]) or (i[2]-i[1] < i[0]):
                print("Niepoprawne dane!")
                return 0
        return 1

    #obliczenie kary wczytaych plików
    def valid(self):
        penalty = 0
        time = 0
        for i in self.order:
            if self.input[i][1] > time:
                time = self.input[i][1]
            time += self.input[i][0]
            if self.input[i][2] < time:
                penalty += self.input[i][3]
        print("Wyliczona kara za opóźnienia wynosi: ", penalty)
        print("Podana w pliku kara za opóźnienie wynosi: ", self.score)


if __name__ == '__main__':
    val = Walidator()