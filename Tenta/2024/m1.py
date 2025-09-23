'''
Module 1: A1, A2, B1
Exam on 2024-10-29
'''

def A1(n): 
    """ A1: complete the function """
    def _A1(n,memory={0:1, 1:1, 2:1, 3:1, 4:0}):
        if n in memory:
            return memory[n]
        else:
            res = 2*_A1(n-1, memory) - 4*_A1(n-2, memory) + 3*_A1(n-3, memory) -_A1(n-4, memory)
            memory[n] = res
            return res
    return _A1(n)

    
def A2(input_string: str) -> bool:
    """ A2: write your solution for A2"""
    input_string = input_string.lower()
    def _A2(string):
        if len(string) < 2:
            return False
        else:
            return string[0] == string[-1] or _A2(string[0:-1])
    return _A2(input_string)

def B1(lst):
    # Base case: empty list
    if not lst:
        return ([], [])
    # Base case: one element left
    if len(lst) == 1:
        return ([lst[0]], [])
    
    # Recursive step: split off first two elements
    even_rest, odd_rest = B1(lst[2:])
    return ([lst[0]] + even_rest, [lst[1]] + odd_rest)


if __name__ == '__main__':
    print(A1(10))
    print(A1(90))
    print(A1(200))

    test = "AbcbA"
    print(test)
    print(test[1:-1])

    print(A2("racecar"))
    print(A2("Realisationsvinstbeskattning"))
    print(A2("madam"))
    
    lists = ([],
             [0],
             [0, 1],
             [0, 1, 2],
             [0, 1, 2, 3],
             [0, 1, 2, 3, 4]
             )
    for lst in lists:
        print(f'{str(lst):15s} \t {B1(lst)}')