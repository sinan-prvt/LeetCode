/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let n = {}
    for(let num of nums){
        n[num] = (n[num] || 0) + 1
        if(n[num] > nums.length / 2) {
            return num
        }
    }
};