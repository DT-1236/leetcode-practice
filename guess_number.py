from pprint import pprint
'''
10 => 16 // 07, 09
11 => 18 // 08, 10

11 => 18 // 08, 04, 06
12 => 21 // 09, 05, 07
13 => 24 // 10, 06, 08
14 => 27 // 11, 07, 09
15 => 30 // 12, 08, 10

15 => 30 // 12, 08, 04, 06
16 => 34 // 13, 09, 05, 07
17 => 38 // 14, 10, 06, 08
18 => 42 // 15, 11, 07, 09
19 => 46 // 16, 12, 08, 10

19 => 46 // 16, 12, 18
20 => 49 // 17, 13, 19
21 => 52 // 18, 14, 20

40 => 119
'''


class Solution:
    def getMoneyAmount(self, n: int, verbose=False):
        '''Implement Dynamic Programming to iterate all possible outcomes and determine the minimum cost
        At the lowest level of iteration, selecting a number will split the problem into two subcases - the numbers on the left and the right
        '''
        # Populate known cases. 0 for single number sets, the lesser number for two number sets
        # Indices will be offset by 1, _e.g._ tabulation[3][5] will be the ideal result for number set 2-4
        # Doing it otherwise would result in an unused column/row
        tabulation = [[x if y == x - 1 else 0 for x in range(0, n)]
                      for y in range(0, n)]

        # Starting number. Start high to account for base cases
        for low_val in range(n, 0, -1):
            # Don't need to test single value ranges or two value ranges
            for high_val in range(low_val + 2, n + 1):
                minimum = float('inf')
                # For each value in [low_val, high_val) evaluate all outcomes
                # Since we're trying to minimize cost, the high_val will never be chosen
                for val in range(low_val, high_val):
                    # Add the value of itself as a choice
                    value = val
                    # 'Divide and conquer'. The worst case will be the higher of the two subcases on either side
                    # _e.g._ for range 1-5, if val is 3, then choose the higher cost between the left and right paths (1-2, 3-5)
                    # The process will iterate again, checking val of 4 + the higher cost between 1-3 and 5-5, etc.
                    value += max((tabulation[low_val - 1][val - 2],
                                  tabulation[val][high_val - 1]))

                    # Keep only the best result
                    minimum = min(value, minimum)

                tabulation[low_val - 1][high_val - 1] = minimum
        if verbose:
            pprint(tabulation)
        return tabulation[0][n - 1]
