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
        if not n > 0:
            raise self.InvalidMatrixParameter('Parâmetro inválido! O valor n de Kn deve ser maior que 0.')
        adjacency_matrix = AdjacencyMatrix(n)
        for i in range(n):
            for j in range(len(adjacency_matrix.matrix[i])):
                adjacency_matrix.matrix[i][j] = 1 if i != j else 0
        return adjacency_matrix

    def build_matrix_for_star_graph(self, n):
        try:
            return self.build_matrix_for_complete_bipartite_graph([1, n])
        except self.InvalidMatrixParameter:
            raise self.InvalidMatrixParameter('Parâmetro inválido! O valor n de Sn deve ser maior que 0.')

    def build_matrix_for_complete_bipartite_graph(self, n):
        try:
            n1, n2 = n
            n = n1 + n2
        except Exception:
            raise self.InvalidMatrixParameter('Parâmetro inválido! Os valores n1 e n2 de Kn1,n2 devem ser separados por virgula.')
        if not (n1 > 0 and n2 > 0):
            raise self.InvalidMatrixParameter('Parâmetro inválido! Os valores n1 e n2 de Kn1,n2 devem ser maior que 0.')
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
        if not n > 0:
            raise self.InvalidMatrixParameter('Parâmetro inválido! O valor n de Pn deve ser maior que 0.')
        adjacency_matrix = AdjacencyMatrix(n)
        for i in range(n):
            for j in range(len(adjacency_matrix.matrix[i])):
                condition = bool(i == j + 1 or i == j - 1)
                adjacency_matrix.matrix[i][j] = 1 if condition else 0
        return adjacency_matrix

    def build_matrix_for_cycle_graph(self, n):
        if not n >= 3:
            raise self.InvalidMatrixParameter('Parâmetro inválido! O valor n de Cn deve ser maior ou igual 3.')
        adjacency_matrix = self.build_matrix_for_path_graph(n)
        adjacency_matrix.matrix[n - 1][0] = 1
        adjacency_matrix.matrix[0][n - 1] = 1
        return adjacency_matrix

    def build_matrix_for_wheel_graph(self, n):
        if not n >= 3:
            raise self.InvalidMatrixParameter('Parâmetro inválido! O valor n de Wn deve ser maior ou igual 3.')
        adjacency_matrix = self.build_matrix_for_cycle_graph(n)
        for i in range(n):
            adjacency_matrix.matrix[i].append(1)
        adjacency_matrix.matrix.append([1 if i != n else 0 for i in range(n + 1)])
        return adjacency_matrix

    def build_matrix_for_hypercube_graph(self, n):
        if not n >= 0:
            raise self.InvalidMatrixParameter('Parâmetro inválido! O valor n de Qn deve ser maior ou igual 0.')
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

    def build_matrix_for_mycielski_graph(self, n):
        try:
            omega, chi = n
        except Exception:
            raise self.InvalidMatrixParameter('Parâmetro inválido! Os valores ω e χ de Mω,χ devem ser separados por virgula.')
        if not 2 <= omega <= chi:
            raise self.InvalidMatrixParameter('Parâmetro inválido! Os valores ω e χ de Mω,χ devem respeitar: 2 <= ω <= χ.')
        if omega == chi:
            return self.build_matrix_for_complete_graph(omega)
        previous_mycielsky_graph = self.build_matrix_for_mycielski_graph((omega, chi - 1))

        n = self._get_mycielsky_vertex_count(omega, chi)
        n_without_universal_vertex = n - 1
        adjacency_matrix = AdjacencyMatrix(n)
        limit = n_without_universal_vertex//2

        for row in range(n_without_universal_vertex):
            for col in range(n_without_universal_vertex):
                if row >= limit and col >= limit:
                    adjacency_matrix.matrix[row][col] = 0
                elif row >= limit and col < limit:
                    adjacency_matrix.matrix[row][col] = previous_mycielsky_graph.matrix[row - limit][col]
                elif row < limit and col >= limit:
                    adjacency_matrix.matrix[row][col] = previous_mycielsky_graph.matrix[row][col - limit]
                else:
                    adjacency_matrix.matrix[row][col] = previous_mycielsky_graph.matrix[row][col]

        for row in range(n_without_universal_vertex):
            if row < limit:
                adjacency_matrix.matrix[row][-1] = 0
            else:
                adjacency_matrix.matrix[row][-1] = 1

        for col in range(n):
            adjacency_matrix.matrix[-1][col] = 1 if col >= limit and col != n - 1 else 0

        return adjacency_matrix

    def _get_mycielsky_vertex_count(self, omega, chi):
        if omega == chi:
            return omega
        return 2 * self._get_mycielsky_vertex_count(omega, chi - 1) + 1

    class InvalidMatrixParameter(Exception):
        pass
