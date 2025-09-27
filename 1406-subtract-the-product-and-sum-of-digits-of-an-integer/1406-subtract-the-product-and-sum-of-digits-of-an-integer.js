/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let product = 1
    let sum = 0 
    for(let digit of n.toString()) {
        let d = parseInt(digit)
        product *= d
        sum += d
    }
    return product - sum
};