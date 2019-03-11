/**
 * @description Takes n and returns an array of all valid parenthesis permutations. Uses memoization to store old parenthesis sets
 * Assumes that all new parenthesis configurations can be accounted by `${left}(${mid})${right}`
 * That is, if all permutations of previous parenthesis configurations are placed to the left, middle, and right of a new set of parenthesis, then all new configurations will have been made
 * @param {number} n Number of parenthesis pairs
 * @return {string[]}
 */
var generateParenthesis = function(n) {
  // Contains sets of all known configurations a number of paren pairs
  // Base cases are known - empty string for no pairs, and a plain '()' for a single pair
  const tabArray = [new Set(['']), new Set(['()'])];
  //   Slowly build up to the target number of pairs
  for (let totalPrevPairs = 1; totalPrevPairs < n; totalPrevPairs++) {
    const newCombinations = new Set();

    // Start by going all-in on the left side of the new parens
    for (let outsideNum = totalPrevPairs; outsideNum >= 0; outsideNum--) {
      // This will end up being zero first, but will grow as the left shrinks
      const insideNum = totalPrevPairs - outsideNum;
      const outsideSet = tabArray[outsideNum];
      const insideSet = tabArray[insideNum];

      // Add a new string for each permutation of inside and outside parens
      outsideSet.forEach(outside =>
        insideSet.forEach(inside =>
          newCombinations.add(`(${inside})${outside}`)
        )
      );
    }

    // Add a new entry to the tabArray
    tabArray[totalPrevPairs + 1] = newCombinations;
  }
  // tabArray[n] should have the last set, or the set pertaining to n pairs
  // The array is sorted to match LeetCode test cases
  return Array.from(tabArray[n]).sort();
};

module.exports = generateParenthesis;
