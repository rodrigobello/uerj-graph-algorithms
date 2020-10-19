from src.adjacency_matrix import AdjacencyMatrix


class AdjacencyMatrixFactory:
    def build_matrix_from_rows(self, rows):
        matrix = []
        for row in rows:
            matrix.append([int(col) for col in row.split(' ')])
        adjacency_matrix = AdjacencyMatrix(len(matrix))
        adjacency_matrix.matrix = matrix
        return adjacency_matrix

    def build_matrix_from_upper_triangle(self, n, upper_triangle):
        adjacency_matrix = AdjacencyMatrix(n)
        adjacency_matrix.fill_main_diagonal()
        adjacency_matrix.set_upper_triangle(upper_triangle)
        adjacency_matrix.fill_lower_triangle()
        return adjacency_matrix

    def build_matrix_for_trivial_graph(self):
        adjacency_matrix = AdjacencyMatrix(1)
        adjacency_matrix.matrix = [[0]]
        return adjacency_matrix

    def build_matrix_for_complete_graph(self, n):
        adjacency_matrix = AdjacencyMatrix(n)
        for i in range(n):
            for j in range(len(adjacency_matrix.matrix[i])):
                adjacency_matrix.matrix[i][j] = 1 if i != j else 0
        return adjacency_matrix

    def build_matrix_for_star_graph(self, n):
        return self.build_matrix_for_complete_bipartite_graph(1, n)

    def build_matrix_for_complete_bipartite_graph(self, n1, n2):
        n = n1 + n2
        if n <= 3:
            return self.build_matrix_for_path_graph(n)
        adjacency_matrix = AdjacencyMatrix(n)
        for i in range(n):
            for j in range(len(adjacency_matrix.matrix[i])):
                if i < n1 and j < n1:
                    adjacency_matrix.matrix[i][j] = 0
                elif i >= n1 and j < n1:
                    adjacency_matrix.matrix[i][j] = 1
                elif i >= n1 and j >= n1:
                    adjacency_matrix.matrix[i][j] = 0
                else:
                    adjacency_matrix.matrix[i][j] = 1
        return adjacency_matrix

    def build_matrix_for_path_graph(self, n):
        adjacency_matrix = AdjacencyMatrix(n)
        for i in range(n):
            for j in range(len(adjacency_matrix.matrix[i])):
                condition = bool(i == j + 1 or i == j - 1)
                adjacency_matrix.matrix[i][j] = 1 if condition else 0
        return adjacency_matrix

    def build_matrix_for_cycle_graph(self, n):
        if n < 3:
            raise self.InvalidMatrixParameter()
        adjacency_matrix = self.build_matrix_for_path_graph(n)
        adjacency_matrix.matrix[n - 1][0] = 1
        adjacency_matrix.matrix[0][n - 1] = 1
        return adjacency_matrix

    def build_matrix_for_wheel_graph(self, n):
        if n < 4:
            raise self.InvalidMatrixParameter()
        adjacency_matrix = self.build_matrix_for_cycle_graph(n - 1)
        for i in range(n - 1):
            adjacency_matrix.matrix[i].append(1)
        adjacency_matrix.matrix.append([1 if i != n - 1 else 0 for i in range(n)])
        return adjacency_matrix

    def build_matrix_for_hypercube_graph(self, n):
        if n == 0:
            return self.build_matrix_for_trivial_graph()
        previous_hyper_cube = self.build_matrix_for_hypercube_graph(n - 1)
        adjacency_matrix = AdjacencyMatrix(pow(2, n))
        limit = adjacency_matrix.n//2
        for i in range(len(adjacency_matrix.matrix)):
            for j in range(len(adjacency_matrix.matrix[i])):
                if i < limit and j < limit:
                    adjacency_matrix.matrix[i][j] = previous_hyper_cube.matrix[i][j]
                elif i >= limit and j >= limit:
                    adjacency_matrix.matrix[i][j] = previous_hyper_cube.matrix[i - limit][j - limit]
                else:
                    adjacency_matrix.matrix[i][j] = 1 if i + j == adjacency_matrix.n - 1 else 0
        return adjacency_matrix

    class InvalidMatrixParameter(Exception):
        pass