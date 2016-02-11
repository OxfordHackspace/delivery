from math import ceil, sqrt

class Drone:
    def __init__(self, id, capacity, location):
        self.id = id
        self.capacity = capacity
        self.location = location
        self.turnsToDestination = 0
        self.order = None
        self.inventory = []
        self.commands = []

    def step(self):
        if self.turnsToDestination > 0 :
            self.turnsToDestination -= 1
        else:
            self.runNextCommand()

    def setTurnsLeft(destination):
        self.location = destination
        if(self.location['row'] != destination['row']) or (self.location['col'] != destionation['col']):
            rowDiffSq = (self.location['row'] - destination['row']) * (self.location['row'] - destination['row'])
            colDiffSq = (self.location['col'] - destination['col']) * (self.location['col'] - destination['col'])
            self.turnsToDestination = ceil(sqrt(rowDiffSq + colDiffSq))
        else:
            self.turnsToDestination = 0

    def load(self, items, warehouse, order):        
        weight = 0
        for item in items:
            weight += item['weight']
        
        if weigh - self.capacity < 0:
            return -1

        self.capacity -= weight

        self.inventory.extend(items)

        self.order = order
        self.warehouse = warehouse

        self.setTurnsLeft(warehouse['location'])

        return capacity
            
    def deliver(self):
        self.setTurnsLeft(self.order['location'])
        self.order = None
        self.inventory = []

    def addCommand(self, command):
        self.commands.insert(0,command)

    def runNextCommand(self):
        if len(self.commands) > 0:
            command = self.commands.pop()
            if len(command) > 1:
                command[0](*command[1:])
            else:
                command[0]()

    def isBusy(self):
        return self.turnsToDestination != 0
