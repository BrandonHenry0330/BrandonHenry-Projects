from psOperators import Operators
from psItems import ArrayValue
import unittest
import sys
sys.path.append('../')

class HW4Sampletests_part1(unittest.TestCase):
    #If the setUp doesn't clear the stacks succesfully, copy the following function to HW4_part1.py and call it in setup. 

    def setUp(self):
        #create the Operators object
        self.psstacks = Operators()
        #clear the opstack and the dictstack
        self.psstacks.clearBoth() 

    # Tests for helper functions : define, lookup   
    def test_lookup1(self):
        self.psstacks.dictPush({'/v':3, '/x': 20})
        self.psstacks.dictPush({'/v':4, '/x': 10})
        self.psstacks.dictPush({'/v':5})
        self.assertEqual(self.psstacks.lookup('x'),10)
        self.assertEqual(self.psstacks.lookup('v'),5)

    def testLookup2(self):
        self.psstacks.dictPush({'/a':355})
        arrayV = ArrayValue([3,5,5])
        self.psstacks.dictPush({'/a':arrayV})
        self.assertTrue(self.psstacks.lookup("a") is arrayV)
        self.assertEqual(self.psstacks.lookup("a").value,arrayV.value)

    def test_define1(self):
        self.psstacks.dictPush({})
        self.psstacks.define("/n1", 4)
        self.assertEqual(self.psstacks.lookup("n1"),4)

    def test_define2(self):
        self.psstacks.dictPush({})
        self.psstacks.define("/n1", 4)
        self.psstacks.define("/n1", 5)
        self.psstacks.define("/n2", 6)
        self.assertEqual(self.psstacks.lookup("n1"),5)
        self.assertEqual(self.psstacks.lookup("n2"),6)        

    def test_define3(self):
        self.psstacks.dictPush({})
        self.psstacks.define("/n1", 4)
        self.psstacks.dictPush({})
        self.psstacks.define("/n2", 6)
        self.psstacks.define("/n2", 7)
        self.psstacks.dictPush({})
        self.psstacks.define("/n1", 6)
        self.assertEqual(self.psstacks.lookup("n1"),6)
        self.assertEqual(self.psstacks.lookup("n2"),7)    
    #-----------------------------------------------------
    #Arithmatic operator tests
    def test_add(self):
        #9 3 add
        self.psstacks.opPush(9)
        self.psstacks.opPush(3)
        self.psstacks.add()
        self.assertEqual(self.psstacks.opPop(),12)

    def test_sub(self):
        #10 2 sub
        self.psstacks.opPush(10)
        self.psstacks.opPush(2)
        self.psstacks.sub()
        self.assertEqual(self.psstacks.opPop(),8)

    def test_mul(self):
        #2 40 mul
        self.psstacks.opPush(2)
        self.psstacks.opPush(40)
        self.psstacks.mul()
        self.assertEqual(self.psstacks.opPop(),80)

    def test_mod(self):
        #20 3 mod
        self.psstacks.opPush(20)
        self.psstacks.opPush(3)
        self.psstacks.mod()
        self.assertEqual(self.psstacks.opPop(),2)

    #-----------------------------------------------------
    #Comparison operators tests
    def test_eq1(self):
        #6 6 eq
        self.psstacks.opPush(6)
        self.psstacks.opPush(6)
        self.psstacks.eq()
        self.assertEqual(self.psstacks.opPop(),True)

    def test_eq2(self):
        #[1 2 3 4] [1 2 3 4] eq
        self.psstacks.opPush(ArrayValue([1,2,3,4]))
        self.psstacks.opPush(ArrayValue([1,2,3,4]))
        self.psstacks.eq()
        self.assertEqual(self.psstacks.opPop(),False)
        arr1 = ArrayValue([1,2,3,4])
        self.psstacks.opPush(arr1)
        self.psstacks.opPush(arr1)
        self.psstacks.eq()
        self.assertEqual(self.psstacks.opPop(),True)

    def test_lt(self):
        #3 6 lt
        self.psstacks.opPush(3)
        self.psstacks.opPush(6)
        self.psstacks.lt()
        self.assertEqual(self.psstacks.opPop(),True)

    def test_gt(self):
        #4 5 gt
        self.psstacks.opPush(4)
        self.psstacks.opPush(5)
        self.psstacks.gt()
        self.assertEqual(self.psstacks.opPop(),False)

    # #-----------------------------------------------------
    # #Array operator tests
    def test_length(self):
        #[3,5,5,3,2,2] length
        self.psstacks.opPush(ArrayValue([3,5,5,3,2,2]))
        self.psstacks.length()
        self.assertEqual(self.psstacks.opPop(),6)      
        self.assertTrue(len(self.psstacks.opstack)==0) 
        #length will not push back the ArrayValue onto the opstack      

    def test_getinterval(self):
        #[0 1 2 3 [4 5 6] 7 True 8 9] 3 5 getinterval
        self.psstacks.opPush(ArrayValue([0, 1, 2, 3, ArrayValue([4, 5, 6]), 7, True, 8, 9]))
        self.psstacks.opPush(3)
        self.psstacks.opPush(5)
        self.psstacks.getinterval()
        array =  self.psstacks.opPop() #pop the array slice
        self.assertEqual(array.value[0], 3)
        self.assertEqual(array.value[1].value, [4, 5, 6])
        self.assertEqual(array.value[2:], [7, True, 8])
        self.assertTrue(len(self.psstacks.opstack)==0)
        #getinterval will not push back the original array onto the opstack 

    def test_putinterval1(self):
        #[0 1 2 3 4 5 6 7] dup dup dup 3 [30 40 50 60] putinterval
        arr1 = ArrayValue([0, 1, 2, 3, 4, 5, 6, 7] )
        self.psstacks.opPush(arr1)
        self.psstacks.dup()  # duplicating the array reference
        self.psstacks.dup()  # duplicating the array reference
        self.psstacks.opPush(3)
        self.psstacks.opPush(ArrayValue([30, 40, 50, 60]))  # the slice that starts at index 3 will be replaced by [30 40 50 60]
        self.psstacks.putinterval()  # putinterval will not push back the changed array onto the opstack 
        arr2 = self.psstacks.opPop()  # we pop the string reference we copied with "dup"; 
        self.assertTrue(arr2 is arr1)  # check if it the same object
        self.assertEqual(arr2.value,[0, 1, 2, 30, 40, 50, 60, 7])  # we check if the ArrValue object value is updated
        arr3 = self.psstacks.opPop()  # #we pop the string reference we copied with "dup";
        self.assertTrue(arr3 is arr1)  # check if it the same object
        self.assertEqual(arr3.value,[0, 1, 2, 30, 40, 50, 60, 7])  # we check if the ArrayValue object value is updated
        self.assertTrue(len(self.psstacks.opstack)==0)

    def test_putinterval2(self):
        #/x [0 1 2 3 4 5 6 7] def x 3 [30 40 50 60] putinterval x
        arr1 = ArrayValue([0, 1, 2, 3, 4, 5, 6, 7] )
        self.psstacks.opPush('/x')
        self.psstacks.opPush(arr1)
        self.psstacks.psDef()  #defines x; x holds the array reference
        self.psstacks.opPush(self.psstacks.lookup('x'))  # pushed the array reference x holds onto the stack
        self.psstacks.opPush(3)
        self.psstacks.opPush(ArrayValue([30, 40, 50, 60]))  # the slice that starts at index 3 will be replaced by [30 40 50 60]
        self.psstacks.putinterval()  # putinterval will not push back the changed array onto the opstack 
        self.psstacks.opPush(self.psstacks.lookup('x'))  # pushed the array reference x holds onto the stack
        arr2 = self.psstacks.opPop()  # we pop the array reference ;
        self.assertTrue(arr2 is arr1) # check if it the same object
        self.assertEqual(arr2.value,[0, 1, 2, 30, 40, 50, 60, 7])  # we check if the ArrayValue object value is updated
        self.assertTrue(len(self.psstacks.opstack)==0)

    def test_aload(self):
        #[3 5 5 True] aload
        self.psstacks.opPush(ArrayValue([3,5,5,True]))
        self.psstacks.aload()
        self.assertTrue(self.psstacks.opPop().value==[3,5,5,True] and  #check whether the arrray value is pushed back onto the stack 
                        self.psstacks.opPop()==True and self.psstacks.opPop() == 5 and self.psstacks.opPop() == 5 and self.psstacks.opPop()==3)  

    def test_astore(self):
        #1 2 3 4 True [0,0,0] astore
        self.psstacks.opPush(1)
        self.psstacks.opPush(2)
        self.psstacks.opPush(3)
        self.psstacks.opPush(4)
        self.psstacks.opPush(True)
        self.psstacks.opPush(ArrayValue([0,0,0]))  
        self.psstacks.astore()
        self.assertTrue(self.psstacks.opPop().value==[3,4,True] and self.psstacks.opPop()==2 and self.psstacks.opPop()==1)  

    # #-----------------------------------------------------
    # #stack manipulation operator tests
    def test_dup(self):
        #[3 5 5 True 4]  dup
        self.psstacks.opPush(ArrayValue([3,5,5,True,4]))
        self.psstacks.dup()
        isSame = self.psstacks.opPop() is self.psstacks.opPop()
        self.assertTrue(isSame)

    def test_exch(self):
        # /x 10 exch
        self.psstacks.opPush('/x')
        self.psstacks.opPush(10)
        self.psstacks.exch()
        self.assertEqual(self.psstacks.opPop(),'/x')
        self.assertEqual(self.psstacks.opPop(),10)

    def test_pop(self):
        l1 = len(self.psstacks.opstack)
        self.psstacks.opPush(10)
        self.psstacks.pop()
        l2 = len(self.psstacks.opstack)
        self.assertEqual(l1,l2)

    def test_copy(self):
        #true 1 3 4 3 copy
        self.psstacks.opPush(True)
        self.psstacks.opPush(1)
        self.psstacks.opPush(3)
        self.psstacks.opPush(4)
        self.psstacks.opPush(3)
        self.psstacks.copy()
        self.assertTrue(self.psstacks.opPop()==4 and self.psstacks.opPop()==3 and self.psstacks.opPop()==1 and self.psstacks.opPop()==4 and self.psstacks.opPop()==3 and self.psstacks.opPop()==1 and self.psstacks.opPop()==True)
        
    def test_clear(self):
        #10 /x clear
        self.psstacks.opPush(10)
        self.psstacks.opPush("/x")
        self.psstacks.clear()
        self.assertEqual(len(self.psstacks.opstack),0)

    def test_roll1(self):
        #1 2 3 4 5 6 7 8 6 4 roll
        for i in range(1,9): # push 1 through 8 (8 is included)
            self.psstacks.opPush(i)
        self.psstacks.opPush(6) # roll top 6
        self.psstacks.opPush(4) #roll 4 times ; clockwise
        self.psstacks.roll()
        print(self.psstacks.opstack)
        self.assertEqual(self.psstacks.opPop(),4)
        self.assertEqual(self.psstacks.opPop(),3)
        self.assertEqual(self.psstacks.opPop(),8)
        self.assertEqual(self.psstacks.opPop(),7)
        self.assertEqual(self.psstacks.opPop(),6)
        self.assertEqual(self.psstacks.opPop(),5)
        self.assertEqual(self.psstacks.opPop(),2)
        self.assertEqual(self.psstacks.opPop(),1)

    def test_roll2(self):
        #1 2 3 4 5 6 7 8 6 -4 roll
        for i in range(1,9): # push 1 through 8 (8 is included)
            self.psstacks.opPush(i)
        self.psstacks.opPush(6) # roll top 6
        self.psstacks.opPush(-4) #roll 4 times ; counter-clockwise
        self.psstacks.roll()
        self.assertEqual(self.psstacks.opPop(),6)
        self.assertEqual(self.psstacks.opPop(),5)
        self.assertEqual(self.psstacks.opPop(),4)
        self.assertEqual(self.psstacks.opPop(),3)
        self.assertEqual(self.psstacks.opPop(),8)
        self.assertEqual(self.psstacks.opPop(),7)
        self.assertEqual(self.psstacks.opPop(),2)
        self.assertEqual(self.psstacks.opPop(),1)
        
    # #-----------------------------------------------------
    #dictionary stack operators
    def test_dict(self):
        #1 dict
        self.psstacks.opPush(1)
        self.psstacks.psDict()
        self.assertEqual(self.psstacks.opPop(),{})

    def test_psDef(self):
        #/x 10 def /x 20 def x
        self.psstacks.dictPush({})
        self.psstacks.opPush("/x")
        self.psstacks.opPush(10)
        self.psstacks.psDef()
        self.psstacks.opPush("/x")
        self.psstacks.opPush(20)
        self.psstacks.psDef()
        self.assertEqual(self.psstacks.lookup('x'),20)

    def test_psDef2(self):
        #/x 10 def 1 dict begin /y 20 def x
        self.psstacks.dictPush({})
        self.psstacks.opPush("/x")
        self.psstacks.opPush(10)
        self.psstacks.psDef()
        self.psstacks.dictPush({})
        self.psstacks.opPush("/y")
        self.psstacks.opPush(20)
        self.psstacks.psDef()
        self.assertEqual(self.psstacks.lookup('x'),10)

    def test_beginEnd(self):
        #/x 3 def 1 dict begin /x 4 def end x
        self.psstacks.opPush(1)
        self.psstacks.psDict()
        self.psstacks.opPush("/x")
        self.psstacks.opPush(3)
        self.psstacks.psDef()
        self.psstacks.opPush(1)
        self.psstacks.psDict()
        self.psstacks.begin()
        self.psstacks.opPush("/x")
        self.psstacks.opPush(4)
        self.psstacks.psDef()
        self.psstacks.end() 
        self.assertEqual(self.psstacks.lookup('x'),3)

    def test_psDef3(self):
        #/x 3 def 1 dict begin /x 30 def 1 dict begin /x 300 def end x
        # define x in the bottom dictionary
        self.psstacks.dictPush({})
        self.psstacks.opPush("/x")
        self.psstacks.opPush(3)
        self.psstacks.psDef()
        # define x in the second dictionary
        self.psstacks.dictPush({})
        self.psstacks.opPush("/x")
        self.psstacks.opPush(30)
        self.psstacks.psDef()
        # define x in the third dictionary
        self.psstacks.dictPush({})
        self.psstacks.opPush("/x")
        self.psstacks.opPush(300)
        self.psstacks.psDef()
        self.psstacks.dictPop()
        self.assertEqual(self.psstacks.lookup('x'),30)

if __name__ == '__main__':
    unittest.main()

