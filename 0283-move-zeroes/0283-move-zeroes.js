/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let zero = 0
    for(let i=0; i< nums.length; i++) {
        if(nums[i] !== 0) {
            nums[zero] = nums[i]
            zero++
        }
    }
    for(let i = zero; i < nums.length; i++) {
        nums[i] = 0
    }
};