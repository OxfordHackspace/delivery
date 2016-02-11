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
        currentDrone = 0;
        for order in self.orders:
            for iType in order['itemTypes']:
                wid = 0
                for warehouse in self.warehouses:
                    if warehouse['typeCounts'][iType] > 0:
                        wid = warehouse['id']
                        warehouse['typeCounts'][iType] -= 1
                        break
                    
                item = {'weight': self.productTypeWeights[iType], 'type':iType}

                d = self.drones[currentDrone]
                
                d.addCommand([d.load, [item], self.warehouses[wid], order])
                d.addCommand([d.deliver])

                currentDrone += 1

                if currentDrone == len(self.drones):
                    for drone in self.drones:
                        drone.step()
                        drone.step()
                    currentDrone = 0

    def writeOutputFile(self, filename):
        commands = []
        for drone in self.drones:
            for command in drone.commandText:
                commands.append(command)
        
        with open(filename+'output.txt', 'w') as f:
            f.write(str(len(commands)) + '\n')
            for command in commands:
                f.write(command + '\n')
