import unittest
import utils
from collections import defaultdict
from mlxtend.frequent_patterns import apriori, association_rules 

class TestingUtils(unittest.TestCase):
    def test_getUnions(self):
        itemSets = [frozenset({1, 2}), frozenset({2, 3}), frozenset({3, 4})]
        length = 3
        output = utils.getUnion(itemSets,length)
        expected_result = {frozenset({1, 2, 3}), frozenset({2, 3, 4})}
        self.assertEqual(output, expected_result)

    def test_getItemSetFromList(self):
        itemSets = [{1,2},{3,2},{1,5},{5,6}]
        output = utils.getItemSetFromList(itemSets)
        expected_result = {frozenset({1}), frozenset({2}),frozenset({3}),frozenset({5}),frozenset({6})}
        self.assertEqual(output, expected_result) 

    def test_getMinSup(self):
        itemList = [{1,2},{3,2},{1,5},{5,6}]
        itemSets = {frozenset({1}), frozenset({2}),frozenset({3}),frozenset({5}),frozenset({6})}
        globalItemSetWithSup = defaultdict(int)
        output = utils.getMinSup(itemSets,itemList,.4,globalItemSetWithSup)
        expected_result = {frozenset({5}), frozenset({2}), frozenset({1})}
        self.assertEqual(output, expected_result) 
        self.assertEqual(globalItemSetWithSup.get(frozenset({2})), 2) 
        self.assertEqual(globalItemSetWithSup.get(frozenset({3})), 1) 

    def test_getPossibleSets(self):
        input_set = {1, 2, 3}
        expected_result= {(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)}
        output = utils.getPossibleSets(input_set)
        self.assertEqual(set(output), expected_result)

    def test_pruning(self):
        candidateSet_1 = {frozenset({1, 2, 3}), frozenset({2, 3, 4}), frozenset({3, 4, 5})}
        prevFreqSet_1 = {frozenset({1, 2}), frozenset({2, 3}),frozenset({2, 4}) ,frozenset({3, 4})}
        length_1 = 2
        expected_result_1 = {frozenset({2, 3, 4})}
        output = utils.pruning(candidateSet_1, prevFreqSet_1, length_1)
        self.assertEqual(output, expected_result_1)

    def test_AprioriAlg(self):
        itemSetList = [['eggs', 'bacon', 'soup'],
                ['eggs', 'bacon', 'apple'],
                ['soup', 'bacon', 'banana']]
        
        outFreItemSet , outRules = utils.getAprioriAlg(itemSetList,.5)
        print(outRules)
        expected_role = [[{'soup'}, {'bacon'}, 1.0], [{'eggs'}, {'bacon'}, 1.0]]
        expected_freq = {1: set({frozenset({'soup'}), frozenset({'bacon'}), frozenset({'eggs'})}), 2: set({frozenset({'soup', 'bacon'}), frozenset({'bacon', 'eggs'})})}
        self.assertEqual(sorted(outRules),sorted(expected_role))
        self.assertEqual(outFreItemSet, expected_freq)

if __name__ == '__main__':
    unittest.main()