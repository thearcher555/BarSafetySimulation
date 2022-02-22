class Bar:
    name = "";
    maxPopulation = -1
    currentPopulation = -1
    capacity = .001;

    def setMaxPop(num):
        maxPopulation = num;

    def calculateCapacity():
        capacity = currentPopulation/maxPopulation

    def updatePop(num):
        currentPopulation = num;
        calculateCapacity()

Bars = []

#Create way to import bar data from text file

#Simulation code








