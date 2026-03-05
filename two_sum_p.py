'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
 
 
 Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
'''
'''
# with O(n2) complexity solution.
def get_indexes(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[j] + nums[i] == target:
                return [i, j]
    else:
        print("We didn't found bro indexes")

nums = [6, 3, 4, 8, 2, 19, 2, 3, 2]   
target = 9 
print(get_indexes(nums, target))
'''
# with O(1) complexity
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the complement and its index
        # Key: number needed (complement), Value: index of the current number
        seen_nums = {}

        for i, num in enumerate(nums): # num 6, 3
            complement = target - num    #  comp 3, 6
            if complement in seen_nums:  # 
                # If the complement is already in the dictionary, we found the pair
                return [seen_nums[complement], i]
            
            # Otherwise, store the current number and its index for future lookups
            seen_nums[num] = i   # seen_nums {'6':0}
        
        # According to the problem statement, there is always exactly one solution,
        # so this part of the code is unreachable in a standard Two Sum problem scenario.
        return []

nums = [6, 3, 8, 2, 19, 2, 2]   
target = 9 
solution_obj = Solution()
indexes = solution_obj.twoSum(nums, target)
print(indexes)
