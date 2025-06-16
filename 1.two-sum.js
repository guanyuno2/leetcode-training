/*
 * @lc app=leetcode id=1 lang=javascript
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// create hashtable to store
// key: value of nums
// value: index
// if exists key: (target - nums[i]) then you got the result

var twoSum = function (nums, target) {
    var hashTable = {};
    for (var i = 0; i < nums.length - 1; i++) {
        // if exist key 
        if (hashTable[nums[i]]) {
            hashTable[nums[i]].push(i)
        }
        else {
            hashTable[nums[i]] = [i]
        }

        // for exp: (9-2) = 7
        // but 7 existed in hashtable before => 
        // return result: index of 7 and current index
        var prev = hashTable[target - nums[i]]
        if (prev) {
            return [prev, i]
        }
    }
    return []
};
// @lc code=end

