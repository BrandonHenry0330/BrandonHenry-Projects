{- Example of using the HUnit unit test framework.  See  http://hackage.haskell.org/package/HUnit for additional documentation.
To run the tests type "run" at the Haskell prompt.  -} 

module HW1SampleTests
    where

import Test.HUnit
import Data.Char
import Data.List (sort)
import HW1

-- Helper functions 
-- Function to sort second elements in each tuple
sortSnds xs = map (\(x,y) -> (x,sort y)) xs

p1_test1 = TestCase (assertEqual "everyOther-test1" 
                                 "ABCDEFGH" 
                                 (everyOther "AaBbCcDdEeFfGgH") )
p1_test2 = TestCase (assertEqual "everyOther-test2" 
                                 [1,3,5,7,9] 
                                 (everyOther [1,2,3,4,5,6,7,8,9,10]) ) 
p1_test3 = TestCase (assertEqual "everyOther-test3" 
                                 ["yes","oui","ja","evet","ye","shi","ie","nai"]  
                                 (everyOther ["yes","no","oui","non","ja","nein","evet","hayir","ye","ani","shi", "hai","ie","meiyou","nai","ochi" ]) ) 
p1_test4 = TestCase (assertEqual "everyOther-test4" 
                                 "A"  
                                 (everyOther ['A']) ) 
p1_test5 = TestCase (assertEqual "everyOther-test5" 
                                  [2,6,10]
                                  (everyOther [2,4,6,8,10]))
p1_test6 = TestCase (assertEqual "everyOther-test6"
                                  [1]
                                  (everyOther [1]))
p2a_test1 = TestCase (assertEqual "eliminateDuplicates-test1" 
                                  (sort [1,2,3,4,5,6,7])  
                                  (sort $ eliminateDuplicates [6,5,1,6,4,2,2,3,7,2,1,1,2,3,4,5,6,7]) ) 
p2a_test2 = TestCase (assertEqual "eliminateDuplicates-test2" 
                                  (sort "-CptS 321")  
                                  (sort $ eliminateDuplicates "CptS322 - CptS322 - CptS 321") ) 
p2a_test3 = TestCase (assertEqual "eliminateDuplicates-test3" 
                                  (sort [[1,2],[3],[1],[]])  
                                  (sort $ eliminateDuplicates [[1,2],[1],[],[3],[1],[]]) ) 
p2a_test4 = TestCase (assertEqual "eliminateDuplicates-test4" 
                                  (sort ["Let","snow","rain","let","it","hail"])  
                                  (sort $ eliminateDuplicates ["Let","it","snow", "let","it", "rain", "let", "it","hail"]) ) 
p2a_test5 = TestCase (assertEqual "eliminateDuplicates-test5 "
                                          (sort[" "])
                                          (sort $ eliminateDuplicates [" "]))
p2a_test6 = TestCase (assertEqual "eliminateDuplicates-test5 "
                                          (sort[1])
                                          (sort $ eliminateDuplicates [1]))


p2b_test1 = TestCase (assertEqual "matchingSeconds-test1" 
                                  (sort [5,3]) 
                                  (sort $ matchingSeconds "cat" [("cat",5),("dog",9),("parrot",3),("cat",3),("fish",1)]) ) 
p2b_test2 = TestCase (assertEqual "matchingSeconds-test2" 
                                   []  
                                   (matchingSeconds "hamster" [("cat",5),("dog",9),("parrot",3),("cat",3),("fish",1)]) ) 
p2b_test3 = TestCase (assertEqual "matchingSeconds-test3" 
                                   (sort [355,302,322]) 
                                   (sort $ matchingSeconds "CptS" [("EE",214),("CptS",355),("CptS",302), ("CptS",322)]) ) 
p2b_test4 = TestCase (assertEqual "matchingSeconds-test4" 
                                    (sort [30,50] )
                                    (sort $ matchingSeconds "cat" [("cat", 30),("dog", 20),("cat",50)] ))
p2b_test5 = TestCase (assertEqual "matchingSeconds-test5"
                                    (sort ["correct","answer"])
                                    (sort $ matchingSeconds "right" [("right","correct"),("wrong","incorrect"),("right","answer")]))
p2c_test1 = TestCase (assertEqual "clusterCommon-test1" 
                                   (sort $ sortSnds [("parrot",[3]),("dog",[10,5,7]),("cat",[5,3]),("fish",[1])])  
                                   (sort $ sortSnds $ clusterCommon [("cat",5),("dog",10),("parrot",3),("dog",5),("dog",7),("cat",3), ("fish",1)]) ) 
p2c_test2 = TestCase (assertEqual "clusterCommon-test2" 
                                   (sort $ sortSnds [(2,[20]),(1,[10,1]),(4,[400,40]),(3,[3,30,300])])  
                                   (sort $ sortSnds $ clusterCommon [(1,10),(4,400),(3,3),(2,20),(3,30),(1,1),(4,40),(3,300)]) ) 
p2c_test3 = TestCase (assertEqual "clusterCommon-test3" 
                                   ([]::[(Int,[Int])]) 
                                   (clusterCommon []) ) 

p2c_test4 = TestCase (assertEqual "clusterCommon-test4" 
                                    (sort $ sortSnds [(2,[20]),(3,[300,30,3]),(4,[40,400]),(1,[1,10])])
                                    (sort $ sortSnds $ clusterCommon [(3,300),(4,40),(1,1),(3,30),(2,20),(3,3),(4,400),(1,10)])            )

p2c_test5 = TestCase (assertEqual "clusterCommon-test5" 
                                    (sort $  [(2,["dog"]),(1,["cat","cat"])])
                                    (sort $ clusterCommon [(1,"cat"),(2,"dog"),(1,"cat")]))

cdcData =[ ("King" , [("Mar",2706),("Apr",3620),("May",1860),("Jun",2157),("July",5014),("Aug",4327),("Sep",2843)]),  
           ("Pierce", [("Mar",460),("Apr",965),("May",522),("Jun",2260),("July",2470),("Aug",1776),("Sep",1266)]), 
           ("Snohomish",[("Mar",1301),("Apr",1145),("May",532),("Jun",568),("July",1540),("Aug",4360),("Sep",811)]), 
           ("Spokane", [("Mar",147),("Apr",4000),("May",233),("Jun",794),("July",2412),("Aug",1530),("Sep",1751)]), 
           ("Whitman" , [("Apr",7),("May",5),("Jun",19),("July",51),("Aug",514),("Sep",732), ("Oct",278)])
        ]

p3_test1 = TestCase (assertEqual "(maxNumCases-test1)" 
                                  2260 (maxNumCases cdcData 
                                  "Jun") ) 
p3_test2 = TestCase (assertEqual "(maxNumCases-test2)" 
                                  4000 (maxNumCases cdcData 
                                  "Apr") ) 
p3_test3 = TestCase (assertEqual "(maxNumCases-test3)" 
                                  0  (maxNumCases cdcData 
                                  "Jan") ) 
p3_test4 = TestCase (assertEqual "(maxNumCases-test4)"
                                    4360
                                   ( maxNumCases cdcData "Aug"))
p3_test5 = TestCase (assertEqual "(maxNumCases-test5)"
                                            2706
                                   (maxNumCases cdcData "Mar") )
p4_test1 = TestCase (assertEqual "(groupIntoLists-test1)" 
                                  [[1],[2,3],[4,5,6],[7,8,9,10],[11,12]]  (groupIntoLists [1,2,3,4,5,6,7,8,9,10,11,12]) ) 
p4_test2 = TestCase (assertEqual "(groupIntoLists-test2)" 
                                  ["a","bc","def","ghij","klmno","pqrstu","wxyz012"]  (groupIntoLists "abcdefghijklmnopqrstuwxyz012") ) 
p4_test3 = TestCase (assertEqual "(groupIntoLists-test3)" 
                                  []  (groupIntoLists "") ) 
p4_test4 = TestCase (assertEqual "(groupIntoLists-test4)" 
                                  ["k","jd","fsg","kfdj","bgkjd","sfbgkf","djbgklj","dsfbfkjd","sbffdjgbk","fjbgfgdj"]  
                                      (groupIntoLists "kjdfsgkfdjbgkjdsfbgkfdjbgkljdsfbfkjdsbffdjgbkfjbgfgdj") ) 
p4_test5= TestCase (assertEqual "(groupIntoLists-test5)" 
                                  [[5],[9,1]]  (groupIntoLists [5,9,1]) ) 
p5_test1 = TestCase (assertEqual "(getSlice-test1)"  
                                 "Covid-19"  
                                 (getSlice ('(',')') "I got the (Covid-19) vaccine!" ) ) 
p5_test2 = TestCase (assertEqual "(getSlice-test2)" 
                                 "2021"  
                                 (getSlice ('(',')') "I hope this year (2021) will be better than last year (2020)." ) ) 
p5_test3 = TestCase (assertEqual "(getSlice-test3)"  
                                 "early" 
                                 (getSlice ('*','*') "Start the assignment *early*!" ) ) 
p5_test4 = TestCase (assertEqual "(getSlice-test4)"  
                                 [5,6,7,8]  
                                 (getSlice (0,9) [1,2,3,4,0,5,6,7,8,9,10,11] ) ) 
p5_test5 = TestCase (assertEqual "(getSlice-test5)"  
                                  []  
                                  (getSlice (0,9)  [1,2,3,4,5,6,7,8,9,10,11] ) ) 
p5_test6 = TestCase (assertEqual "(getSlice-test6)"  
                                  [5,6,7,8,10,11]  
                                  (getSlice (0,9)  [1,2,3,4,0,5,6,7,8,10,11] ) ) 
p5_test7 = TestCase (assertEqual "(getSlice-test7)"
                                             []   
                                             (getSlice ('(',')') "phew all done")   )
p5_test8= TestCase (assertEqual "(getSlice-test8)"
                                      "Done"
                                      (getSlice ('!','!') "I am all !Done!"))

--completed tests (1,2a,2b,2c,3,4,5)
tests = TestList [ TestLabel "Problem 1- test1 " p1_test1, 
                   TestLabel "Problem 1- test2 " p1_test2,  
                   TestLabel "Problem 1- test3 " p1_test3,
                   TestLabel "Problem 1- test4 " p1_test4,  
                   TestLabel "Problem 1- test5 " p1_test5,
                   TestLabel "Problem 1- test6 " p1_test6,
                   TestLabel "Problem 2a- test1 " p2a_test1,
                   TestLabel "Problem 2a- test2 " p2a_test2,  
                   TestLabel "Problem 2a- test3 " p2a_test3,
                   TestLabel "Problem 2a- test4 " p2a_test4,  
                   TestLabel "Problem 2a- test5 " p2a_test5,    
                   TestLabel "Problem 2a- test6 " p2a_test6,  
                   TestLabel "Problem 2b- test1 " p2b_test1, 
                   TestLabel "Problem 2b- test2 " p2b_test2, 
                   TestLabel "Problem 2b- test3 " p2b_test3, 
                   TestLabel "Problem 2b- test4 " p2b_test4, 
                   TestLabel "Problem 2b- test5 " p2b_test5, 
                   TestLabel "Problem 2c- test1 " p2c_test1, 
                   TestLabel "Problem 2c- test2 " p2c_test2, 
                   TestLabel "Problem 2c- test3 " p2c_test3, 
                   TestLabel "Problem 2c- test4 " p2c_test4,
                   TestLabel "Problem 2c- test5 " p2c_test5, 
                   TestLabel "Problem 3- test1 " p3_test1, 
                   TestLabel "Problem 3- test2 " p3_test2, 
                   TestLabel "Problem 3- test3 " p3_test3,
                   TestLabel "Problem 3- test4 " p3_test4, 
                   TestLabel "Problem 3- test5 " p3_test5,
                   TestLabel "Problem 4- test1 " p4_test1, 
                   TestLabel "Problem 4- test2 " p4_test2,
                   TestLabel "Problem 4- test3 " p4_test3, 
                   TestLabel "Problem 4- test4 " p4_test4,
                   TestLabel "Problem 4- test5 " p4_test5, 
                   TestLabel "Problem 5- test1 " p5_test1, 
                   TestLabel "Problem 5- test2 " p5_test2,
                   TestLabel "Problem 5- test3 " p5_test3, 
                   TestLabel "Problem 5- test4 " p5_test4, 
                   TestLabel "Problem 5- test5 " p5_test5, 
                   TestLabel "Problem 5- test6 " p5_test6,
                   TestLabel "Problem 5- test7 " p5_test7,
                   TestLabel "Problem 5- test8 " p5_test8 
                 ] 
                  
-- shortcut to run the tests
run = runTestTT  tests