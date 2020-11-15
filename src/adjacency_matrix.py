import random


class AdjacencyMatrix:
    def __init__(self, n):
        self.matrix = [[None for _ in range(n)] for _ in range(n)]

    @property
    def n(self):
        return len(self.matrix)

    def set_upper_triangle(self, upper_m):
        for i in range(self.n - 1):
            for j in range(i + 1, self.n):
                self.matrix[i][j] = upper_m.pop(0)

    def fill_lower_triangle(self):
        for i in range(1, self.n):
            for j in range(i):
                self.matrix[i][j] = self.matrix[j][i]

    def fill_main_diagonal(self):
        for i in range(self.n):
            self.matrix[i][i] = 0

    @property
    def number_of_connected_components(self):
        number_of_connected_components = 0
        nodes = list(range(self.n))
        while nodes:
            reachability_tree = self.bfs(random.choice(nodes))
            number_of_connected_components += 1
            nodes = list(set(nodes) - set(reachability_tree.keys()))
        return number_of_connected_components

    @property
    def vertex_coloring(self):
        return self.greedy_coloring()

    def bfs(self, node_index):
        queue = []
        reachability_tree = {
            node:{ 'parent': None, 'color': 'WHITE', 'discovery_time': -1 }
            for node in range(self.n)
        }
        reachability_tree[node_index].update({
            'color': 'GRAY',
            'discovery_time': 0
        })
        queue.append(node_index)
        while queue:
            dequeued_node = queue.pop(0)
            for neighbor_node in self.get_neighbors(dequeued_node):
                if reachability_tree[neighbor_node]['color'] == 'WHITE':
                    reachability_tree[neighbor_node] = {
                        'parent': dequeued_node,
                        'color': 'GRAY',
                        'discovery_time': reachability_tree[dequeued_node]['discovery_time'] + 1
                    }
                    queue.append(neighbor_node)
            reachability_tree[dequeued_node]['color'] = 'BLACK'
        return {
            k:{'parent': v['parent'], 'discovery_time': v['discovery_time']}
            for k, v in reachability_tree.items()
            if v['color'] == 'BLACK'
        }

    def greedy_coloring(self):
        colors = [-1 for _ in range(self.n)]
        colors[0] = 0
        for node in range(1, self.n):
            used_colors = set([colors[x] for x in self.get_neighbors(node)])
            node_color = 0
            while node_color in used_colors:
                node_color += 1
            colors[node] = node_color
        return colors

    def get_neighbors(self, node_index):
        return [
            index for index, edges in enumerate(self.matrix[node_index])
            if edges
        ]

    def __str__(self):
        return '\n'.join(' '.join(map(str,sl)) for sl in self.matrix)
