from configparser import MAX_INTERPOLATION_DEPTH
from pickle import FALSE, TRUE
import random

# Bar class: objects contain name, max population, current population, and capacity of the bar
class Bar:
    # notes: self.currentPopulation should always begin at -1, self.capacity at .001
    def __init__(self,name,maxPopulation,):
        self.name = str(name)
        self.maxPopulation = int(maxPopulation)
        self.currentPopulation = 0
        self.capacity = .001

    def setMaxPop(self, num):
        maxPopulation = num

    def calculateCapacity(self):
        self.capacity = self.currentPopulation/self.maxPopulation

    def updatePop(self, num):
        self.currentPopulation = num
        self.calculateCapacity()

    def setName(self, newName):
        name = newName


# Simulation class that takes in an array of Bars
# provides methods to simulate the movement of people and other calculations
class Simulation:
    #takes in the Bar array which is created from a text document
    def __init__(self, Bars = []):
        self.BarsList = []
        self.BarsList = Bars
        self.totalPopulation = 0

    def getBarData(self):
        print("\nData of Bars: ")
        for x in self.BarsList:
            print(x.name + ": " + str(x.currentPopulation) + " out of " + str(x.maxPopulation))
            x.calculateCapacity()
            print("      Capacity: " + str(x.capacity) + "\n")
            
    #finds the total number of people that all bars in NB can hold
    def setTotalPopulation(self):
        for x in self.BarsList:
            self.totalPopulation += x.maxPopulation


    def initializer(self):

        self.setTotalPopulation()

        length = len(self.BarsList)
        inverseList = list()

        for x in self.BarsList:
            inverse = x.maxPopulation/self.totalPopulation
            inverseList.append(inverse)

        movingPeople = int(.65*self.totalPopulation)

        while (movingPeople > 0):
            index = random.randint(0, length-1)
            chance = random.random()

            if (self.BarsList[index].currentPopulation >= self.BarsList[index].maxPopulation):
                continue

            if chance < inverseList[index]:
                self.BarsList[index].currentPopulation += 1
                movingPeople -= 1

    #function to choose the 5 'best' bars of an array of bars
    #picks the 5 median bars based of capacity
    #can be modified later to have an offset
    def barChoice(self):
        sortedBars = sorted(self.BarsList, key=lambda x: x.capacity)
        chosenBars = []
        lower = .6
        upper = .8
        breakState = TRUE

        while breakState:

            for x in self.BarsList:
                if(x.capacity >= lower & x.capacity <= upper):
                    chosenBars.append(x)
        
            if len(chosenBars) < 5:
                if (upper + .05) <= 1:
                    upper += .05

                if (lower - .05) > 0:
                    lower -= .05
            else:
                breakState = FALSE

        return chosenBars
        

#Simulation Code
#Population is initialized then redistributed

# helper method to read from text file
def readBars():
    #Bar object to hold all variables
    #Array of bars will be used to index all entries
    Bars = []

    # Imports lines from text file, splits name and population
    # into Bar object, and is added to Bars array
    with open ('NewBrunswickBars.txt', 'r') as f:
        for line in f:
            line = line.split(",")
            num = int(line[1])
            temp = Bar(line[0],num)
            Bars.append(temp)
    return Bars


if __name__ == "__main__":
    Bars = readBars()
    Simulator = Simulation(Bars)
    Simulator.initializer()
    Simulator.getBarData()