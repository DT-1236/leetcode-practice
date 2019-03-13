/**
 * @param {number[]} prices Array of unsorted numbers representing stock prices over time
 * @return {number} Maximum profit for given stock price array
 */
var maxProfit = function(prices) {
  let best = 0;
  let localMin = Infinity;
  let localMax = -Infinity;
  prices.forEach(price => {
    if (price < localMin) {
      best = Math.max(localMax - localMin, best);
      localMin = price;
      localMax = price;
    } else {
      localMax = Math.max(price, localMax);
    }
  });
  return Math.max(localMax - localMin, best);
};
