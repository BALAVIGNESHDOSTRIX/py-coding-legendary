''' 
    Create a function that takes a number num and returns its length.
    
    Example:
        number_length(10) ➞ 2

        number_length(5000) ➞ 4

        number_length(0) ➞ 1
        
    The use of the len() function is prohibited.
'''

def number_len(num):
    count = 0
    if num == 0:
        count += 1
    while num > 0:
        num = num // 10
        count += 1
    return count 
    
number_len(0)