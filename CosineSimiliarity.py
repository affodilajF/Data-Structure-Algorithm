import math
from collections import defaultdict


## VERSI CLASS ------------------------------------------------
class VectorBreakDown: 

    # constructor method 
    def __init__(self, stringToBeBreakdowned) : 
        self.sSplited = stringToBeBreakdowned.split()
        self.sentenceDict = defaultdict(int)
        self.vectorLength = int 

        # bikin dict, key : string, value : int frekuensi
        for i in self.sSplited : 
            self.sentenceDict[i] += 1

        # panjang vektor
        self.vectorLength = math.sqrt(sum([i**2 for i in self.sentenceDict.values()]))


    def cosine(self, toBeCompared):
        self.vectorDot = 0
        self.aa = toBeCompared

        # ngebandingin 2 vektor, stringnya ada yg sama engga, lalu di dot product
        self.vectorDot = sum([self.sentenceDict[i]*self.aa.sentenceDict[j] for i in self.sentenceDict for j in self.aa.sentenceDict if i==j])

        return self.vectorDot / (self.vectorLength * self.aa.vectorLength)
        

a = VectorBreakDown("Julie loves me more than Linda loves me")
b = VectorBreakDown("Jane likes me more than Julie loves me")

print(f'the cosine similiarity is : {a.cosine(b)}')
print(f'the cosine similiarity is : {b.cosine(a)}')




## ---------------------------------------------------------------------------
## VERSI NORMAL  --------------------------------------------------------------
def cosine (stringA, stringB):
    dictA = defaultdict(int)
    dictB = defaultdict(int)

    for i in stringA.split() :
        dictA[i] += 1;
    for i in stringB.split() :
        dictB[i] += 1; 

    lengthA = math.sqrt(sum([i**2 for i in dictA.values()]))
    lengthB = math.sqrt(sum([i**2 for i in dictB.values()]))

    vectorDot = sum([dictA[i]*dictB[j] for i in dictA for j in dictB if i==j])

    return vectorDot / (lengthA*lengthB)


aA = "Julie loves me more than Linda loves me"
bB = "Jane likes me more than Julie loves me"

print()
print(f'the cosine similiarity is : {cosine(aA,bB)}')

# -----------------------------------------------------------------------------







