from collections import defaultdict


class Solution:
    def containVirus(self, grid: list[list[int]]) -> int:
        pass


class Graph:
    def __init__(self, grid):
        self.nodes = {}
        self.walls = 0
        self.representative_infected_nodes = []

        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                self.nodes[(x, y)] = Node(x, y, grid, self)

    def assess(self):
        queue = set(self.nodes.keys())
        while queue:
            node = self.nodes[queue.pop()]
            if node.infected:
                self.representative_infected_nodes.append(node)
                queue = queue ^ node.zone
        most_threatened = 0
        most_threatening = None
        for node in self.representative_infected_nodes:
            if len(node.threatening) > most_threatened:
                most_threatening = node
                most_threatened = len(node.threatening)
        return most_threatening


class Node:
    def __init__(self, x, y, grid, graph):
        self.x = x
        self.y = y
        self.infected = bool(grid[y][x])
        self.adjacent = set()
        if 1 <= y < len(grid):
            self.adjacent.add((x, y - 1))
        if 0 <= y < len(grid) - 1:
            self.adjacent.add((x, y + 1))
        if 1 <= y < len(grid):
            self.adjacent.add((x - 1, y))
        if 0 <= y < len(grid) - 1:
            self.adjacent.add((x + 1, y))
        self.zone = {(x, y)}
        self.threatening = defaultdict(set)
        if self.infected:
            for adj_x, adj_y in self.adjacent:
                if not grid[adj_y][adj_x]:
                    self.threatening.add((adj_x, adj_y))
                else:
                    adj_inf = graph[(adj_x, adj_y)]
                    adj_inf.zone = self.zone = self.zone | adj_inf.zone
                    adj_inf.treatening = self.threatening = self.threatening | adj_inf.threatening

        graph.nodes[(x, y)] = self
