# CptS 355 - Fall 2021 - Assignment 3
# Brandon Henry
from collections import defaultdict
debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

my_cats_log =  {(2,2019):{"Oceanfish":7, "Tuna":1, "Whitefish":3, "Chicken":4, "Beef":2},
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
                (10,2021):{ "Sardines":1, "Tuna":2, "Whitefish":2, "Salmon":2, "Chicken":4, "Beef":2, "Turkey":4} }

p1a_output = {2019: {'Oceanfish': 13, 'Tuna': 6, 'Whitefish': 7, 'Chicken': 15, 'Beef': 4, 'Salmon': 5, 'Turkey': 1, 'Sardines': 1}, 
              2020: {'Whitefish': 10, 'Sardines': 6, 'Chicken': 22, 'Beef': 10, 'Oceanfish': 3, 'Tuna': 4, 'Salmon': 4, 'Turkey': 9}, 
              2021: {'Salmon': 6, 'Whitefish': 6, 'Turkey': 8, 'Beef': 16, 'Tuna': 10, 'MixedGrill': 2, 'Scallop': 9, 'Chicken': 15, 'Oceanfish': 5, 'Sardines': 4}}
graph2 = {'A':{'B','C'},'B':{'C','F'}, 'C':{'A','D','E'}, 'D':{'H'},'E':{'B','F'},'F':{'B','C'}, 'H':{}}


## problem 1(a) merge_by_year - 10% (complete)
test_log = {(6,2019):{"Item":3, "Thing":4},
                        (9,2019):{"Test":5,"Item":2},
                        (3,2020):{"Thing":7,"Test":2},
                        (10,2020):{"Test":5,"Thing":2},
                        (7,2021):{"That":1,"Thing":3,"Item":2},
                        (12,2021):{"Thing":8}
        }
def merge_by_year(data):
     output = defaultdict(lambda: defaultdict(lambda: 0))
     for (month,year),log in data.items():
         for flavor,num in log.items():
             output[year][flavor] += num          
                    
     
     return {key:dict(value) for key,value in output.items()}
print(merge_by_year(test_log))



from functools import reduce

## problem 1(b) merge_year - 15%(complete)
def merge_year(data,year):
    output = dict(filter(lambda x: x[0][1] == year, data.items()))
    def combine_dicts_high(d1,d2):
        common_items = map(lambda x: (x[0],x[1]+ d2.get(x[0],0)),d1.items())
        other_items = filter(lambda t: not (t[0] in d1.keys()) , d2.items())
        return dict(list(common_items) + list(other_items))
    return reduce(combine_dicts_high,output.values())
#print(merge_year(my_cats_log,2019))
## problem 1(c) getmax_of_flavor - 15% (complete)
def getmax_of_flavor(data,flavor):
    key,value = max(data.items(), key = lambda x: x[1].get(flavor,0))
    return ((key),value[flavor])
#print(getmax_of_flavor(my_cats_log,'Beef'))
graph = {'A':{'B','C','D'},'B':{'C'},'C':{'B','E','F','G'},'D':{'A','E','F'},'E':{'F'}, 'F':{'E', 'G'},'G':{}, 'H':{'F','G'}}

## problem 2(a) follow_the_follower - 10% (complete)
def follow_the_follower(graph):
        output = []
        for key,partners in graph.items():
            for partner in partners:
                if key in graph[partner]:
                    output.append((key,partner))
        return output        
#print(follow_the_follower(graph_test))
## problem 2(b) follow_the_follower2 - 6% (complete)

def follow_the_follower2(graph):
    return [
        (key,partner)
        for key,partners in graph.items()
        for partner in partners
        if key in graph[partner] 
    ]
#print(follow_the_follower2(graph))
## problem 3 - connected - 15% (complete)

def connected(graph,start,finish):
    def inner(graph,start,finish,seen):
        if(start == finish):
           return True
        seen.add(start)
        
        for node in graph[start]:
            if(node in seen):
                continue
            if inner(graph,node,finish,seen):
                return True
        return False
    return inner(graph,start,finish,set())     
     
## problem 4(a) - lazy_word_reader - 20%
class lazy_word_reader:
    def __init__(self,file_name):
        self.file = open(file_name, 'r')
        self.pending = []
    def __next__(self):
        while not self.pending:
            line = self.file.readline()
            if line:
                self.pending = line.split()
            else:
                raise StopIteration                    
        return self.pending.pop(0)
        #return self.file.readline().split()
    def __iter__(self):
        return self 
mywords = lazy_word_reader("testfile2.txt")
print(mywords.__next__()) # returns CptS
print(mywords.__next__()) # returns 355
print(mywords.__next__()) # returns Assignment


## problem 4(b) - word_histogram - 3% (complete)
from collections import Counter
def word_histogram(it):
    output = sorted(Counter(it).most_common(),key = lambda x: (-x[1],x[0]))
    return output 

print(word_histogram(lazy_word_reader('testfile2.txt')))
