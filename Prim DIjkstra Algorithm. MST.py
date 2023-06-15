graph = {
    'A' : {'B':11, 'C':15, 'D':9},
    'B' : {'A':11, 'C':8},
    'C' : {'A':15, 'B':8, 'D':7, 'E':14, 'H': 17, 'F' : 10},
    'D' : {'A':9, 'C': 7, 'E' : 5, 'G' : 16}, 
    'E' : {'C':14, 'D':5, 'H':4},
    'F' : {'C':10, 'H':6}, 
    'G' : {'D':16, 'H':12},
    'H' : {'C':17, 'E':4, 'F':6, 'G':12 }
}

# randomly choosen starter node
n = 'A'
dataWeight = list(set(n))

# jumlah node
a = len(set(graph.keys()))

# # prim dijkstra mst
for i in range(a):
    wSmallest = 10000000
    tempList = []
    for j in range(len(dataWeight)):
        tempDict = graph.get(dataWeight[j])
        for key,values in tempDict.items():
            if key not in dataWeight:
                if values < wSmallest:
                    tempList = [dataWeight[j],key,values]
                    wSmallest = values
    if len(tempList) != 0:
        print(tempList)
        dataWeight.append(tempList[1])
    print("")



