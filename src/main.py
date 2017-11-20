# get user input for node topology
numberOfNodes = eval(raw_input())
arrayOfNodes = []
for i in range(0, numberOfNodes):
    arrayOfNodes.append(raw_input())

# get user input for scenario
numberOfScenarios = eval(raw_input())
arrayOfScenarios = []
for i in range(0, numberOfScenarios):
    stringInput = raw_input()
    result = stringInput.split(' ')
    source = int(result[0])
    destination = int(result[1])
    arrayOfScenarios.append([source, destination])

print arrayOfNodes
print arrayOfScenarios
