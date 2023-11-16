from collections import defaultdict
from itertools import chain, combinations

def getUnion(itemSet, length):
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])

def getAprioriAlg(itemSetList, minSup):
    C1List = getItemSetFromList(itemSetList) ## frequest 1 itemlist
    # print(C1List)
    globalFreqItemSet = dict() 
    globalItemSetWithSup = defaultdict(int) ## total counts of each item "count of existance"
    L1ItemSet = getMinSup(C1List,itemSetList,minSup,globalItemSetWithSup) ## return first level of freq item set
    # print(globalItemSetWithSup)
    currentLSet = L1ItemSet
    k = 2
    while currentLSet:
        globalFreqItemSet[k-1] = currentLSet ## for k = 1 "size of set is 1"
        candidateSet = getUnion(currentLSet, k) ## create  itemsets for size k  from the current list
        currentLSet = getMinSup(candidateSet,itemSetList,minSup,globalItemSetWithSup) ## return only sets above min support
        k = k +1

    rules = associationRule(globalFreqItemSet, globalItemSetWithSup, .7)  ## .3 is the min acceptable confidence.
    rules.sort(key=lambda x: x[2]) ## sort by confidence 
    print(rules)
    return globalFreqItemSet, rules
    
def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s))) ## generate all possible combinations ex[1,2,3] output [1,2,3,{1,2},{2,3},{1,3}]

def associationRule(freqItemSet, itemSetWithSup, minConf):
    rules = []
    for k, itemSet in freqItemSet.items():
        for item in itemSet:
            # print("---------")
            # print(item)
            subsets = powerset(item)
            for s in subsets:
                confidence = float(
                    itemSetWithSup[item] / itemSetWithSup[frozenset(s)])
                if(confidence > minConf):
                    rules.append([set(s), set(item.difference(s)), confidence])
    return rules

def getItemSetFromList(itemSetList):
    tempItemSet = set()
    for itemSet in itemSetList:
        for item in itemSet:
            tempItemSet.add(frozenset([item]))

    return tempItemSet





def getMinSup(itemSet, itemSetList, minSup, globalItemSetWithSup):
    freqItemSet = set()
    localItemSetWithSup = defaultdict(int)

    ## count the occurance of a set in all itemsets // we put it in global store to be able to use it  for confidence calc at the end.
    for item in itemSet:
        for itemSet in itemSetList:
            if item.issubset(itemSet):
                globalItemSetWithSup[item] += 1
                localItemSetWithSup[item] += 1


    ## calc the support for each item and add it to fequest item list.
    for item, supCount in localItemSetWithSup.items():
        support = float(supCount / len(itemSetList))
        if(support >= minSup):
            freqItemSet.add(item)

    return freqItemSet


