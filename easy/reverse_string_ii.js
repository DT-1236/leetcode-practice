/**
 * @description Reverses num characters of string. Reverses all if string length is fewer than num
 * Runtime: 68 ms, faster than 70.88% of JavaScript online submissions for Reverse String II.
 * Memory Usage: 38.3 MB, less than 12.50% of JavaScript online submissions for Reverse String II.
 * @param {string} string Input string
 * @param {number} num Number of leading characters to reverse
 * @return {string} Reversed string
 */
var reverseStr = function(string, num) {
  let output = '';
  let pointer = 0;
  while (pointer < string.length) {
    let fragment = '';
    for (let i = 0; i < num && pointer < string.length; i++, pointer++) {
      fragment = string[pointer] + fragment;
    }
    output += fragment;
    fragment = '';
    for (let i = 0; i < num && pointer < string.length; i++, pointer++) {
      fragment += string[pointer];
    }
    output += fragment;
  }
  return output;
};
