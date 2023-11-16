import unittest
import utils
from collections import defaultdict
class TestingUtils(unittest.TestCase):
    def test_getUnions(self):
        itemSets = [frozenset({1, 2}), frozenset({2, 3}), frozenset({3, 4})]
        length = 3
        output = utils.getUnion(itemSets,length)
        print(output)
        expected_result = {frozenset({1, 2, 3}), frozenset({2, 3, 4})}
        self.assertEqual(output, expected_result)

    def test_getItemSetFromList(self):
        itemSets = [{1,2},{3,2},{1,5},{5,6}]
        output = utils.getItemSetFromList(itemSets)
        print(output)
        expected_result = {frozenset({1}), frozenset({2}),frozenset({3}),frozenset({5}),frozenset({6})}
        self.assertEqual(output, expected_result) 

    def test_getMinSup(self):
        itemSets = {frozenset({1}), frozenset({2}),frozenset({3}),frozenset({5}),frozenset({6})}
        globalItemSetWithSup = defaultdict(int)
        output = utils.getItemSetFromList(itemSets)
        print(output)
        expected_result = {frozenset({1}), frozenset({2}),frozenset({3}),frozenset({5}),frozenset({6})}
        self.assertEqual(output, expected_result) 

if __name__ == '__main__':
    unittest.main()