from drone import Drone

class DeliveryManager:
    def __init__(self, droneCount, capacity, warehouses, orders):
        self.drones = []
        for i in range(0, droneCount):
            d = Drone(i, capacity, warehouses[0].location)
            self.drones.append(d)
        self.warehouses = warehouses
        self.orders = orders

    def go(self):
        pass
