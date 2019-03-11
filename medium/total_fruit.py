class Solution:
    def totalFruit(self, tree: [int]) -> int:
        if not tree:
            return 0
        max_fruits = 1
        current = 1
        seen = [tree[0]]
        left = 0
        for idx in range(1, len(tree)):
            if tree[idx] != seen[-1]:
                # A 2nd value is seen
                if len(seen) < 2:
                    seen.append(tree[idx])
                # Value is the other value, so just make it the most recent value
                elif tree[idx] == seen[0]:
                    seen[0], seen[1] = seen[1], seen[0]
                # Value is entirely new
                else:
                    # Replace the older value with the new value
                    seen[0], seen[1] = seen[1], tree[idx]
                    max_fruits = max(current, max_fruits)
                    current = idx - left
                left = idx
            current += 1
        return max(current, max_fruits)

    def naive(self, tree: [int]) -> int:
        max_fruits = 0
        current = 0
        # Will contain 2 letters and their last seen index
        seen = {}
        for idx in range(0, len(tree)):
            if tree[idx] not in seen:
                if len(seen) < 2:
                    seen[tree[idx]] = idx
                    current += 1
                else:
                    max_fruits = max(current, max_fruits)
                    other_type = next(
                        x for x in seen.keys() if x != tree[idx - 1])
                    current = idx - seen[other_type] - 1
                    del seen[other_type]
                    seen[tree[idx]] = idx
                    current += 1
            elif tree[idx] in seen:
                seen[tree[idx]] = idx
                current += 1

        return max(current, max_fruits)
