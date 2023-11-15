from collections import defaultdict
from itertools import chain, combinations

def getAprioriAlg(itemSetList, minSup):
    C1List = getItemSetFromList(itemSetList)
    # print(C1List)
    globalFreqItemSet = dict() 
    globalItemSetWithSup = defaultdict(int) ## total counts of each item "count of existance"
    L1ItemSet = getMinSup(C1List,itemSetList,minSup,globalItemSetWithSup)
    # print(globalItemSetWithSup)
    currentLSet = L1ItemSet
    k = 2
    while currentLSet:
        globalFreqItemSet[k-1] = currentLSet ## for k = 1
        candidateSet = getUnion(currentLSet, k) ## create frequest itemsets
        candidateSet = pruning(candidateSet, currentLSet, k-1)
        currentLSet = getMinSup(candidateSet,itemSetList,minSup,globalItemSetWithSup)
        k +1

    print(globalFreqItemSet)
    rules = associationRule(globalFreqItemSet, globalItemSetWithSup, .5)  ## .5 is the min acceptable confidence.
    rules.sort(key=lambda x: x[2]) ## sort by confidence 
    print(rules)
    return globalFreqItemSet, rules
    
def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))

def associationRule(freqItemSet, itemSetWithSup, minConf):
    rules = []
    for k, itemSet in freqItemSet.items():
        for item in itemSet:
            print("---------")
            print(item)
            subsets = powerset(item)
            for s in subsets:
                print(s)
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



def pruning(candidateSet, prevFreqSet, length):
    print("=--------------------" )
    print("start pruning : ",candidateSet )
    tempCandidateSet = candidateSet.copy()
    for item in candidateSet:
        subsets = combinations(item, length)
        for subset in subsets:
            # if the subset is not in previous K-frequent get, then remove the set
            if(frozenset(subset) not in prevFreqSet):
                tempCandidateSet.remove(item)
                break
            
    print("after pruning : ",candidateSet )
    return tempCandidateSet


def getMinSup(itemSet, itemSetList, minSup, globalItemSetWithSup):
    freqItemSet = set()
    localItemSetWithSup = defaultdict(int)

    for item in itemSet:
        for itemSet in itemSetList:
            if item.issubset(itemSet):
                globalItemSetWithSup[item] += 1
                localItemSetWithSup[item] += 1

    for item, supCount in localItemSetWithSup.items():
        support = float(supCount / len(itemSetList))
        if(support >= minSup):
            freqItemSet.add(item)

    return freqItemSet



def getUnion(itemSet, length):
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])
