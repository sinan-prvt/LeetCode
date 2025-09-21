/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    const freq = {}
    let length = 0
    let oddFound = false
    for(let char of s) {
        freq[char] = (freq[char] || 0) + 1
    }
    for(let count of Object.values(freq)) {
    length += Math.floor(count / 2) * 2; 
    if (count % 2 === 1) oddFound = true;
  }
  return oddFound ? length + 1 : length;
};