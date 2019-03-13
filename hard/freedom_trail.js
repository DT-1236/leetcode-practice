/**
 * @param {string} ring String representing stock characters from which to make the key
 * @param {string} key String representing the key that needs to be made from the ring
 * @return {number} Moves needed to create the key from the ring
 */
function findRotateSteps(ring, key) {
  const indices = {};
  const costs = [];
  for (let i = 0; i < ring.length; i++) {
    if (indices[ring[i]]) indices[ring[i]].add(i);
    else indices[ring[i]] = new Set([i]);
    costs[i] = ringCost(i, 0, ring.length);
  }
  let prevChar = key[0];
  for (let currIdx = 1; currIdx < key.length; currIdx++) {
    const prevIndices = indices[prevChar];
    indices[key[currIdx]].forEach(idx => {
      let best = Infinity;
      // Each one of these indices needs to get updated in costs
      prevIndices.forEach(prev => {
        best = Math.min(best, ringCost(prev, idx, ring.length) + costs[prev]);
      });
      costs[idx] = best;
    });
    prevChar = key[currIdx];
  }
  let best = Infinity;
  indices[key.slice(-1)].forEach(idx => {
    best = Math.min(best, costs[idx]);
  });
  return best;
}

function ringCost(currIdx, prevIdx, length) {
  let lesser, greater;
  if (currIdx < prevIdx) {
    lesser = currIdx;
    greater = prevIdx;
  } else {
    lesser = prevIdx;
    greater = currIdx;
  }
  return Math.min(greater - lesser, lesser + (length - greater)) + 1;
}
