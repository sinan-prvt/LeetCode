/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    let freq = {}

    for(let char of s) {
        freq[char] = (freq[char] || 0) + 1
    }

    for(let i = 0; i < s.length; i++) {
        if(freq[s[i]] === 1) {
            return i
        }
    }
    return -1
};