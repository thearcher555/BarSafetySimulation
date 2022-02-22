#Bar object to hold all variables
#Array of bars will be used to index all entries
class Bar:
    name = ""
    maxPopulation = -1
    currentPopulation = -1
    capacity = .001

    def setMaxPop(num):
        maxPopulation = num

    def calculateCapacity():
        capacity = currentPopulation/maxPopulation

    def updatePop(num):
        currentPopulation = num
        calculateCapacity()

    def setName(newName):
        name = newName

Bars = []

#Create way to import bar data from text file
with open ('NewBrunswickBars.txt', 'r') as reader:
    Bars.append()


#Simulation code








