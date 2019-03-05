/**
 * @param {number} n
 * @return {number}
 */
var getMoneyAmount = function(n) {
  const tabulation = [];
  for (let i = 0; i <= n; i++) {
    tabulation.push(Array.from({ length: n + 1 }).fill(0));
  }
  for (let lowVal = n; lowVal > 0; lowVal--) {
    for (let highVal = lowVal + 1; highVal <= n; highVal++) {
      let bestCost = Infinity;
      for (let guess = lowVal; guess < highVal; guess++) {
        const worstSubCost = Math.max(
          tabulation[lowVal][guess - 1],
          tabulation[guess + 1][highVal]
        );
        let cost = guess + worstSubCost;
        bestCost = Math.min(cost, bestCost);
      }
      tabulation[lowVal][highVal] = bestCost;
    }
  }
  return tabulation[1][n];
};

module.exports = getMoneyAmount;
