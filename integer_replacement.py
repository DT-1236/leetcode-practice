class Solution:
    def integerReplacement(self, n: int) -> int:
        print("Disgusting", self.disgusting_solution(n))
        count = 0
        path = [n]
        while n != 1:
            if n % 2:
                if n < 10:
                    n -= 1
                elif len(bin(n + 1)[bin(n + 1).rfind('1'):]) > len(
                        bin(n - 1)[bin(n - 1).rfind('1'):]):
                    n += 1
                else:
                    n -= 1
            else:
                n //= 2
            count += 1
            path.append(n)
        print("bin-style", path)
        return count

    def disgusting_solution(self, n):
        self.best = float('inf')
        self.paths = None

        def _iterate(num, count, path):
            path = path + [num]
            if num == 1:
                if count < self.best:
                    self.best = count
                    self.paths = set([tuple(path)])
                elif count == self.best:
                    self.paths.add(tuple(path))

            elif count < self.best:
                if num % 2:
                    _iterate(num + 1, count + 1, path)
                    _iterate(num - 1, count + 1, path)

                else:
                    _iterate(num // 2, count + 1, path)

        _iterate(n, 0, [])
        print(self.paths)
        return self.best