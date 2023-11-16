import unittest
import utils
from collections import defaultdict
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

    def test_powerset(self):
        input_set = {1, 2, 3}
        expected_result= set({(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)})
        output = utils.powerset(input_set)
        print(set(output))
        self.assertEqual(output, expected_result)


if __name__ == '__main__':
    unittest.main()