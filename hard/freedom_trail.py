from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """Keeps track of all paths using a single array representing the ring
        As each letter is used, all costs for that letter are updated with the best cost at that time
        >>> test = Solution()
        None
        >>> test("edcba", "abcde")
        10
        >>> test("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx")
        137
)
        """
        indices = defaultdict(set)
        for idx in range(0, len(ring)):
            indices[ring[idx]].add(idx)
        # Assign cost of every index to the cost of moving and assigning
        costs = [
            Solution.ring_cost(x, 0, len(ring))
            for x in range(0,
                           len(ring) + 0)
        ]
        print(costs)
        # Cycle through all subsequent characters in the key
        prev_char = key[0]
        for char in key[1:]:
            char_indices = indices[char]
            # Iterate all possible solutions
            # _i.e._ update costs for every position of the next character
            for c_idx in char_indices:
                # The update cost will be the best choice from the all previous positions
                costs[c_idx] = min(
                    Solution.ring_cost(c_idx, prev_idx, len(costs)) +
                    costs[prev_idx] for prev_idx in indices[prev_char])
            prev_char = char
        return min(costs[x] for x in indices[key[-1]])

    @staticmethod
    def ring_cost(c_idx: int, prev_idx: int, length: int) -> int:
        """Takes two indices and the length of the ring and returns the ring distance + 1"""
        if c_idx < prev_idx:
            lesser, greater = c_idx, prev_idx
        else:
            greater, lesser = c_idx, prev_idx
        return min(abs(c_idx - prev_idx), lesser + (length - greater)) + 1

    def naive(self, ring: str, key: str) -> int:
        """This one actually times out. It needs a good implementation of Dynamic Programming/Backtracking"""
        counts = defaultdict(set)
        for idx in range(0, len(ring)):
            counts[ring[idx]].add(idx)

        def _recurse(key_index, count, current_index):
            # Stop when key_index == last index
            if key_index < len(key) - 1:
                next_letter = key[key_index + 1]
                if next_letter == ring[current_index]:
                    _recurse(key_index + 1, count + 1, current_index)
                else:
                    for next_index in counts[next_letter]:
                        direct = abs(current_index - next_index)
                        if current_index < next_index:
                            lesser, greater = current_index, next_index
                        else:
                            greater, lesser = current_index, next_index
                        loop = lesser + ((len(ring)) - greater)
                        # The best way to get to the next_index
                        steps = min(direct, loop)
                        # Add travel time and cost to add the new character
                        new_count = count + steps + 1
                        # Advance to the next key item at the location of the current letter
                        _recurse(key_index + 1, new_count, next_index)
            else:
                self.best = min(count, self.best)

        self.best = float('inf')
        _recurse(-1, 0, 0)
        return self.best
