from collections import deque

def naive_solution(senate: str) -> str:
    '''Making it a list first and mutating the list as we go'''
    if not senate:
        return "The senate is empty"
    senate = list(senate)
    control = senate[0]
    seen = {"D": True, "R": True}
    stack = []
    while seen["D"] and seen["R"]:
        seen = {"D": False, "R": False}
        for index in range(len(senate)):
            letter = senate[index]
            if letter == "B":
                continue
            elif letter == control:
                stack.append(letter)
                seen[letter] = True
            elif stack:
                stack.pop()
                senate[index] = "B"
            else:
                stack = [letter]
                control = letter
                seen[letter] = True

    return 'Radiant' if seen["R"] else 'Dire'


def model_solution(senate):
    queue = deque()
    members = {'R': 0, 'L': 0}
    bans = {'R': 0, 'L': 0}
    control = senate[0]
    stack = [senate[0]]
    for letter in senate:
        queue.append(letter)
        members[letter] += 1
    while members['R'] and members['L']:
        floor = queue.popleft()
        other = 'R' if floor == 'L' else 'L'
        if bans[other]:
            bans[other] -= 1
            members[floor] -= 1
        else:
            bans[floor] += 1
            queue.append(floor)
    return 'Radiant' if members['R'] else 'Dire'