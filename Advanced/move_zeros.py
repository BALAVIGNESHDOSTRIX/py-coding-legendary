''' 
    Create a function that takes a list lst of numbers and moves all zeros to the end, preserving the order of the other elements.
    Examples:
        move_zeros([1, 0, 1, 2, 0, 1, 3]) ➞ [1, 1, 2, 1, 3, 0, 0]

        move_zeros([0, 1, None, 2, false, 1, 0]) ➞ [1, None, 2, false, 1, 0, 0]

        move_zeros(['a', 0, 0, 'b', 'c', 'd', 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) ➞ ['a', 'b', 'c', 'd', 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        ['a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] should equal 

['a', 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
['a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

def move_zeros(lst):
    zero = []
    newl = []
    for x in lst:
        if isinstance(x, bool):
            newl.append(x)
        elif x == 0:
            zero.append(0)
        else:
            newl.append(x)
    return newl+zero


print(move_zeros(['a', 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        