--Name: Brandon Henry

module HW2
     where
{- 1. groupbyNTail - 10% complete-}


groupbyNTail iL n = (groupbyNTailHelper iL n [] [])
     where     
          groupbyNTailHelper [] _ buf list = reverse ((reverse buf):list)
          groupbyNTailHelper (x:xs) n buf list|((length buf) >= n) = (groupbyNTailHelper (x:xs) n [] ((reverse buf):list))
                                              | otherwise = (groupbyNTailHelper xs n (x:buf) list)


--not tail recursive version 
groupbyN iL n = (grouphelper iL n [])
     where
          grouphelper [] n buf = (reverse buf):[] 
          grouphelper (x:xs) n buf|(length buf) >= n = (reverse buf):(grouphelper xs n (x:[]))
                                  |otherwise = (grouphelper xs n(x:buf))

-----------------------------------------------------------

{- 2.  elemAll and stopsAt  -  20% -}

{- (a)  elemAll - 10% (complete) -}
-- please don't include the myCatsLog list in your solution file. 
--[3,5,7,10] [1,2,3,4,5,6,7,8,9,10]

--elemAll :: Eq a => [a] -> [a] -> Bool
elemAll list1 list2 = elemAllHelper (map (\x -> (x `elem` list2)) list1) 
                    where
                         elemAllHelper = foldr (\x z -> (x && z)) True



{- (b) stopsAt - 10% (complete)-}
buses = [("Wheat",["Chinook","Orchard","Valley","Maple","Aspen","TerreView","Clay","Dismores","Martin","Bishop","Walmart","PorchLight","Campus"]),
     ("Silver",["TransferStation","PorchLight","Stadium","Bishop","Walmart","Shopco","RockeyWay"]),
     ("Blue",["TransferStation","State","Larry","TerreView","Grand","TacoBell","Chinook","Library"]),("Gray",["TransferStation","Wawawai","Main","Sunnyside","Crestview","CityHall","Stadium","Colorado"])] 

--stopsAt ["Bishop","TerreView","Walmart"] buses -> ["Wheat"]
--stopsAt :: [a] -> [(b,[a])] -> [b]

stopsAt stops xs = map (\(route,stoplist) -> route) (filter (\(route,stoplist) -> (elemAll stops stoplist)) xs) 
--stopsAt stops xs = [ bus | (bus, routes) <- xs, if (any [route | route <- routes, route `elem` stops])]

--stopsAtHelper stops (x,y) buf |(elemAll stops y) = x:buf
--                              | otherwise = []

-----------------------------------------------------------

{- 3. isBigger and applyRange - 25% -}

--define the Timestamp datatype
data Timestamp =  DATE (Int,Int,Int) |  DATETIME (Int,Int,Int,Int,Int) 
                  deriving (Show, Eq)

{- (a)  isBigger - 15% -}
--possibilities
isBigger (DATE (v1,v2,v3)) (DATE (0,0,0)) = True
isBigger (DATE (0,0,0)) (DATE (v1,v2,v3)) = False
isBigger (DATE (v1,v2,v3)) (DATE (z1,z2,z3)) = if (v1 > z1) 
                                                  then True 
                                             else if (v1 < z1) 
                                                  then False 
                                             else if (v2 > z2)
                                                  then True
                                             else if (v2 < z2) 
                                                  then False 
                                             else if (v3 > z3)
                                                  then True
                                             else if (v3 < z3) 
                                                  then False 
                                             else False
isBigger (DATE (v1,v2,v3)) (DATETIME (z1,z2,z3,z4,z5)) = if (v1 > z1) 
                                                  then True 
                                             else if (v1 < z1) 
                                                  then False 
                                             else if (v2 > z2)
                                                  then True
                                             else if (v2 < z2) 
                                                  then False 
                                             else if (v3 > z3)
                                                  then True
                                             else if (v3 < z3) 
                                                  then False 
                                             else False
isBigger (DATETIME (z1,z2,z3,z4,z5)) (DATE (v1,v2,v3)) = if (v3 < z3) 
                                                  then True 
                                             else if (v3 > z3) 
                                                  then False 
                                             else if (v1 < z1)
                                                  then True
                                             else if (v1 > z1) 
                                                  then False 
                                             else if (v2 < z2)
                                                  then True
                                             else if (v2 > z2) 
                                                  then False 
                                             else False
isBigger (DATETIME (month,day,year,hour,minute)) (DATETIME (month1,day1,year1,hour1,minute1)) = if (year > year1)
                                                                                                    then True
                                                                                               else if (year < year1)
                                                                                                    then False
                                                                                               else if (month > month1)
                                                                                                    then True
                                                                                               else if (month < month1)
                                                                                                    then False
                                                                                               else if (day > day1)
                                                                                                    then True
                                                                                               else if (day < day1)
                                                                                                    then False
                                                                                               else if (hour > hour1)
                                                                                                    then True
                                                                                               else if (hour < hour1)
                                                                                                    then False
                                                                                               else if (minute > minute1)
                                                                                                    then True
                                                                                               else if (minute < minute1)
                                                                                                    then False
                                                                                               else False
{- (b) applyRange - 10% -}

mydatelist = [DATE(5,28,2021),DATETIME(6,1,2021,14,15),DATE(6,22,2021),DATE(6,1,2021),DATETIME(6,21,2021,15,20),DATETIME(5,21,2020,14,40),DATE(5,20,2021),DATETIME(6,9,2021,19,30),DATETIME(6,10,2021,11,10)]

applyRange (date1,date2) dataset = filter (\d -> (isBigger d date1) && (isBigger date2 d)) dataset 




-----------------------------------------------------------
{-4 - foldTree, createRTree, fastSearch  - 35%-}

--define Tree and RTree data types
data Tree a = LEAF a | NODE a (Tree a) (Tree a)
               deriving (Show,  Eq, Ord)

data RTree a = RLEAF a | RNODE a (a,a) (RTree a) (RTree a)
                    deriving (Show, Eq, Ord)

{- (a) foldTree - 8% -}
--tree2 = NODE"F" (NODE"D" (LEAF"E") (NODE"C" (LEAF"B") (LEAF"G"))) (NODE"G" (NODE"H" (LEAF"F") (LEAF"E")) (LEAF"A"))

foldTree :: (a -> a -> a) -> Tree a -> a
foldTree function (LEAF val) = val
foldTree function (NODE val t1 t2) =  function (function val (foldTree function t1)) (foldTree function t2)
       

{- (b) createRTree - 12% -}

--this function also wants the range of the tree per node, (min,max) of each node

--Lab2 evaluateTree

mytree1 = NODE 5 (NODE 1 (NODE 2 (LEAF 4) (LEAF 5) )(LEAF 6)) (NODE 10 (LEAF 8)(LEAF 9))
mytree2 = NODE"F" (NODE"D" (LEAF"E") (NODE"C" (LEAF"B") (LEAF"G"))) (NODE"G" (NODE"H" (LEAF"F") (LEAF"E")) (LEAF"A"))

--createRTree
createRTree (LEAF v) = (RLEAF v)
createRTree (NODE value t1 t2) = RNODE value ((getChildMin (NODE value t1 t2)),(getChildMax (NODE value t1 t2))) (createRTree t1)  (createRTree t2)
                                   where
                                        getChildMin (LEAF v) = v
                                        getChildMin (NODE v t1 t2) = min v (getChildMin t1) (getChildMin t2) 
                                        getChildMax (LEAF v) = v
                                        getChildMax (NODE v t1 t2) = max v (getChildMax t1) (getChildMax t2) 
                                        min v1 v2 v3 |(v1 < v2) && (v1 < v3) = v1
                                                     |(v2 < v1) && (v2 < v3) = v2
                                                     |(v3 < v1) && (v3 < v2) = v3
                                                     |otherwise = v3
                                        max v1 v2 v3 |(v1 > v2) && (v1 > v3) = v1
                                                     |(v2 > v1) && (v2 > v3) = v2
                                                     |(v3 > v1) && (v3 > v2) = v3
                                                     |otherwise = v3
                                        

{- (c) fastSearch - 15% -}
fastSearch :: Ord t => RTree t -> t -> [([Char],t)] 

fastSearch node n = (fastSearchHelper node n [])

fastSearchHelper (RLEAF v) n buf = ("leaf", v):buf

fastSearchHelper (RNODE v (min,max) t1 t2) n buf = if ((n <= max) && (n >= min)) 

                                               then ("node",v):((fastSearchHelper t1 n buf) ++ (fastSearchHelper t2 n buf) )

                                               else ("node", v):buf

-------------------------------------------------------------------

{- Tree Examples 5% -}
-- include your tree examples in the test file. 

{-Testing your tree functions - 5%-}


