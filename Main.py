#Bar object to hold all variables
#Array of bars will be used to index all entries
class Bar:
    # notes: self.currentPopulation should always begin at -1, self.capacity at .001
    def __init__(self,name,maxPopulation, currentPopulation, capacity):
        self.name = str(name)
        self.maxPopulation = int(maxPopulation)
        self.currentPopulation = int(currentPopulation)
        self.capacity = int(capacity)

    def setMaxPop(self, num):
        maxPopulation = num

    def calculateCapacity(self):
        capacity = self.currentPopulation/self.maxPopulation

    def updatePop(self, num):
        self.currentPopulation = num
        self.calculateCapacity()

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









