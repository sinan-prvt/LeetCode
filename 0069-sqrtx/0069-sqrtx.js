/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if(x < 2) return x
     let a = 1, b = Math.floor(x / 2);

    while (a <= b) {
        let mid = Math.floor((a + b) / 2);
        let square = mid * mid;

        if (square === x) {
            return mid;
        } else if (square < x) {
            a = mid + 1;
        } else {
            b = mid - 1;
        }
    }

    return b;
};