from collections import deque


class Solution:
    @staticmethod
    def stack_to_string(stack: deque) -> str:
        output_string = ''
        string_stack = deque()
        for item in stack:
            string_stack.appendleft(item)
            output_string += '('
        while string_stack:
            current = string_stack.popleft()
            # Put any nested parenthesis on the stack. Nested parens will resolve first
            while current:
                string_stack.appendleft(current.popleft())
                output_string += '('
            output_string += ')'
        return output_string

    def generateParenthesis(self, n: int) -> [str]:
        '''For all permutations,
        Create a stack. Generate strings based on the stack. Stack items are additional stacks. Each stack is a set of parens'''
        string_stack = deque()
        current_stack = deque()


1 => [‘( )’]
2 => [‘( ) ( )’, ‘( ( ) )’]
3 => [‘( ( ( ) ) )’, ‘( ) ( ( ) )’, ‘( ( ) ) ( )’, ‘( ) ( ) ( )’]
