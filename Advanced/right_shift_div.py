''' 
    The right shift operation is similar to floor division by powers of two.
    Sample calculation using the right shift operator ( >> ):
    
    Example:
        80 >> 3 = floor(80/2^3) = floor(80/8) = 10
        -24 >> 2 = floor(-24/2^2) = floor(-24/4) = -6
        -5 >> 1 = floor(-5/2^1) = floor(-5/2) = -3
        
    Notes:
        There will be no negative values for the second parameter y.
        This challenge is more like recreating of the right shift operation, thus, the use of the operator directly is prohibited.
        Alternatively, you can solve this challenge via recursion
'''

def shift_to_right(x, y):
	return x//2**y