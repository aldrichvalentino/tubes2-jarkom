#include <iostream>
#include <utility>
#include <stdio.h>

using namespace std;

int main() {
    int numberOfNodes, numberOfEdges;
    cin >> numberOfNodes >> numberOfEdges;

    pair<int, int> listOfRoutingTables[numberOfNodes][numberOfNodes];
    for(int i = 0; i < numberOfNodes; i++){
        for(int j = 0; j < numberOfNodes; j++){
            if(i == j){
                listOfRoutingTables[i][j] = make_pair(0, i);
            } else {
                listOfRoutingTables[i][j] = make_pair(-1, -1);
            }
        }
    }

    for (int i = 0;i < numberOfEdges; i++) {
        int source, destination;
        cin >> source >> destination;
        source -= 1;
        destination -= 1;
        listOfRoutingTables[source][destination].first = 1;
        listOfRoutingTables[source][destination].second = destination;
        // vice versa
        listOfRoutingTables[destination][source].first = 1;
        listOfRoutingTables[destination][source].second = source;
        // cout << listOfRoutingTables[source][destination].first << listOfRoutingTables[source][destination].second << endl;
    }

    int numberOfScenarios;
    cin >> numberOfScenarios;

    for(int i = 0; i < numberOfScenarios; i++){
        int source, dest;
        cin >> source >> dest;
        source -= 1;
        dest -= 1;
        for(int j = 0; j < numberOfNodes; j++){
            if(listOfRoutingTables[dest][j].first == -1 && listOfRoutingTables[source][j].first != -1){
                listOfRoutingTables[dest][j].first = 1 + listOfRoutingTables[source][j].first;
                listOfRoutingTables[dest][j].second = source;
            } else if(listOfRoutingTables[dest][j].first > (listOfRoutingTables[source][j].first + 1) &&
                        listOfRoutingTables[source][j].first != -1 &&
                        listOfRoutingTables[dest][j].second != source){
                listOfRoutingTables[dest][j].first = 1 + listOfRoutingTables[source][j].first;
                listOfRoutingTables[dest][j].second = source;
            } else if(listOfRoutingTables[dest][j].first == (listOfRoutingTables[source][j].first + 1) &&
                        listOfRoutingTables[dest][j].first != -1 &&
                        listOfRoutingTables[dest][j].second > source){
                listOfRoutingTables[dest][j].first = 1 + listOfRoutingTables[source][j].first;
                listOfRoutingTables[dest][j].second = source;
            }
        }
    }

    for(int i = 0; i < numberOfNodes; i++){
        for(int j = 0; j < numberOfNodes; j++){
            if(listOfRoutingTables[i][j].second != -1){
                listOfRoutingTables[i][j].second += 1;
            }
            printf("%d %d\n", listOfRoutingTables[i][j].first, listOfRoutingTables[i][j].second);
        }
    }

    return 0;
}