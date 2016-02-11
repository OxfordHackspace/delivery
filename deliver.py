filelines = ''
with open('busy_day.in') as f:
    filelines = f.readlines()

bits = filelines[0].split(' ')

rows = int(bits[0])
cols = int(bits[1])
dronecount = int(bits[2])
deadline = int(bits[3])
maxload = int(bits[4])

productTypeCount = int(filelines[1])
productTypeWeights = [int(x) for x in filelines[2].split(' ')]

numberOfWarehouses = int(filelines[3])

warehouseLocations = []
warehouseTypeCounts = []

start = 4;

for i in range(0,numberOfWarehouses):
    locChunk = filelines[start + (i*2)].split(' ')
    location = {'row': int(locChunk[0]), 'col':(locChunk[1])}
    warehouseLocations.append(location)
    warehouseTypeCounts.append([int(x) for x in filelines[(start + (i*2))+1].split(' ')])

curPos = start + numberOfWarehouses*2

customerOrderCount = int(filelines[curPos])

curPos += 1

customerOrders = []
    
for i in range(0, customerOrderCount):
    order = {}
    locChunk = filelines[curPos + (i*3)].split(' ')
    order['row'] = int(locChunk[0])
    order['col'] = int(locChunk[1])
    order['itemCount'] = int(filelines[(curPos + (i*3))+1])
    order['itemTypes'] = [int(x) for x in filelines[(curPos + (i*3))+2].split(' ')]
    customerOrders.append(order)

print customerOrders[-1]
