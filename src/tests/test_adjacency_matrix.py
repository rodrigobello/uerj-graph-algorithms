from unittest import TestCase
from src.adjacency_matrix import AdjacencyMatrix


class AdjacencyMatrixTestCase(TestCase):
    maxDiff = None

    def test_fill_adjacency_matrix_main_diagonal(self):
        M = AdjacencyMatrix(3)
        M.fill_main_diagonal()
        expected_matrix = [[0, None, None], [None, 0, None], [None, None, 0]]
        self.assertEqual(M.matrix, expected_matrix)

    def test_set_upper_triangle(self):
        M = AdjacencyMatrix(5)
        M.set_upper_triangle([1, 1, 0, 1, 1, 0, 0, 1, 0, 1])
        expected_matrix = [
            [None, 1, 1, 0, 1],
            [None, None, 1, 0, 0],
            [None, None, None, 1, 0],
            [None, None, None, None, 1],
            [None, None, None, None, None],
        ]
        self.assertEqual(M.matrix, expected_matrix)

    def test_fill_lower_triangle(self):
        M = AdjacencyMatrix(3)
        M.matrix = [[0, 1, 0], [None, 0, 1], [None, None, 0]]
        M.fill_lower_triangle()
        expected_matrix = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        self.assertEqual(M.matrix, expected_matrix)

    def test_get_neighbors(self):
        M = AdjacencyMatrix(4)
        M.matrix = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
        self.assertEqual(M.get_neighbors(0), [1, 2, 3])
        self.assertEqual(M.get_neighbors(1), [0, 2])
        self.assertEqual(M.get_neighbors(2), [0, 1])
        self.assertEqual(M.get_neighbors(3), [0])

    def test_bfs(self):
        M = AdjacencyMatrix(9)
        M.matrix = [
            [0, 1, 1, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 0, 1, 1],
            [0, 1, 0, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 1, 0]
        ]
        reachability_tree = M.bfs(8)
        self.assertEqual(
            reachability_tree,
            {
                8: { 'parent': None, 'discovery_time': 0 },
                4: { 'parent': 8, 'discovery_time': 1 },
                5: { 'parent': 8, 'discovery_time': 1 },
                6: { 'parent': 8, 'discovery_time': 1 },
                7: { 'parent': 8, 'discovery_time': 1 },
                0: { 'parent': 7, 'discovery_time': 2 },
                1: { 'parent': 6, 'discovery_time': 2 },
                2: { 'parent': 5, 'discovery_time': 2 },
                3: { 'parent': 4, 'discovery_time': 2 }
            }
        )

    def test_number_of_connected_components(self):
        M = AdjacencyMatrix(9)
        M.matrix = [
            [0, 1, 1, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 0, 1, 1],
            [0, 1, 0, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 1, 0]
        ]
        self.assertEqual(M.number_of_connected_components, 1)

        M = AdjacencyMatrix(4)
        M.matrix = [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ]
        self.assertEqual(M.number_of_connected_components, 2)

        M = AdjacencyMatrix(5)
        M.matrix = [
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(M.number_of_connected_components, 3)

    def test_greedy_coloring(self):
        M = AdjacencyMatrix(5)
        M.matrix = [
            [0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1],
            [1, 1, 0, 1, 0],
        ]
        self.assertEqual(M.vertex_coloring, [0, 1, 0, 1, 2])

    def test_has_eulerian_path(self):
        M1 = AdjacencyMatrix(7)
        M1.matrix = [
            [0, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 0],
        ]
        self.assertFalse(M1.has_eulerian_path)

        M2 = AdjacencyMatrix(4)
        M2.matrix = [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ]
        self.assertTrue(M2.has_eulerian_path)

        M3 = AdjacencyMatrix(3)
        M3.matrix = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0],
        ]
        self.assertTrue(M3.has_eulerian_path)

    def test_adjacency_matrix_is_caching_properties(self):
        M = AdjacencyMatrix(7)
        M.matrix = [
            [0, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 0],
        ]
        self.assertEqual(M.number_of_connected_components, 2)
        self.assertFalse(M.has_eulerian_path)
        self.assertEqual(M.vertex_coloring, [0, 1, 1, 0, 0, 1, 2])

        M.matrix = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0],
        ]

        self.assertEqual(M.number_of_connected_components, 2)
        self.assertFalse(M.has_eulerian_path)
        self.assertEqual(M.vertex_coloring, [0, 1, 1, 0, 0, 1, 2])
