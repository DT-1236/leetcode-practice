from collections import defaultdict


class Solution:
    def containVirus(self, grid: list[list[int]]) -> int:
        pass


class Graph:
    def __init__(self, grid):
        self.nodes = {}
        self.walls = 0

        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                self.nodes[(x, y)] = Node(x, y, grid, self)

    def get_representative_infected_nodes(self):
        """Returns a representative node of the most threatening area"""
        queue = set(self.nodes.keys())
        representative_infected_nodes = []
        while queue:
            node = self.nodes[queue.pop()]
            if node.infected:
                representative_infected_nodes.append(node)
                queue = queue ^ node.zone
        return representative_infected_nodes

    @staticmethod
    def find_most_threatening_zone(representative_nodes):
        most_threatening = None
        for node in representative_nodes:
            if len(node.threatening) > len(most_threatened.threatening):
                most_threatening = node
        return most_threatening

    def build_walls(self, node):
        """The node is a representative infected node for that zone"""
        queue = node.threatening
        while queue:
            safe = nodes[queue.pop()]
            for coords in safe.adjacent:
                neighbor = self.nodes[coords]
                if neighbor.infected:
                    safe.adjacent.remove(coords)
                    neighbor.adjacent.remove((safe.x, safe.y))
                    self.walls += 1

    def propagate_virus(self, infected):
        for node in infected:
            pass


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
