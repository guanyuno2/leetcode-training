#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# solution 2: using Hash map
# using hashmap to store all indicates previous index
# [value] = index
# result: existed (target - value[i]) && that value != i 

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        my_dict = {}
        for index, value in enumerate(nums):
            if(my_dict.get(value) is None):
                my_dict[value] = index
            if (my_dict.get(target - value) is not None and my_dict.get(target - value) != index):
                return [my_dict.get(target - value), index]
        
        return []
        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.twoSum([2,7,11,15], 9)
    print("Result:", result)