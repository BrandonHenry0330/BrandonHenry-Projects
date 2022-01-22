-- CptS 355 - Fall 2021 -- Homework1 - Haskell
-- Name: Brandon Henry 
-- Collaborators: Nate tsig, Nathan Waltz

module HW1
     where

-- Q1 everyOther (complete)
--everyOther [1,2,3,4,5,6,7,8,9,10] --> [1,3,5,7,9]
everyOther [] = []
everyOther (x:xs) = (everyOtherHelper 1 (x:xs) 1)
     where
          everyOtherHelper n [] m = []
          everyOtherHelper n (x:xs) m |(n == 0) = (everyOtherHelper m xs m)
                                      | otherwise = x:(everyOtherHelper (n-1) xs m)

-- Q2(a) eliminateDuplicates (complete)
list = [6,5,1,6,4,2,2,3,7,2,1,1,2,3,4,5,6,7] -- [1,2,3,4,5,6,7]
eliminateDuplicates :: Eq a=>[a]->[a]

eliminateDuplicates [] = []
eliminateDuplicates (x:xs)  |(x `elem` xs) = (eliminateDuplicates xs) 
                            |otherwise = x:(eliminateDuplicates xs )

-- Q2(b) matchingSeconds(complete)
matchinglist = [("cat",5),("dog",9),("parrot",3),("cat",3),("fish",1)] 
matchingSeconds input [] = []
matchingSeconds input ((animal,number):xs) | (input == animal ) = number:(matchingSeconds input xs)
                                           | otherwise = (matchingSeconds input xs)
-- Q2(c) clusterCommon (complete)
 
clusterCommon :: (Eq t, Eq a) => [(t,a)] -> [(t,[a])]

clusterCommon iL = (eliminateDuplicates (clusterCommonHelper iL))
     where
          clusterCommonHelper [] = []
          clusterCommonHelper ((x,y):xs) = (x,(matchingSeconds x (iL) )):(clusterCommonHelper xs)                      

-- Q3 maxNumCases (complete)
maxNumCases :: (Num p,Ord p,Eq t) => [(a,[(t,p)])] -> t -> p

mycdcData=[("King",[("Mar",2706),("Apr",3620),("May",1860),("Jun",2157),("July",5014),("Aug",4327),("Sep",2843)]),("Pierce",[("Mar",460),("Apr",965),("May",522),("Jun",2260),("July",2470),("Aug",1776),("Sep",1266)]),("Snohomish",[("Mar",1301),("Apr",1145),("May",532),("Jun",568),("July",1540),("Aug",4360),("Sep",811)]),("Spokane",[("Mar",147),("Apr",4000),("May",233),("Jun",794),("July",2412),("Aug",1530),("Sep",1751)]),("Whitman",[("Apr",7),("May",5),("Jun",19),("July",51),("Aug",514),("Sep",732),("Oct",278)])]

maxNumCases iL month = (maxNumCasesRunner iL month 0)

maxNumCasesRunner [] month high = high + 0
maxNumCasesRunner ((county,(x,y):ys):xs) month high | ((maxNumCasesHelp ((x,y):ys) month 0) > high) = ((maxNumCasesRunner xs month (maxNumCasesHelp ((x,y):ys) month 0 ) ) )
                                              | otherwise = (maxNumCasesRunner xs month high)
     where
          maxNumCasesHelp [] month high = high + 0
          maxNumCasesHelp ((x,y):xs) month high |(month == x) = (maxNumCasesHelp xs month (isbigger y high))
                                                |otherwise = (maxNumCasesHelp xs month high)
                    where
                         isbigger y high | (y > high) = y
                                         | otherwise = high

-- Q4 groupIntoLists(complete)
--groupIntoLists [1,2,3,4,5,6,7,8,9,10,11,12] --> [[1],[2,3],[4,5,6],[7,8,9,10],[11,12]]
groupIntoLists ::[a]->[[a]]
groupIntoLists iL = (groupIntoListsHelper iL 1 1 [])
     where
          groupIntoListsHelper [] n m [] = []
          groupIntoListsHelper [] n m buf = [(reverse buf)]
          groupIntoListsHelper (x:xs) n m buf | (n == 0) = (reverse buf):(groupIntoListsHelper (x:xs) (m+1) (m+1) [])
                                              | otherwise = (groupIntoListsHelper xs (n-1) m (x:buf))
-- Q5 getSlice (complete)
getSlicetest = [1,2,3,4,0,5,6,7,8,9,10,11] --output [5,6,7,8] 
getSlicetest2 = "Ihopethisyear(2021)willbebetterthanlastyear(2020)." --"2021" ('(',')')

getSlice (low,high) [] = []
getSlice (low,high) (x:xs) |(low == x) = (getSliceHelper high xs)
                           |otherwise = (getSlice (low,high) xs)
     where    
               getSliceHelper high [] = []
               getSliceHelper high (x:xs) |(high /= x) = x:(getSliceHelper high xs)
                                          | otherwise = (getSliceHelper high [])
                              

