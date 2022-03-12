#Bar object to hold all variables
#Array of bars will be used to index all entries
class Bar:
    def __init__(self,name,maxPopulation, currentPopulation=-1, capacity = .001):
        self.name = str(name)
        self.maxPopulation = int(maxPopulation)

    def setMaxPop(self, num):
        maxPopulation = num

    def calculateCapacity(self):
        capacity = currentPopulation/maxPopulation

    def updatePop(self, num):
        currentPopulation = num
        calculateCapacity()

    def setName(self, newName):
        name = newName

Bars = []

#Create way to import bar data from text file
with open ('NewBrunswickBars.txt', 'r') as f:
    for line in f:
        line.split(",")
        num = type(int(line[1]))
        temp = Bar(line[0],num)
        Bars.append(temp)


#Simulation code









