#Brandon Henry#
from psItems import Value, ArrayValue, FunctionValue
from psParser import is_literal
class Operators:
    def __init__(self):
        #stack variables
        self.opstack = []  #assuming top of the stack is the end of the list
        self.dictstack = []  #assuming top of the stack is the end of the list
        
        #The builtin operators supported by our interpreter
        self.builtin_operators = {
            
            "add":self.add,
            "sub":self.sub,
            "mul":self.mul,
            "mod":self.mod,
            "eq":self.eq,
            "lt":self.lt,
            "gt":self.gt,
            "length":self.length,
            "getinterval":self.getinterval,
            "putinterval":self.putinterval,
            "aload":self.aload,
            "astore":self.astore,
            "pop":self.pop,
            "stack":self.stack,
            "dup":self.dup,
            "count":self.count,
            "clear":self.clear,
            "copy":self.copy,
            "exch":self.exch,
            "roll":self.roll,
            "dict":self.psDict,
            "begin":self.begin,
            "end":self.end,
            "def":self.psDef,
            "if":self.psIf,
            "ifelse":self.psIfelse,
            "repeat":self.repeat,
            "forall":self.forall
             # include the key value pairs where he keys are the PostScrip opertor names and the values are the function values that implement that operator. 
             # Make sure **not to call the functions** 
        }
    #-------  Operand Stack Operators --------------
    """
        Helper function. Pops the top value from opstack and returns it.
    """
    def opPop(self):
        if len(self.opstack) > 0:
            return self.opstack.pop()
        else:
            print("error opstack too small for opPop")

    """
       Helper function. Pushes the given value to the opstack.
    """
    def opPush(self,value):
        self.opstack.append(value)
        
    #------- Dict Stack Operators --------------
    
    """
       Helper function. Pops the top dictionary from dictstack and returns it.
    """   
    def dictPop(self):
        if len(self.dictstack) > 0:
            return self.dictstack.pop()
        else:
            print("error dictstack too small for dictPop")

    """
       Helper function. Pushes the given dictionary onto the dictstack. 
    """   
    def dictPush(self,d):
        if self.dictstack != []:
            if self.dictstack[-1] == {}:
               self.dictstack[-1] = d
            elif d == {}:
                self.dictstack.append({})
            else:
                for key,item in d.items():
                    self.dictstack[-1][key] = item
        else:
            self.dictstack.append({})

    """
       Helper function. Adds name:value pair to the top dictionary in the dictstack.
       (Note: If the dictstack is empty, first adds an empty dictionary to the dictstack then adds the name:value to that. 
    """   
    def define(self,name, value):
        if len(self.dictstack) == 0: 
            self.dictPush({})
            self.dictstack[0] = {name:value}
        else:
            self.dictPush({name:value})

    """
       Helper function. Searches the dictstack for a variable or function and returns its value. 
       (Starts searching at the top of the dictstack; if name is not found returns None and prints an error message.
        Make sure to add '/' to the begining of the name.)
    """
    def lookup(self,name):
        savedstack = self.dictstack.copy()
        name  = '/' + name
        while not(savedstack == []):
            
            if name in savedstack[-1]:
                endresult = savedstack[-1][name]
                savedstack = self.dictstack
                return endresult 
            else:
                savedstack.pop()

        
    #------- Arithmetic Operators --------------
    
    """
       Pops 2 values from opstack; checks if they are numerical (int); adds them; then pushes the result back to opstack. 
    """   
    def add(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op1 + op2)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: add expects 2 operands")
 
    """
       Pop 2 values from opstack; checks if they are numerical (int); subtracts them; and pushes the result back to opstack. 
    """   
    def sub(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op2 - op1)
            else:
                print("Error: sub - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: sub expects 2 operands")

    """
        Pops 2 values from opstack; checks if they are numerical (int); multiplies them; and pushes the result back to opstack. 
    """    
    def mul(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op1 * op2)
            else:
                print("Error: mul - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: mul expects 2 operands")

    """
        Pops 2 values from stack; checks if they are int values; calculates the remainder of dividing the bottom value by the top one; 
        pushes the result back to opstack.
    """ 
    def mod(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op2 % op1)
            else:
                print("Error: mod - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: add expects 2 operands")
    #---------- Comparison Operators  -----------------
    """
       Pops the top two values from the opstack; pushes "True" is they are equal, otherwise pushes "False"
    """ 
    def eq(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,type(op1)) and isinstance(op2,type(op2)):
                self.opPush(op1 == op2)
            else:
                print("Error: eq - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: eq expects 2 operands")

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is less than the top value, otherwise pushes "False"
    """ 
    def lt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,type(op1)) and isinstance(op2,type(op2)):
                self.opPush(op2 < op1)
            else:
                print("Error: lt - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: lt expects 2 operands")

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is greater than the top value, otherwise pushes "False"
    """ 
    def gt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,type(op1)) and isinstance(op2,type(op2)):
                self.opPush(op2 > op1)
            else:
                print("Error: gt - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: gt expects 2 operands")

    # ------- Array Operators --------------
    """ 
       Pops an array value from the operand opstack and calculates the length of it. Pushes the length back onto the opstack.
       The `length` method should support ArrayValue values.
    """
    def length(self):
        if len(self.opstack) > 0:
                templist = self.opPop()
                counter = len(templist.value) 
                self.opPush(counter)    
        else:
            self.opPush(0)    
    """ 
        Pops the `count` (int), an (zero-based) start `index`, and an array constant (ArrayValue) from the operand stack.  
        Pushes the slice of the array of length `count` starting at `index` onto the opstack.(i.e., from `index` to `index`+`count`) 
        If the end index of the slice goes beyond the array length, will give an error. 
    """
    def getinterval(self):
        index_end = self.opPop() 
        count_val = self.opPop()
        index_end = index_end + count_val
        array_val = self.opPop()
        saved_array = array_val.value.copy()
        array_val.value = []
       
        for item in range(count_val,index_end):
            array_val.value.append(saved_array[count_val])
            count_val = count_val + 1
        
        self.opPush(array_val)

    """ 
        Pops an array constant (ArrayValue), start `index` (int), and another array constant (ArrayValue) from the operand stack.  
        Replaces the slice in the bottom ArrayValue starting at `index` with the top ArrayValue (the one we popped first). 
        The result is not pushed onto the stack.
        The index is 0-based. If the end index of the slice goes beyond the array length, will give an error. 
    """
    def putinterval(self):
        array1 = self.opPop()
        index_start = self.opPop()
        array2 = self.opPop()
        it = 0
        while not(it == (len(array1.value))):
            array2.value[index_start] = array1.value[it]
            index_start= index_start + 1
            it = it + 1

    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pushes all values in the array constant to the opstack in order (the first value in the array should be pushed first). 
        Pushes the orginal array value back on to the stack. 
    """
    def aload(self):
        temparray = self.opPop()
        for item in range(len(temparray.value)):
            self.opPush(temparray.value[item])
        self.opPush(temparray)
    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pops as many elements as the length of the array from the operand stack and stores them in the array constant. 
        The value which was on the top of the opstack will be the last element in the array. 
        Pushes the array value back onto the operand stack. 
    """
    def astore(self):
        temparray = self.opPop()
        for item in range(len(temparray.value)):
            temparray.value[item] = self.opPop()
        temparray_val = temparray.value
        temparray_val.reverse()
        self.opPush(temparray)

    #------- Stack Manipulation and Print Operators --------------

    """
       This function implements the Postscript "pop operator". Calls self.opPop() to pop the top value from the opstack and discards the value. 
    """
    def pop (self):
        return self.opPop()
    

    """
       Prints the opstack. The end of the list is the top of the stack. 
    """
    def stack(self):
        if len(self.opstack) > 0:
            val = -1
            for val in range(len(self.opstack)):
                print(self.opstack[(val)])
                val = val -1

    """
       Copies the top element in opstack.
    """
    def dup(self):
        if len(self.opstack) > 0:
            self.opPush(self.opstack[-1])
        else:
            print("error empty stack")
    """
       Pops an integer count from opstack, copies count number of values in the opstack. 
    """
    def copy(self):
        num_elem = self.opPop()
        position = -1
        copied_elem = []
        while num_elem > 0:
            copied_elem.append(self.opstack[position])
            num_elem = num_elem - 1
            position = position -1
        while not(copied_elem == []):
            self.opstack.append(copied_elem.pop())
    """
        Counts the number of elements in the opstack and pushes the count onto the top of the opstack.
    """
    def count(self):
        self.opPush(len(self.opstack))

    """
       Clears the opstack.
    """
    def clear(self):
        while len(self.opstack) > 0:
            self.opPop()
        
    """
       swaps the top two elements in opstack
    """
    def exch(self):
        op1 = self.opPop()
        op2 = self.opPop()
        self.opPush(op1)
        self.opPush(op2)

    """
        Implements roll operator.
        Pops two integer values (m, n) from opstack; 
        Rolls the top m values in opstack n times (if n is positive roll clockwise, otherwise roll counter-clockwise)
    """
    def roll(self):
        times = self.opPop()
        size = self.opPop()
        roll_list = []
        while size > 0:
            roll_list.append(self.opPop())
            size = size -1
        roll_list.reverse()
        new_list = []
        if times > 0:
            while times > 0:
                new_list.append(roll_list.pop())

                times = times - 1
            roll_list.reverse()
            new_list.reverse()
            while not(roll_list == []):
                new_list.append(roll_list.pop())
            new_list.reverse()
            while not(new_list == []):
                self.opstack.append(new_list.pop())
        else:
            roll_list.reverse()
            while times < 0:
                new_list.append(roll_list.pop())
                times = times + 1
            new_list.reverse()
            roll_list.reverse()
            while not(new_list == []):
                roll_list.append(new_list.pop())
            roll_list.reverse()
            while not(roll_list == []):
                self.opstack.append(roll_list.pop())
    """
       Pops an integer from the opstack (size argument) and pushes an  empty dictionary onto the opstack.
    """
    def psDict(self):
        size = self.opPop()
        if size == 0:
            self.opPush({})
        while size > 0:
            self.opPush({})
            size = size - 1
    """
       Pops the dictionary at the top of the opstack; pushes it to the dictstack.
    """
    def begin(self):
        self.dictPush(self.opPop())
        

    """
       Removes the top dictionary from dictstack.
    """
    def end(self):
        self.dictPop()
        
    """
       Pops a name and a value from opstack, adds the name:value pair to the top dictionary by calling define.  
    """
    def psDef(self):
        value = self.opPop()
        name = self.opPop()
        self.define(name,value)


    # ------- if/ifelse Operators --------------
    """
       Implements if operator. 
       Pops the `ifbody` and the `condition` from opstack. 
       If the condition is True, evaluates the `ifbody`.  
    """
    def psIf(self):
        ifbody = self.opPop()
        condition = self.opPop()
        if type(condition) != bool:
            condition = condition.apply(self)
        if condition:
            ifbody.apply(self)

        # TO-DO in part2

    """
       Implements ifelse operator. 
       Pops the `elsebody`, `ifbody`, and the condition from opstack. 
       If the condition is True, evaluate `ifbody`, otherwise evaluate `elsebody`. 
    """
    def psIfelse(self):
        elsebody = self.opPop()
        ifbody = self.opPop()
        condition = self.opPop()
        if type(condition) != bool:
            condition = condition.apply(self)
            condition = self.opPop()
        
        if condition:
            ifbody.apply(self)
        else:
            elsebody.apply(self)
        # TO-DO in part2


    #------- Loop Operators --------------
    """
       Implements repeat operator.   
       Pops the `loop_body` (FunctionValue) and loop `count` (int) arguments from opstack; 
       Evaluates (applies) the `loopbody` `count` times. 
       Will be completed in part-2. 
    """  
    def repeat(self):
        loop_body = self.opPop()
        count = self.opPop()
        while count > 0:
            loop_body.apply(self)
            count = count -1
        #TO-DO in part2
        
    """
       Implements forall operator.   
       Pops a `codearray` (FunctionValue) and an `array` (ArrayValue) from opstack; 
       Evaluates (applies) the `codearray` on every value in the `array`.  
       Will be completed in part-2. 
    """ 
    def forall(self):
        functval = self.opPop()
        arr = self.opPop()
        for elements in arr.value:
            self.opPush(elements)
            functval.apply(self)

            
        # TO-DO in part2

    #--- used in the setup of unittests 
    def clearBoth(self):
        self.opstack[:] = []
        self.dictstack[:] = []
    #needed for repl.py clears possible None on the stack
    def cleanTop(self): 
        if len(self.opstack)>1: 
            if self.opstack[-1] is None: 
                self.opstack.pop() 