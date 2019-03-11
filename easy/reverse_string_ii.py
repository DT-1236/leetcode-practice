class Solution:
    def reverseStr(self, input_string: str, num: int) -> str:
        """Returns a string where num characters have been reversed every num * 2 places"""
        output = ''
        for rng in range(0, len(input_string), 2 * num):
            rev = input_string[rng + num - 1:rng - 1 if rng else None:-1]
            fwd = input_string[rng + num:rng + (2 * num)]
            output += rev + fwd
        return output
