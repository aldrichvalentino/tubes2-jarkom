# get user input for node topology
numberOfNodes = eval(raw_input())
arrayOfNodes = []
for i in range(0, numberOfNodes):
    stringInput = raw_input()
    result = stringInput.split(',')
    neighbourNodes = []
    for j in range(0, len(result)):
        neighbourNodes.append(eval(result[j]) - 1)  # begin with 0
    arrayOfNodes.append(neighbourNodes)

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
    print sourceRoutingTable
    print destinationRoutingTable
    #TODO: update the routing table of destination node
