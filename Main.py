from configparser import MAX_INTERPOLATION_DEPTH
from pickle import FALSE, TRUE
import random
import numpy as np
import matplotlib.pyplot as plt
# Bar class: objects contain name, max population, current population, and capacity of the bar
class Bar:
    # notes: self.currentPopulation should always begin at 0, self.capacity at .001
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
        print("\n List of all Bars: ")
        for x in self.BarsList:
            print(x.name + ": " + str(x.currentPopulation) + " out of " + str(x.maxPopulation))
            x.calculateCapacity()
            print("   Capacity: " + str(x.capacity) + "\n")
        
        chosen_dict= {} #chosen dict maps bars to their current cpacities
        arr = self.barChoice()
        print("Recommended Bars:")
        for x in arr:
            print(x.name + ", ")
            chosen_dict[x.name]=''

        for x in self.BarsList:
            if x.name in chosen_dict:
                x.calculateCapacity()
                chosen_dict[x.name] = x.capacity

        # displays recommended bars and their current percent capacities
        barnames = list(chosen_dict.keys())
        capacities = list(np.round(list(chosen_dict.values()), decimals=2)*100)
        fig = plt.figure(figsize = (8,5))
        plt.ylim(0,100)
        plt.yticks(range(0,101,10))
        plt.title('Recommended Bars and Their Capacities',fontweight='bold')
        plt.xlabel('Bars',fontweight='bold')
        plt.ylabel('Percent Capacity\n(out of 100%)',fontweight='bold')
        plt.bar(barnames, capacities)
        plt.show()

            
    #finds the total number of people that all bars in NB can hold
    def setTotalPopulation(self):
        for x in self.BarsList:
            self.totalPopulation += x.maxPopulation

    # initializes all bars with a population, proportional to their stake in total population of all bars
    # ensures that higher capacity bars will have more people than smaller bars 
    # 70% (configurable) of total population is calculated, then distributed among all bars
    def initializer(self):

        self.setTotalPopulation()

        length = len(self.BarsList)
        inverseList = list()

        for x in self.BarsList:
            inverse = x.maxPopulation/self.totalPopulation
            inverseList.append(inverse)

        movingPeople = int(.70*self.totalPopulation)

        while (movingPeople > 0):
            index = random.randint(0, length-1)
            chance = random.random()

            if (self.BarsList[index].currentPopulation >= self.BarsList[index].maxPopulation):
                continue

            if chance < inverseList[index]:
                self.BarsList[index].currentPopulation += 1
                movingPeople -= 1

    # method that simulates people moving from bar to bar, will be run multiple times over the course
    # of the simulation.  A bar hotness variable is generated to represent desire to leave or go to bar
    # 40% (configurable) of population is removed, then added back in accordance to bar hotness
    def shmovement(self):
        movingPeople = 0

        for x in self.BarsList:
            tempMoving = int(.40*x.currentPopulation)
            movingPeople += tempMoving
            x.currentPopulation -= tempMoving

        length = len(self.BarsList)
        hotnessList = list()

        for x in self.BarsList:
            hotness = random.random();
            hotnessList.append(hotness)

        while (movingPeople > 0):
            index = random.randint(0, length-1)
            chance = random.random()

            if (self.BarsList[index].currentPopulation >= self.BarsList[index].maxPopulation):
                continue

            if chance < hotnessList[index]:
                self.BarsList[index].currentPopulation += 1
                movingPeople -= 1
        

    # Method to generate recommendations for bars based on capacity. Begins with a capacity
    # window of 65 - 70% (configurable), and increases the size of the window if there are no bars that 
    # satisfy the threshold. Always will return 3 or 4 bars for the user.
    # parameters are set so a full bar (95 - 100% capacity) will never be recommended
    def barChoice(self):
        sortedBars = sorted(self.BarsList, key=lambda x: x.capacity)
        chosenBars = []
        lower = .65
        upper = .7
        breakState = TRUE 

        while breakState is TRUE:
            for x in sortedBars:
                if(x.capacity >= lower and x.capacity <= upper):
                    chosenBars.append(x)
                    sortedBars.remove(x)
        
            if len(chosenBars) < 3:
                if (upper + .05) < 1:
                    upper += .05

                if (lower - .05) > 0:
                    lower -= .05
            else:
                breakState = FALSE
            
        if len(chosenBars) > 4:
            chosenBars = chosenBars[0:4]

        return chosenBars

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

#main method to make function calls
if __name__ == "__main__":
    Bars = readBars()
    Simulator = Simulation(Bars)
    Simulator.initializer()
    Simulator.getBarData()
    
    Simulator.shmovement()
    print("//////////////////////////////")
    Simulator.getBarData()