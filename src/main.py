# get user input for node topology
nodesAndEdge = raw_input()
userInput = nodesAndEdge.split(' ')
numberOfNodes = eval(userInput[0])
numberOfEdge = eval(userInput[1])

listOfRoutingTables = []
distanceAndnextHop = [-1, -1]
for i in range(numberOfNodes):
    routingTable = []
    for j in range(numberOfNodes):
        if(i == j):
            routingTable.append([0,j])
        else:
            routingTable.append(distanceAndnextHop)
    listOfRoutingTables.append(routingTable)
    
for i in range(numberOfEdge):
    edge = raw_input()
    edgeResult = edge.split(' ')
    sourceEdge = eval(edgeResult[0]) - 1
    destinationEdge = eval(edgeResult[1]) - 1
    listOfRoutingTables[sourceEdge][destinationEdge] = [1, destinationEdge]
    # vice versa
    listOfRoutingTables[destinationEdge][sourceEdge] = [1, sourceEdge]

# get the scenarios
numberOfScenarios = eval(raw_input())

# iterate through the scenarios
for i in range(numberOfScenarios):
    scenario = raw_input()
    scenarioResult = scenario.split(' ')
    source = eval(scenarioResult[0]) - 1
    destination = eval(scenarioResult[1]) - 1

    # update the destination routing table with the source routing table
    sourceRoutingTable = listOfRoutingTables[source]
    destinationRoutingTable = listOfRoutingTables[destination]
    # print sourceRoutingTable
    print destinationRoutingTable

    # Update the routing table of destination node
    for j in range(len(destinationRoutingTable)):
        if(destinationRoutingTable[j][0] == -1):  # information unknown
            print 'harus diupdate nih'
            # check if the source routing table has the info about the unknown node
            if(sourceRoutingTable[j][0] != -1):
                # info is known, then the next hop is assigned to the source node
                # the distance is updated
                destinationRoutingTable[j] = [1 + sourceRoutingTable[j][0], source]
        elif(destinationRoutingTable[j][0] > sourceRoutingTable[j][0] and  # distance is shorter
            sourceRoutingTable[j][0] != -1 and  # the source has the information about the shorter path
            destinationRoutingTable[j][1] != source):  # the destination routing table is different from the source path
            # if the distance of the source routing table is shorter, then update
            destinationRoutingTable[j] = [1 + sourceRoutingTable[j][0], source]
    
    print 'udah diupdate'
    print destinationRoutingTable
    # dump the routing table back into the list
    listOfRoutingTables[destination] = destinationRoutingTable

# print ' '
for i in range(0, len(listOfRoutingTables)):
    for j in range(0, len(listOfRoutingTables[i])):
        # output format: distance _ next hop node
        distance = listOfRoutingTables[i][j][0]
        nextHop = listOfRoutingTables[i][j][1]
        if(nextHop != -1):
            nextHop += 1
        print str(distance) + ' ' + str(nextHop)
