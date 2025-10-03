"""
Solutions to module 4 - A calculator
Student: 
Mail:
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA4tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(arg)


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    #wtok.next()
    if not wtok.is_at_end():
        raise SyntaxError(f'Expected End of Line')
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if not wtok.is_name():
            raise SyntaxError('Excpected variable name')
        else:
            variables[wtok.get_current()] = result
            wtok.next()
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        elif wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
    return result

def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/':
        if  wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        elif wtok.get_current() == '/':
            wtok.next()
            denominator = factor(wtok, variables)
            if denominator == 0:
                raise EvaluationError(f'Cannot divide by zero')
            else:
                result = result / denominator
    return result

def power(x,e):
    if int(e) != e and x<0:
        raise EvaluationError(f'Complex  numbers not defined, cannot raise negative number to non-integer power: {x}^{e}')
    else:
        return math.pow(x,e)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def exp(x):
    return math.exp(x)

def log(x):
    if x <= 0:
        raise EvaluationError(f"log(x) is only defined for x>0")
    else:
        return math.log(x)

def fac(x):

    if x < 0 or int(x) != x: 
        raise EvaluationError(f"fac() is only defined for non-negative integers")
    else:
        return math.factorial(int(x))

def fib(x):
    if x < 0 or int(x) != x:
        raise EvaluationError(f'fib() is only defined for non-negative integers')
    else: 
        
        memory = {0:0, 1:1}
        
        def _fib_mem(n):
            if n not in memory:
                memory[n] = _fib_mem(n-1) + _fib_mem(n-2)
            return memory[n]
        
        return _fib_mem(x)

def max(args: list):
    return max(args)
    
def min(args: list):
    return min(args)

def mean(args: list):
    if len(args) == 0:
        raise EvaluationError('mean() requires at least one argument')
    else:
        return mean(args)

def sum(args):
    return sum(args)

def factor(wtok, variables):
    """ See syntax chart for factor"""
    function_1 = {'sin':sin, 'cos':cos, 'exp':exp, 'log':log, 'fac':fac, 'fib':fib}
    function_n = {'max':max, 'min':min, 'sum':sum, 'mean':mean}


    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
            
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    
    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok,variables)

    elif wtok.is_name():
        if wtok.get_current() == 'vars':
            print('-------------------------')
            print(f'Variable            Value')
            for i in variables:
                width = 20 - len(i)
                print(i + ' '*width + str(variables[i]))
            print('-------------------------')
            print()
            return

        elif wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()

        elif wtok.get_current() in function_1:
            wtok.next()
            if wtok.get_current() != '(':
                raise SyntaxError("Expected '(' after function defintion")
            else:
                result = function_1[wtok.get_previous()](factor(wtok,variables))
                
        elif wtok.get_current() in function_n:
            wtok.next()
            if wtok.get_current() != '(':
                raise SyntaxError("Expected '(' after function defintion")
            else:
                result = function_n[wtok.get_previous()](arglist(wtok,variables))

        else:
            raise EvaluationError(f'Expected defined function or existing variable')

    else:
        raise SyntaxError(
            "Expected number or '('")
    
    if wtok.get_current() == '**':
        wtok.next()
        exponent = factor(wtok, variables)
        result = power(result, exponent)
    return result

def arglist(wtok, variables):
    lst = []
    while wtok.get_current() != ')':
        lst.append(assignment(wtok, variables))
        wtok.next()
        if wtok.get_current() not in [',', ')']:
            raise SyntaxError('Argument should be followed by comma or paranthesis')
        if wtok.get_current() == ')':
            wtok.next()
            break
        wtok.next()
    return lst

    
         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA4init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except EvaluationError as ve:
                print("*** EvaluationError: ", ve)

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 


if __name__ == "__main__":
    main()
