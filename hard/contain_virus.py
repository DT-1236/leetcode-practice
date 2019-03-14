from collections import defaultdict
from typing import List, NewType


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
            graph.infected.add((x, y))
            for adj_x, adj_y in self.adjacent:
                if not grid[adj_y][adj_x]:
                    self.threatening.add((adj_x, adj_y))
                else:
                    adj_inf = graph[(adj_x, adj_y)]
                    adj_inf.zone.update(self.zone)
                    self.zone = adj_inf.zone
                    adj_inf.threatening.update(self.threatening)
                    self.threatening = adj_inf.threatening

        graph.nodes[(x, y)] = self


GraphNode = NewType('GraphNode', Node)


class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        pass


class Graph:
    def __init__(self, grid: List[List[int]]):
        self.nodes = {}
        self.infected = {}
        self.walls = 0
        self.grid = grid

        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                self.nodes[(x, y)] = Node(x, y, grid, self)

    def get_representative_infected_nodes(self) -> list[GraphNode]:
        """Returns a representative node of the most threatening area"""
        queue = set(self.nodes.keys())
        representative_infected_nodes = []
        while queue:
            node = self.nodes[queue.pop()]
            if node.infected:
                representative_infected_nodes.append(node)
                # Remove all nodes that are in the infected zone
                queue = queue ^ node.zone
        return representative_infected_nodes

    @staticmethod
    def find_most_threatening_zone(
            representative_nodes: List[GraphNode]) -> Node:
        most_threatening = None
        for node in representative_nodes:
            if len(node.threatening) > len(most_threatening.threatening):
                most_threatening = node
        return most_threatening

    def build_walls(self, node: GraphNode) -> None:
        """The node is a representative infected node for that zone
        Since the zone will no longer propagate, the set can be mutated"""
        queue = node.threatening
        while queue:
            safe = self.nodes[queue.pop()]
            for coords in safe.adjacent:
                neighbor = self.nodes[coords]
                if neighbor.infected:
                    safe.adjacent.remove(coords)
                    neighbor.adjacent.remove((safe.x, safe.y))
                    self.walls += 1
        self.infected.difference_update(node.zone)

    def propagate_virus(self, infected: List[GraphNode]):
        for representative_node in infected:
            threatening = representative_node.threatening
            zone = representative_node.zone
            queue = threatening.copy()
            threatening.clear()
            for x, y in queue:
                node = self.nodes[(x, y)]
                node.infected = True
                self.grid[y][x] = 1
                zone.add((x, y))
                node.zone = zone
                # Will filter out infected and threatened nodes later
                threatening.update(node.adjacent)
            # This removes infected nodes from threatened status
            threatening.difference_update(zone)
        # Now if nodes are threatened and also in a zone, it triggers a merge
        # Merge infected

    def merge_adjacent(self, infected: List[GraphNode]) -> None:
        for representative_node in infected:
            threatened_coords = representative_node.threatened
            for threat_x, threat_y in threatened_coords:
                if (threat_x, threat_y) in self.infected:
                    # Trigger merge
                    zone1 = representative_node.zone
                    merge_queue = self.nodes[(threat_x, threat_y)].zone.copy()
                    zone1.update()
