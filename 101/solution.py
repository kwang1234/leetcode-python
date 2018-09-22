#  Two Sum
#  Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
    visited = {}
    idx1=idx2=0
    for idx,val in enumerate(nums):
        v1, idx1 = val, idx
        v2 = target - v1
        if v2 in visited:
            idx2 = visited[v2]
            break
        else:
            visited[val] = idx
    return [idx2, idx1] if nums[idx1] + nums[idx2] == target else None

n = [2, 7, 11, 15]
n1 = [-3,4,3,90]
t1 = 0
target = 9
print(twoSum(n1, t1))

        
        



