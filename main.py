
import utils
if __name__ == "__main__":
    dataset = [['Milk','Onion', 'Bread', 'Kidney Beans','Eggs','Yoghurt'],
           ['Fish','Onion','Bread','Eggs','Yoghurt'],
           ['Milk', 'Apples', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Sugar', 'Tea Leaves', 'Kidney Beans', 'Yoghurt'],
           ['Tea Leaves','Onion','Kidney Beans', 'Ice cream', 'Eggs'],]
    utils.getAprioriAlg(dataset,.3)
     
