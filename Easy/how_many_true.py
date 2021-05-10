''' 
    Create a function which returns the number of True values in a list.
    
    Example:
        count_true([True, False, False, True, False]) ➞ 2

        count_true([False, False, False, False]) ➞ 0

        count_true([]) ➞ 0
'''

def count_true(lst):
	return sum([1 for x in lst if x == True]) if lst else 0