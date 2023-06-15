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

dataWeight = list(set((weight for edges in graph.values() for weight in edges.values())))


dataHasilA = []
for m in range(len(dataWeight)):
	for x,y in graph.items():
            for a,u in y.items():
        	    if u == dataWeight[m]:
                        temp = [x,a,u]
                        if [temp[1], temp[0], temp[2]] not in dataHasilA: 
                            dataHasilA.append(temp)

# # Logic buat nentuin whether data nya ngebikin siklik or nah + algoritma kruskal
ac = set()
for i in range(len(dataHasilA)):
    if dataHasilA[i][1] in ac and dataHasilA[i][0] in ac: 
        pass
    else :
        print(dataHasilA[i])
        ac.add(dataHasilA[i][0])
        ac.add(dataHasilA[i][1])
        print("")