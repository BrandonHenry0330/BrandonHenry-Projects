import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    "Unittest setup file. Unitetst framework will run this before every test."
    def setUp(self):
        self.my_cats_log =  {(2,2019):{"Oceanfish":7, "Tuna":1, "Whitefish":3, "Chicken":4, "Beef":2},
            (5,2019):{"Oceanfish":6, "Tuna":2, "Whitefish":1, "Salmon":3, "Chicken":6},
            (9,2019):{"Tuna":3, "Whitefish":3, "Salmon":2, "Chicken":5, "Beef":2, "Turkey":1, "Sardines":1},
            (5,2020):{"Whitefish":5, "Sardines":3, "Chicken":7, "Beef":3},
            (8,2020):{"Oceanfish":3, "Tuna":2, "Whitefish":2, "Salmon":2, "Chicken":4, "Beef":2, "Turkey":1},
            (10,2020):{"Tuna":2, "Whitefish":2, "Salmon":2, "Chicken":4, "Beef":2, "Turkey":4, "Sardines":1},
            (12,2020):{"Chicken":7,"Beef":3, "Turkey":4, "Whitefish":1, "Sardines":2},
            (4,2021):{"Salmon":2,"Whitefish":4, "Turkey":2, "Beef":4, "Tuna":3, "MixedGrill": 2}, 
            (5,2021):{"Tuna":5,"Beef":4, "Scallop":4, "Chicken":3}, 
            (6,2021):{"Turkey":2,"Salmon":2, "Scallop":5, "Oceanfish":5, "Sardines":3}, 
            (9,2021):{"Chicken":8,"Beef":6},                 
            (10,2021):{ "Sardines":1, "Tuna":2, "Whitefish":2, "Salmon":2, "Chicken":4, "Beef":2, "Turkey":4}
        } 
        self.graph = {'A':{'B','C','D'},'B':{'C'},'C':{'B','E','F','G'},'D':{'A','E','F'},'E':{'F'}, 'F':{'E', 'G'},'G':{}, 'H':{'F','G'}}
        self.test_log = {(6,2019):{"Item":3, "Thing":4},
                        (9,2019):{"Test":5,"Item":2},
                        (3,2020):{"Thing":7,"Test":2},
                        (10,2020):{"Test":5,"Thing":2},
                        (7,2021):{"That":1,"Thing":3,"Item":2},
                        (12,2021):{"Thing":8}}
        self.graph2 = {'A':{'B','C'},'B':{'C','F'}, 'C':{'A','D','E'}, 'D':{'H'},'E':{'B','F'},'F':{'B','C'}, 'H':{}}

    #--- Problem 1(a)----------------------------------
    def test_1_merge_by_year(self):
        output = {2019: {'Oceanfish': 13, 'Tuna': 6, 'Whitefish': 7, 'Chicken': 15, 'Beef': 4, 'Salmon': 5, 'Turkey': 1, 'Sardines': 1}, 
                  2020: {'Whitefish': 10, 'Sardines': 6, 'Chicken': 22, 'Beef': 10, 'Oceanfish': 3, 'Tuna': 4, 'Salmon': 4, 'Turkey': 9}, 
                  2021: {'Salmon': 6, 'Whitefish': 6, 'Turkey': 8, 'Beef': 16, 'Tuna': 10, 'MixedGrill': 2, 'Scallop': 9, 'Chicken': 15, 'Oceanfish': 5, 'Sardines': 4}}
        self.assertDictEqual(merge_by_year(self.my_cats_log),output)

    def test_2_merge_by_year(self):
        output = {2019:{"Item":5,"Thing":4,"Test":5},
                  2020:{"Thing":9,"Test":7},
                  2021:{"That":1,"Thing":11,"Item":2}
        }
        self.assertDictEqual(merge_by_year(self.test_log),output)
        # Provide your own test here. Create your own input dictionary for this test (similar to self.my_cats_log).
    
    #--- Problem 1(b)----------------------------------
    def test_1_merge_year(self): 
        output1 = {'Oceanfish': 13, 'Tuna': 6, 'Whitefish': 7, 'Chicken': 15, 'Beef': 4, 'Salmon': 5, 'Turkey': 1, 'Sardines': 1}
        self.assertDictEqual(merge_year(self.my_cats_log,2019),output1 )
        output2 = {'Salmon': 6, 'Whitefish': 6, 'Turkey': 8, 'Beef': 16, 'Tuna': 10, 'MixedGrill': 2, 'Scallop': 9, 'Chicken': 15, 'Oceanfish': 5, 'Sardines': 4}
        self.assertDictEqual(merge_year(self.my_cats_log,2021),output2 )

    def test_2_merge_year(self):
        output1 = {"Thing":9,"Test":7}
        self.assertDictEqual(merge_year(self.test_log,2020),output1 )
        output2 = {"That":1,"Thing":11,"Item":2}
        self.assertDictEqual(merge_year(self.test_log,2021),output2 )
        # Provide your own test here. Create your own input dictionary for this test (similar to self.my_cats_log). 
        # You can re-use the data dictionary you created for merge_by_year test.

    #--- Problem 1(c)----------------------------------
    def test_1_getmax_of_flavor(self):
        output1 = ((5, 2021), 5)
        self.assertTupleEqual(getmax_of_flavor(self.my_cats_log,"Tuna"),output1 )
        output2 = ((9, 2021), 6)
        self.assertTupleEqual(getmax_of_flavor(self.my_cats_log,"Beef"),output2 )

    def test_2_getmax_of_flavor(self):
        output1 = ((6, 2019), 3)
        self.assertTupleEqual(getmax_of_flavor(self.test_log,"Item"),output1 ) 
        output2 = ((12, 2021), 8)
        self.assertTupleEqual(getmax_of_flavor(self.test_log,"Thing"),output2 )
        # Provide your own test here. Create your own input dictionary for this test (similar to self.my_cats_log). 
        # You can re-use the data dictionary you created for merge_by_year test.

    #--- Problem 2(a)----------------------------------
    def test_1_follow_the_follower(self):
        output = [('A', 'D'), ('B', 'C'), ('C', 'B'), ('D', 'A'), ('E', 'F'), ('F', 'E')]
        self.assertListEqual(follow_the_follower(self.graph),output )

    def test_2_follow_the_follower(self):
        output =[('A', 'C'), ('B', 'F'), ('C', 'A'), ('F', 'B')]
        self.assertListEqual(follow_the_follower(self.graph2),output )
        # Provide your own test here. Create your own graph dictionary for this test (similar to self.graph). 
    
    #--- Problem 2(b)----------------------------------
    def test_1_follow_the_follower2(self):
        output = [('A', 'D'), ('B', 'C'), ('C', 'B'), ('D', 'A'), ('E', 'F'), ('F', 'E')]
        self.assertListEqual(follow_the_follower2(self.graph),output )

    def test_2_follow_the_follower2(self):
        output =[('A', 'C'), ('B', 'F'), ('C', 'A'), ('F', 'B')]
        self.assertListEqual(follow_the_follower2(self.graph2),output )
        # Provide your own test here. Create your own graph dictionary for this test (similar to self.graph). 
        # You can re-use the data dictionary you created for follow_the_follower test.

    #--- Problem 3----------------------------------
    def test_1_connected(self):
        self.assertTrue(connected(graph, 'A' ,'F'))
        self.assertFalse(connected(graph, 'E' ,'A'))
        self.assertFalse(connected(graph, 'A' ,'H'))
        self.assertTrue(connected(graph, 'H' ,'E'))

    def test_2_connected(self):
        self.assertTrue(connected(graph2, 'A' ,'C'))
        self.assertFalse(connected(graph2, 'D' ,'B'))
        self.assertFalse(connected(graph2, 'D' ,'A'))
        self.assertTrue(connected(graph2, 'B' ,'F'))
        # Provide your own test here. Create your own graph dictionary for this test (similar to self.graph). 
        # You can re-use the data dictionary you created for follow_the_follower test.

    #--- Problem 4(a)----------------------------------
    def test1_lazy_word_reader(self):
        # lazy_word_reader output
        self.filetokens = ["CptS","355","Assignment","3","-","Python","Warmup","This","is","a","text","test","file","for","CptS","355","-","Assignment","3","-","Python",
                         "Warmup","With","some","repeated","text","for","CptS","355","-","Assignment","3","-","Python","Warmup",".","dot"]
        mywords = lazy_word_reader("testfile.txt")
        mywords.__next__()   # returns CptS
        mywords.__next__()   # returns 355
        mywords.__next__()   # returns Assignment

        rest_of_file = []
        for word in mywords:  
            rest_of_file.append(word)
        self.assertListEqual(rest_of_file,self.filetokens[3:])
    def test2_lazy_word_reader(self):
        self.filetokens = ["this","is","my","test","file","testing","test"]
        mywords = lazy_word_reader("testfile2.txt")
        mywords.__next__()   
        mywords.__next__()   
        mywords.__next__()   

        rest_of_file = []
        for word in mywords:
            rest_of_file.append(word)
        self.assertListEqual(rest_of_file,self.filetokens[3:])
    #--- Problem 4(b)----------------------------------
    def test_word_histogram(self):
        # histogram output
         self.histogram = [('-', 5), ('3', 3), ('355', 3), ('Assignment', 3), ('CptS', 3), ('Python', 3), ('Warmup', 3), ('for', 2), ('text', 2), ('.', 1), ('This', 1), ('With', 1), ('a', 1), ('dot', 1), ('file', 1), ('is', 1), ('repeated', 1), ('some', 1), ('test', 1)]
         self.assertListEqual(word_histogram(lazy_word_reader("testfile.txt")),self.histogram)
    def test_word_histogram2(self):
        self.histogram = [('test', 2), ('file', 1), ('is', 1), ('my', 1), ('testing', 1), ('this', 1)]
        self.assertListEqual(word_histogram(lazy_word_reader("testfile2.txt")),self.histogram)
if __name__ == '__main__':
    unittest.main()

