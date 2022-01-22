import unittest
from psParser import read
from psItems import  Literal, Name, Array, Block, Value, ArrayValue, FunctionValue
from psOperators import Operators



class HW4GradingTests(unittest.TestCase):

    def setUp(self):
        #create the Stack object
        self.psstacks = Operators()
        #clear the opstack and the dictstack
        self.psstacks.clearBoth() 
        self.psstacks.dictstack.append({})

        self.opstack_output= {
            'test1': [6, 2], 
            'test2': [True, True, False, True], 
            'test3': [1, 10], 
            'test4': [10, 1], 
            'test5': [100, 10, 1], 
            'test6': [2, 2], 
            'test7': [ArrayValue([1, 2, 3, 4, 5, 6, 7])], 
            'test8': [ArrayValue([1, 2, 3, 4, 5, ArrayValue([6, 3, 4]), ArrayValue([True])])], 
            'test9': [4, 6], 
            'test10': [ArrayValue([4, 5, 6]), ArrayValue([8, 9, 10])], 
            'test11': [ArrayValue([1, 2, 3, 40, 50, 60, 70, 8, 9, 10]), ArrayValue([1, 2, 3, 4, 5, 6, 40, 50, 60, 70])], 
            'test12': [True], 
            'test13': [1, 2, ArrayValue([3, 4, 5, 6])], 
            'test14': [ArrayValue([1, 2, 3, 4]), False], 
            'test15': [1, 2, 3, 4, 5, 3, 4, 5, 8], 
            'test16': [1, 2, 6, 7, 8, 9, 3, 4, 5], 
            'test17': [1, 2, 7, 8, 9, 3, 4, 5, 6], 
            'test18': [5], 
            'test19': [2], 
            'test20': [256], 
            'test21': [1, 4, 9, 16], 
            'test22': [ArrayValue([1, 4, 9, 16])], 
            'test23': [9], 
            'test24': [10], 
            'test25': [10, 3, 10, 20, 1, 2], 
            'test26': [True], 
            'test27': [False, True, 10], 
            'test28': [120], 
            'test29': [720], 
            'test30': [30], 
            'test31': [True, True, True]}

    def compareObjectData(self,obj1,obj2):
        if type(obj1) != type(obj2):
            return False
        if isinstance(obj1,Literal):
            return obj1.value == obj2.value
        elif isinstance(obj1,Array) or isinstance(obj1,Block):
            for i in range(0,len(obj1.value)):
                if self.compareObjectData(obj1.value[i],obj2.value[i])== False:
                    return False
            return True
        elif isinstance(obj1,Name):
            return obj1.var_name == obj2.var_name
        elif isinstance(obj1,ArrayValue):
            for i in range(0,len(obj1.value)):
                if self.compareObjectData(obj1.value[i],obj2.value[i])== False:
                    return False
            return True
        elif isinstance(obj1,FunctionValue) :
            for i in range(0,len(obj1.value)):
                if self.compareObjectData(obj1.value[i],obj2.value[i])== False:
                    return False
            return True
        else:
            return obj1 == obj2


    def test_input1(self):
        testinput1 = """
            10 -2 add
            5 sub
            2 mul 
            20 3 mod
        """
        test_case = 'test{}'.format(1)
        expr_list = read(testinput1)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input2(self):
        testinput2 = """
            10 20 lt
            20 15 gt
            [1 2 3 4] [1 2 3 4] eq
            [1 2 3 4] dup eq 
        """
        test_case = 'test{}'.format(2)
        expr_list = read(testinput2)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input3(self):
        testinput3 = """
            /x 1 def
            x
            /x 10 def
            x
        """
        test_case = 'test{}'.format(3)
        expr_list = read(testinput3)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))


    def test_input4(self):
        testinput4 = """
            /x 1 def
            1 dict begin /x 10 def x end
            x
        """
        test_case = 'test{}'.format(4)
        expr_list = read(testinput4)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input5(self):
        testinput5 = """
            /x 1 def
            1 dict begin /x 10 def  
                1 dict begin /x 100 def x end 
                x 
            end
            x
        """
        test_case = 'test{}'.format(5)
        expr_list = read(testinput5)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input6(self):
        testinput6 = """
            /x 1 def
            /y 2 def
            1 dict begin /x 10 def  
                1 dict begin /x 100 def y end 
                y
            end
        """ 
        test_case = 'test{}'.format(6)
        expr_list = read(testinput6)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input7(self):
        testinput7 = """
            /x 3 def 
            /y 4 def
            [1 2 x x 1 add 5 x x add x y add ] 
        """
        test_case = 'test{}'.format(7)
        expr_list = read(testinput7)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input8(self):
        testinput8 = """
            /x 3 def 
            /y 4 def
            [1 2 x x 1 add 5 [x x add x y] [true]] 
        """
        test_case = 'test{}'.format(8)
        expr_list = read(testinput8)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input9(self):
        testinput9 = """
            [1 2 3 4] length
            [1 2 3 [4 5] 6 [false] ] length
        """
        test_case = 'test{}'.format(9)
        expr_list = read(testinput9)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input10(self):
        testinput10 = """
            [1 2 3 4 5 6 7 8 9 10] 3 3 getinterval
            [1 2 3 4 5 6 7 8 9 10] 7 3 getinterval
        """
        test_case = 'test{}'.format(10)
        expr_list = read(testinput10)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input11(self):
        testinput11 = """
            [1 2 3 4 5 6 7 8 9 10] dup 3 [40 50 60 70]   putinterval
            [1 2 3 4 5 6 7 8 9 10] dup 6 [40 50 60 70]   putinterval
        """
        test_case = 'test{}'.format(11)
        expr_list = read(testinput11)
        for expr in expr_list:
            expr.evaluate(self.psstacks)
        self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
        for i in range(0,len(self.opstack_output[test_case])):
            self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input12(self):
            testinput12 = """
                [1 2 3 4 5 6] aload pop add add add add add 21 eq
            """
            test_case = 'test{}'.format(12)
            expr_list = read(testinput12)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input13(self):
            testinput13 = """
                1 2 3 4 5 6 [0 0 0 0] astore 
            """
            test_case = 'test{}'.format(13)
            expr_list = read(testinput13)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input14(self):
            testinput14 = """
                [1 2 3 4] dup /arr exch def 
                [1 2 3 4] arr eq
            """
            test_case = 'test{}'.format(14)
            expr_list = read(testinput14)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input15(self):
            testinput15 = """
                1 2 3 4 5 3 copy count
            """
            test_case = 'test{}'.format(15)
            expr_list = read(testinput15)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input16(self):
            testinput16 = """
                1 2 3 4 5 6 7 8 9 7 4 roll
            """
            test_case = 'test{}'.format(16)
            expr_list = read(testinput16)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input17(self):
            testinput17 = """
                1 2 3 4 5 6 7 8 9 7 -4 roll
            """
            test_case = 'test{}'.format(17)
            expr_list = read(testinput17)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))


    def test_input18(self):
            testinput18 = """
                /isNeg { 0 lt } def  -5 dup isNeg { -1 mul } if
            """
            test_case = 'test{}'.format(18)
            expr_list = read(testinput18)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input19(self):
            testinput19 = """
                /isNeg { 0 lt } def  -1 dup isNeg { -2 mul } { 3 mul} ifelse
            """
            test_case = 'test{}'.format(19)
            expr_list = read(testinput19)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))


    def test_input20(self):
            testinput20 = """
                1 8 {2 mul } repeat 
            """
            test_case = 'test{}'.format(20)
            expr_list = read(testinput20)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input21(self):
            testinput21 = """
                [1 2 3 4] {dup mul } forall
            """
            test_case = 'test{}'.format(21)
            expr_list = read(testinput21)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input22(self):
            testinput22 = """
                /arr [1 2 3 4] def arr {dup mul } forall arr astore pop arr
            """
            test_case = 'test{}'.format(22)
            expr_list = read(testinput22)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input23(self):
            testinput23 = """
                /x 4 def 
                /square {dup mul} def
                [x 1 x sub 1] /arr exch def  
                arr 1 1 getinterval aload pop dup
                0 gt 
                {2 mul} {square} ifelse
            """
            test_case = 'test{}'.format(23)
            expr_list = read(testinput23)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input24(self):
            testinput24 = """
                /x 10 def
                /y 20 def
                /x 0 def
                /y 2 def
                5 { x y add /x exch def } repeat 
                x
            """
            test_case = 'test{}'.format(24)
            expr_list = read(testinput24)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input25(self):
            testinput25 = """
                /x 1 def
                /y 2 def
                1 dict begin
                /x 10 def
                1 dict begin /y 3 def x y end
                /y 20 def
                x y
                end
                x y
            """
            test_case = 'test{}'.format(25)
            expr_list = read(testinput25)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input26(self):
            testinput26 = """
                1 2 3 4 5  15 5 { exch sub} repeat 0 eq
            """
            test_case = 'test{}'.format(26)
            expr_list = read(testinput26)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input27(self):
            testinput27 = """
                [1 2 3 4] {2 mod 0 eq} forall 
                {
                    { /x 1 def }
                    { /x 10 def }
                    ifelse
                } if
                x
            """
            test_case = 'test{}'.format(27)
            expr_list = read(testinput27)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input28(self):
            testinput28 = """
                /n 5 def
                /fact {
                    0 dict begin
                    /n exch def
                    n 2 lt
                    { 1}
                    {n 1 sub fact n mul }
                    ifelse
                    end
                } def
                n fact
            """
            test_case = 'test{}'.format(28)
            expr_list = read(testinput28)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input29(self):
            testinput29 = """
                /fact {
                    0 dict
                    begin
                        /n exch def
                        1
                        n { n mul /n n 1 sub def } repeat
                    end
                } def
                6 fact
            """
            test_case = 'test{}'.format(29)
            expr_list = read(testinput29)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input30(self):
            testinput30 = """
                /sumArray {0 exch aload pop count n sub {add} repeat } def
                /x 5 def
                /y 10 def
                /n 1 def
                [x y x y add] sumArray
            """
            test_case = 'test{}'.format(30)
            expr_list = read(testinput30)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))

    def test_input31(self):
            testinput31 = """
                [ 1 2 3 4 5 6 7 8 9 ] 6 3 getinterval aload pop
                [ 7 8 9 1 2 3 4 5 6 ] 0 3 getinterval aload pop
                /x exch def /y exch def /z exch def
                x eq count 1 roll y eq count 1 roll z eq count 1 roll
            """
            test_case = 'test{}'.format(31)
            expr_list = read(testinput31)
            for expr in expr_list:
                expr.evaluate(self.psstacks)
            self.assertEqual(len(self.psstacks.opstack),len(self.opstack_output[test_case]))
            for i in range(0,len(self.opstack_output[test_case])):
                self.assertTrue(self.compareObjectData(self.psstacks.opstack[i], self.opstack_output[test_case][i]))


if __name__ == '__main__':
    unittest.main()

