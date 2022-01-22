import sys

from psParser import read
from psOperators import Operators
from psItems import ArrayValue, Literal, Name, Array,Block
from colors import *

# Postscript examples that use arithmetic operators. 
testinput1 = """
    10 -2 add
    5 sub
    2 mul 
    20 3 mod
"""
#opstack : [6, 2]

# Postscript examples that use comparison operators. 
testinput2 = """
    10 20 lt
    20 15 gt
    [1 2 3 4] [1 2 3 4] eq
    [1 2 3 4] dup eq 
"""
# opstack : [True, True, False, True]

# Postscript examples that use def, dict, begin, end
testinput3 = """
    /x 1 def
    x
    /x 10 def
    x
"""
# opstack : [1, 10]

testinput4 = """
    /x 1 def
    1 dict begin /x 10 def x end
    x
"""
# opstack : [10, 1]

testinput5 = """
    /x 1 def
    1 dict begin /x 10 def  
        1 dict begin /x 100 def x end 
        x 
    end
    x
"""
# opstack : [100, 10, 1]

testinput6 = """
    /x 1 def
    /y 2 def
    1 dict begin /x 10 def  
        1 dict begin /x 100 def y end 
        y
    end
"""
# opstack : [2, 2]


# Postscript examples that use array operators. 

#test array evaluation
testinput7 = """
    /x 3 def 
    /y 4 def
    [1 2 x x 1 add 5 x x add x y add ] 
"""
# opstack : [ArrayValue([1, 2, 3, 4, 5, 6, 7])]

testinput8 = """
    /x 3 def 
    /y 4 def
    [1 2 x x 1 add 5 [x x add x y] [true]] 
"""
# opstack : [ArrayValue([1, 2, 3, 4, 5, ArrayValue([6, 3, 4]), ArrayValue([True])])]

testinput9 = """
    [1 2 3 4] length
    [1 2 3 [4 5] 6 [false] ] length
"""
# opstack : [4, 6]

testinput10 = """
     [1 2 3 4 5 6 7 8 9 10] 3 3 getinterval
     [1 2 3 4 5 6 7 8 9 10] 7 3 getinterval
"""
# opstack : [ArrayValue([4, 5, 6]), ArrayValue([8, 9, 10])]

testinput11 = """
     [1 2 3 4 5 6 7 8 9 10] dup 3 [40 50 60 70]   putinterval
     [1 2 3 4 5 6 7 8 9 10] dup 6 [40 50 60 70]   putinterval
"""
# opstack : [ArrayValue([1, 2, 3, 40, 50, 60, 70, 8, 9, 10]), ArrayValue([1, 2, 3, 4, 5, 6, 40, 50, 60, 70])]

testinput12 = """
     [1 2 3 4 5 6] aload pop add add add add add 21 eq
"""
# opstack : [True]

testinput13 = """
     1 2 3 4 5 6 [0 0 0 0] astore 
"""
# opstack : [1, 2, ArrayValue([3, 4, 5, 6])]

# Postscript examples that use stack manipulation operators. 
 
testinput14 = """
     [1 2 3 4] dup /arr exch def 
     [1 2 3 4] arr eq
"""
# opstack : [ArrayValue([1, 2, 3, 4]), False]

testinput15 = """
     1 2 3 4 5 3 copy count 
"""
# opstack : [1, 2, 3, 4, 5, 3, 4, 5, 8]

testinput16 = """
     1 2 3 4 5 6 7 8 9 7 4 roll
"""
# opstack : [1, 2, 6, 7, 8, 9, 3, 4, 5]

testinput17 = """
     1 2 3 4 5 6 7 8 9 7 -4 roll
"""
# opstack : [1, 2, 7, 8, 9, 3, 4, 5, 6]

testinput18 = """
    /isNeg { 0 lt } def  -5 dup isNeg { -1 mul } if
"""
# opstack : [5]

testinput19 = """
    /isNeg { 0 lt } def  -1 dup isNeg { -2 mul } { 3 mul} ifelse
"""
#opstack : [2]

testinput20 = """
    1 8 {2 mul } repeat 
"""
#opstack : [256]

testinput21 = """
    [1 2 3 4] {dup mul } forall
"""
#opstack : [1, 4, 9, 16]

testinput22 = """
    /arr [1 2 3 4] def arr {dup mul } forall arr astore pop arr
"""
#opstack : [ArrayValue([1, 4, 9, 16])]

testinput23 = """
    /x 4 def 
    /square {dup mul} def
    [x 1 x sub 1] /arr exch def  
    arr 1 1 getinterval aload pop dup
    0 gt 
    {2 mul} {square} ifelse
"""
#opstack : [9]

testinput24 = """
    /x 10 def
    /y 20 def
    /x 0 def
    /y 2 def
    5 { x y add /x exch def } repeat 
    x
"""
#opstack : [10]

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
#opstack : [10, 3, 10, 20, 1, 2]

testinput26 = """
        1 2 3 4 5  15 5 { exch sub} repeat 0 eq
"""
# opstack: [True]
   
testinput27 = """
    [1 2 3 4] {2 mod 0 eq} forall 
        {
            { /x 1 def }
            { /x 10 def }
            ifelse
        } if
    x
"""
# opstack : [False, True, 10]

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
# opstack : [120]

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
# opstack : [720]

testinput30 = """        
        /sumArray {0 exch aload pop count n sub {add} repeat } def
        /x 5 def
        /y 10 def
        /n 1 def
        [x y x y add] sumArray
"""
# opstack : [30]

testinput31 = """
    [ 1 2 3 4 5 6 7 8 9 ] 6 3 getinterval aload pop
    [ 7 8 9 1 2 3 4 5 6 ] 0 3 getinterval aload pop
    /x exch def /y exch def /z exch def
    x eq count 1 roll y eq count 1 roll z eq count 1 roll
"""
# opstack : [True, True, True]

tests = [testinput1,testinput2,testinput3,testinput4,testinput5,testinput6,testinput7,testinput8,testinput9,testinput10,
         testinput11,testinput12,testinput13,testinput14,testinput15,testinput16,testinput17,testinput18,testinput19,testinput20,
         testinput21,testinput22,testinput23,testinput24,testinput25,testinput26,testinput27,testinput28,testinput29,testinput30,testinput31]

parse_output = {
    'test1': [Literal(10), Literal(-2), Name('add'), Literal(5), Name('sub'), Literal(2), Name('mul'), Literal(20), Literal(3), Name('mod')], 
    'test2': [Literal(10), Literal(20), Name('lt'), Literal(20), Literal(15), Name('gt'), Array([Literal(1), Literal(2), Literal(3), Literal(4)]), Array([Literal(1), Literal(2), Literal(3), Literal(4)]), Name('eq'), Array([Literal(1), Literal(2), Literal(3), Literal(4)]), Name('dup'), Name('eq')], 
    'test3': [Name('/x'), Literal(1), Name('def'), Name('x'), Name('/x'), Literal(10), Name('def'), Name('x')], 
    'test4': [Name('/x'), Literal(1), Name('def'), Literal(1), Name('dict'), Name('begin'), Name('/x'), Literal(10), Name('def'), Name('x'), Name('end'), Name('x')], 
    'test5': [Name('/x'), Literal(1), Name('def'), Literal(1), Name('dict'), Name('begin'), Name('/x'), Literal(10), Name('def'), Literal(1), Name('dict'), Name('begin'), Name('/x'), Literal(100), Name('def'), Name('x'), Name('end'), Name('x'), Name('end'), Name('x')], 
    'test6': [Name('/x'), Literal(1), Name('def'), Name('/y'), Literal(2), Name('def'), Literal(1), Name('dict'), Name('begin'), Name('/x'), Literal(10), Name('def'), Literal(1), Name('dict'), Name('begin'), Name('/x'), Literal(100), Name('def'), Name('y'), Name('end'), Name('y'), Name('end')], 
    'test7': [Name('/x'), Literal(3), Name('def'), Name('/y'), Literal(4), Name('def'), Array([Literal(1), Literal(2), Name('x'), Name('x'), Literal(1), Name('add'), Literal(5), Name('x'), Name('x'), Name('add'), Name('x'), Name('y'), Name('add')])], 
    'test8': [Name('/x'), Literal(3), Name('def'), Name('/y'), Literal(4), Name('def'), Array([Literal(1), Literal(2), Name('x'), Name('x'), Literal(1), Name('add'), Literal(5), Array([Name('x'), Name('x'), Name('add'), Name('x'), Name('y')]), Array([Literal(True)])])], 
    'test9': [Array([Literal(1), Literal(2), Literal(3), Literal(4)]), Name('length'), Array([Literal(1), Literal(2), Literal(3), Array([Literal(4), Literal(5)]), Literal(6), Array([Literal(True)])]), Name('length')], 
    'test10': [Array([Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(6), Literal(7), Literal(8), Literal(9), Literal(10)]), Literal(3), Literal(3), Name('getinterval'), Array([Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(6), Literal(7), Literal(8), Literal(9), Literal(10)]), Literal(7), Literal(3), Name('getinterval')], 
    'test11': [Array([Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(6), Literal(7), Literal(8), Literal(9), Literal(10)]), Name('dup'), Literal(3), Array([Literal(40), Literal(50), Literal(60), Literal(70)]), Name('putinterval'), Array([Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(6), Literal(7), Literal(8), Literal(9), Literal(10)]), Name('dup'), Literal(6), Array([Literal(40), Literal(50), Literal(60), Literal(70)]), Name('putinterval')], 
    'test12': [Array([Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(6)]), Name('aload'), Name('pop'), Name('add'), Name('add'), Name('add'), Name('add'), Name('add'), Literal(21), Name('eq')], 
    'test13': [Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(6), Array([Literal(0), Literal(0), Literal(0), Literal(0)]), Name('astore')], 
    'test14': [Array([Literal(1), Literal(2), Literal(3), Literal(4)]), Name('dup'), Name('/arr'), Name('exch'), Name('def'), Array([Literal(1), Literal(2), Literal(3), Literal(4)]), Name('arr'), Name('eq')], 
    'test15': [Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(3), Name('copy'), Name('count')], 
    'test16': [Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(6), Literal(7), Literal(8), Literal(9), Literal(7), Literal(4), Name('roll')], 
    'test17': [Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(6), Literal(7), Literal(8), Literal(9), Literal(7), Literal(-4), Name('roll')], 
    'test18': [Name('/isNeg'), Block([Literal(0), Name('lt')]), Name('def'), Literal(-5), Name('dup'), Name('isNeg'), Block([Literal(-1), Name('mul')]), Name('if')], 
    'test19': [Name('/isNeg'), Block([Literal(0), Name('lt')]), Name('def'), Literal(-1), Name('dup'), Name('isNeg'), Block([Literal(-2), Name('mul')]), Block([Literal(3), Name('mul')]), Name('ifelse')], 
    'test20': [Literal(1), Literal(8), Block([Literal(2), Name('mul')]), Name('repeat')], 
    'test21': [Array([Literal(1), Literal(2), Literal(3), Literal(4)]), Block([Name('dup'), Name('mul')]), Name('forall')], 
    'test22': [Name('/arr'), Array([Literal(1), Literal(2), Literal(3), Literal(4)]), Name('def'), Name('arr'), Block([Name('dup'), Name('mul')]), Name('forall'), Name('arr'), Name('astore'), Name('pop'), Name('arr')], 
    'test23': [Name('/x'), Literal(4), Name('def'), Name('/square'), Block([Name('dup'), Name('mul')]), Name('def'), Array([Name('x'), Literal(1), Name('x'), Name('sub'), Literal(1)]), Name('/arr'), Name('exch'), Name('def'), Name('arr'), Literal(1), Literal(1), Name('getinterval'), Name('aload'), Name('pop'), Name('dup'), Literal(0), Name('gt'), Block([Literal(2), Name('mul')]), Block([Name('square')]), Name('ifelse')], 
    'test24': [Name('/x'), Literal(10), Name('def'), Name('/y'), Literal(20), Name('def'), Name('/x'), Literal(0), Name('def'), Name('/y'), Literal(2), Name('def'), Literal(5), Block([Name('x'), Name('y'), Name('add'), Name('/x'), Name('exch'), Name('def')]), Name('repeat'), Name('x')], 
    'test25': [Name('/x'), Literal(1), Name('def'), Name('/y'), Literal(2), Name('def'), Literal(1), Name('dict'), Name('begin'), Name('/x'), Literal(10), Name('def'), Literal(1), Name('dict'), Name('begin'), Name('/y'), Literal(3), Name('def'), Name('x'), Name('y'), Name('end'), Name('/y'), Literal(20), Name('def'), Name('x'), Name('y'), Name('end'), Name('x'), Name('y')], 
    'test26': [Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(15), Literal(5), Block([Name('exch'), Name('sub')]), Name('repeat'), Literal(0), Name('eq')], 
    'test27': [Array([Literal(1), Literal(2), Literal(3), Literal(4)]), Block([Literal(2), Name('mod'), Literal(0), Name('eq')]), Name('forall'), Block([Block([Name('/x'), Literal(1), Name('def')]), Block([Name('/x'), Literal(10), Name('def')]), Name('ifelse')]), Name('if'), Name('x')], 
    'test28': [Name('/n'), Literal(5), Name('def'), Name('/fact'), Block([Literal(0), Name('dict'), Name('begin'), Name('/n'), Name('exch'), Name('def'), Name('n'), Literal(2), Name('lt'), Block([Literal(1)]), Block([Name('n'), Literal(1), Name('sub'), Name('fact'), Name('n'), Name('mul')]), Name('ifelse'), Name('end')]), Name('def'), Name('n'), Name('fact')], 
    'test29': [Name('/fact'), Block([Literal(0), Name('dict'), Name('begin'), Name('/n'), Name('exch'), Name('def'), Literal(1), Name('n'), Block([Name('n'), Name('mul'), Name('/n'), Name('n'), Literal(1), Name('sub'), Name('def')]), Name('repeat'), Name('end')]), Name('def'), Literal(6), Name('fact')], 
    'test30': [Name('/sumArray'), Block([Literal(0), Name('exch'), Name('aload'), Name('pop'), Name('count'), Name('n'), Name('sub'), Block([Name('add')]), Name('repeat')]), Name('def'), Name('/x'), Literal(5), Name('def'), Name('/y'), Literal(10), Name('def'), Name('/n'), Literal(1), Name('def'), Array([Name('x'), Name('y'), Name('x'), Name('y'), Name('add')]), Name('sumArray')], 
    'test31': [Array([Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(6), Literal(7), Literal(8), Literal(9)]), Literal(6), Literal(3), Name('getinterval'), Name('aload'), Name('pop'), Array([Literal(7), Literal(8), Literal(9), Literal(1), Literal(2), Literal(3), Literal(4), Literal(5), Literal(6)]), Literal(0), Literal(3), Name('getinterval'), Name('aload'), Name('pop'), Name('/x'), Name('exch'), Name('def'), Name('/y'), Name('exch'), Name('def'), Name('/z'), Name('exch'), Name('def'), Name('x'), Name('eq'), Name('count'), Literal(1), Name('roll'), Name('y'), Name('eq'), Name('count'), Literal(1), Name('roll'), Name('z'), Name('eq'), Name('count'), Literal(1), Name('roll')]}


expected_output= {
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
        'test31': [True, True, True]
}
# program start
if __name__ == '__main__':
    
    psstacks = Operators()  
    testnum = 1
    for testcase in tests:
        print("--------------------------------------------------------")
        try:
            expr_list = read(testcase)
            for expr in expr_list:
                expr.evaluate(psstacks)
            print("--test {}--".format(testnum))
            testnum += 1
            print('opstack:\n', psstacks.opstack)
            # print('dictstack:\n ' , psstacks.dictstack)
        except (SyntaxError, NameError, TypeError, Exception) as err:
            print(type(err).__name__ + ':', err)
        psstacks.clearBoth()