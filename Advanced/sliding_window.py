nums = [1,3,-1,-3,5,3,6,7]
k = 3


def sliding_window():
    return [max(nums[x:x+3]) for x in range(len(nums) - 2)]
    
print(sliding_window())