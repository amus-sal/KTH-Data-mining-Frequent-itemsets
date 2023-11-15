import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import utils
if __name__ == "__main__":
    dataset = [['Milk','Onion', 'Bread', 'Eggs','Yoghurt'],
           ['Fish','Onion','Bread','Eggs','Yoghurt'],
           ['Milk', 'Apples',  'Eggs'],
           ['Milk', 'Sugar', 'Tea',  'Yoghurt'],
           ['Tea','Onion', 'Ice cream', 'Eggs'],]
    utils.getAprioriAlg(dataset,.3)
     
