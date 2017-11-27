# get user input for node topology
nodesAndEdge = raw_input()
userInput = nodesAndEdge.split(' ')
numberOfNodes = eval(userInput[0])
numberOfEdge = eval(userInput[1])

# initiate array of nodes
arrayOfNodes = []
for i in range(0, numberOfNodes):
    arrayOfNodes.append([])

# fill the edge
for i in range(0, numberOfEdge):
    stringInput = raw_input()
    result = stringInput.split(' ')
    sourceEdge = eval(result[0]) - 1 
    destinationEdge = eval(result[1]) - 1
    neighbourNodes = arrayOfNodes[sourceEdge]
    # insert the new neighbour
    neighbourNodes.append(destinationEdge)
    arrayOfNodes[sourceEdge] = neighbourNodes
    # vice versa
    neighbourNodes = arrayOfNodes[destinationEdge]
    neighbourNodes.append(sourceEdge)
    arrayOfNodes[destinationEdge] = neighbourNodes

# get user input for scenario
numberOfScenarios = eval(raw_input())
arrayOfScenarios = []
for i in range(0, numberOfScenarios):
    stringInput = raw_input()
    result = stringInput.split(' ')
    source = int(result[0]) - 1  # begin with zero
    destination = int(result[1]) - 1  # begin with zero
    arrayOfScenarios.append([source, destination])

# print arrayOfNodes
# print arrayOfScenarios

# initiate the routing table
listOfRoutingTables = []
for i in range(0, numberOfNodes):
    # get the neighbour node list
    neighbourNodes = arrayOfNodes[i]
    
    # make a routing table, initiate everything with -1
    routingTable = []  # contains [distance, next hop]
    for j in range(0, numberOfNodes):
        if(j == i):  # routing to itself
            routingTable.append([0, j])
        else:
            routingTable.append([-1, -1])
    
    # fill the routing table with known neighbours
    for j in range(0, len(neighbourNodes)):
        routingTable[neighbourNodes[j]] = [1, neighbourNodes[j]]
    
    # insert into the list of routing table
    listOfRoutingTables.append(routingTable)

# for i in range(0, len(listOfRoutingTables)):
#     print listOfRoutingTables[i]

# iterate through the scenarios
for i in range(0, len(arrayOfScenarios)):
    source = arrayOfScenarios[i][0]
    destination = arrayOfScenarios[i][1]
    
    # update the destination routing table with the source routing table
    sourceRoutingTable = listOfRoutingTables[source]
    destinationRoutingTable = listOfRoutingTables[destination]
    # print sourceRoutingTable
    # print destinationRoutingTable

    # Update the routing table of destination node
    for j in range(0, len(destinationRoutingTable)):
        if(destinationRoutingTable[j][0] == -1):  # information unknown
            # print 'harus diupdate nih'
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
    
    # print 'udah diupdate'
    # print destinationRoutingTable
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
