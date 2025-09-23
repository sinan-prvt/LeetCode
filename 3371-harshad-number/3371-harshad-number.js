/**
 * @param {number} x
 * @return {number}
 */
var sumOfTheDigitsOfHarshadNumber = function(x) {
    let digitSum = x
        .toString()
        .split("")
        .reduce((sum, d) => sum + parseInt(d), 0)
    return x % digitSum === 0 ? digitSum : -1
};