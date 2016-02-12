import sys
from math import ceil, sqrt
from drone import Drone

class DeliveryManager:
    def __init__(self, droneCount, capacity, warehouses, orders, productTypeWeights):
        self.drones = []
        for i in range(0, droneCount):
            d = Drone(i, capacity, warehouses[0]['location'])
            self.drones.append(d)
        self.warehouses = warehouses
        self.orders = orders
        self.productTypeWeights = productTypeWeights

    def go(self):
        self.orders.sort(key=lambda order: order['itemCount'], reverse=True)

        while len(self.orders) > 0:
            order = self.orders.pop()
            for iType in order['itemTypes']:
                warehouse = self.findNearestWarehouse(order['location'], iType)
                warehouse['typeCounts'][iType] -= 1

                drone = self.findNearestDrone(warehouse)

                if drone is None:
                    for drone in self.drones:
                        while len(drone.commands) > 0:
                            drone.step()

                drone = self.findNearestDrone(warehouse)

                item = {'weight': self.productTypeWeights[iType], 'type':iType}

                drone.addCommand([drone.load, item, warehouse, order])
                drone.addCommand([drone.deliver])

        for drone in self.drones:
            while len(drone.commands) > 0:
                drone.step()

    def findNearestDrone(self, warehouse):
        posDrones = [drone for drone in self.drones if len(drone.commands) == 0]
        if len(posDrones) == 0:
            return None
        posDrones.sort(key=lambda drone: self.distance(drone.location, warehouse['location']))
        return posDrones[0]

    def distance(self, loc1, loc2):
        rd = (loc1['row'] - loc2['row'])*(loc1['row'] - loc2['row'])
        cd = (loc1['col'] - loc2['col'])*(loc1['col'] - loc2['col'])
        return ceil(sqrt(rd+cd))

    def findNearestWarehouse(self, orderLoc, iType):
        posHouses = [warehouse for warehouse in self.warehouses if warehouse['typeCounts'][iType] > 0]
        posHouses.sort(key=lambda warehouse: self.distance(orderLoc, warehouse['location']))
        return posHouses[0]
    
    def writeOutputFile(self, filename):

        self.drones.sort(key=lambda drone: drone.totalTime)
        print 'total time:', self.drones[0].totalTime

        commands = []
        for drone in self.drones:
            for command in drone.commandText:
                commands.append(command)
        
        with open(filename+'output.txt', 'w') as f:
            f.write(str(len(commands)) + '\n')
            for command in commands:
                f.write(command + '\n')
