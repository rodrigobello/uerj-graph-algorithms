from unittest import TestCase
from src.adjacency_matrix import AdjacencyMatrix
from src.adjacency_matrix_factory import AdjacencyMatrixFactory


class AdjacencyMatrixFactoryTestCase(TestCase):
    maxDiff = None

    def setUp(self):
        self.factory = AdjacencyMatrixFactory()

    def test_build_matrix_from_upper_triangle(self):
        M = self.factory.build_matrix_from_upper_triangle(5, [1, 1, 0, 1, 1, 0, 0, 1, 0, 1])
        self.assertIsInstance(M, AdjacencyMatrix)
        expected_matrix = [
            [0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 1, 0],
        ]
        self.assertEqual(M.matrix, expected_matrix)

    def test_build_matrix_from_rows(self):
        M = self.factory.build_matrix_from_rows(['0 1 1', '1 0 1', '1 1 0'])
        self.assertIsInstance(M, AdjacencyMatrix)
        expected_matrix = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0],
        ]
        self.assertEqual(M.matrix, expected_matrix)

    def test_build_matrix_for_hypercube_graph(self):
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_hypercube_graph,
            -1
        )

        Q0 = self.factory.build_matrix_for_hypercube_graph(0)
        self.assertIsInstance(Q0, AdjacencyMatrix)
        self.assertEqual(Q0.matrix, [[0]])

        Q1 = self.factory.build_matrix_for_hypercube_graph(1)
        self.assertIsInstance(Q1, AdjacencyMatrix)
        self.assertEqual(
            Q1.matrix,
            [[0, 1], [1, 0]]
        )

        Q2 = self.factory.build_matrix_for_hypercube_graph(2)
        self.assertIsInstance(Q2, AdjacencyMatrix)
        expected_matrix = [
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0],
        ]
        self.assertEqual(Q2.matrix, expected_matrix)

        Q3 = self.factory.build_matrix_for_hypercube_graph(3)
        self.assertIsInstance(Q3, AdjacencyMatrix)
        expected_matrix = [
            [0, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 0],
        ]
        self.assertEqual(Q3.matrix, expected_matrix)

    def test_build_matrix_for_path_graph(self):
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_path_graph,
            0
        )

        P1 = self.factory.build_matrix_for_path_graph(1)
        self.assertIsInstance(P1, AdjacencyMatrix)
        self.assertEqual(P1.matrix, [[0]])

        P2 = self.factory.build_matrix_for_path_graph(2)
        self.assertIsInstance(P2, AdjacencyMatrix)
        self.assertEqual(
            P2.matrix,
            [[0, 1], [1, 0]]
        )
        P3 = self.factory.build_matrix_for_path_graph(3)
        self.assertIsInstance(P3, AdjacencyMatrix)
        self.assertEqual(P3.matrix,[
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ])
        P4 = self.factory.build_matrix_for_path_graph(4)
        self.assertIsInstance(P4, AdjacencyMatrix)
        self.assertEqual(P4.matrix,[
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
        ])
        P5 = self.factory.build_matrix_for_path_graph(5)
        self.assertIsInstance(P5, AdjacencyMatrix)
        self.assertEqual(P5.matrix,[
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0],
        ])

    def test_build_matrix_for_cycle_graph(self):
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_cycle_graph,
            1
        )
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_cycle_graph,
            2
        )
        C3 = self.factory.build_matrix_for_cycle_graph(3)
        self.assertIsInstance(C3, AdjacencyMatrix)
        self.assertEqual(C3.matrix,[
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0],
        ])
        C4 = self.factory.build_matrix_for_cycle_graph(4)
        self.assertIsInstance(C4, AdjacencyMatrix)
        self.assertEqual(C4.matrix,[
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0],
        ])
        C5 = self.factory.build_matrix_for_cycle_graph(5)
        self.assertIsInstance(C5, AdjacencyMatrix)
        self.assertEqual(C5.matrix,[
            [0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 1, 0],
        ])

    def test_build_matrix_for_wheel_graph(self):
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_wheel_graph,
            1
        )
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_wheel_graph,
            2
        )
        W3 = self.factory.build_matrix_for_wheel_graph(3)
        self.assertIsInstance(W3, AdjacencyMatrix)
        self.assertEqual(W3.matrix,[
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0],
        ])
        W4 = self.factory.build_matrix_for_wheel_graph(4)
        self.assertIsInstance(W4, AdjacencyMatrix)
        self.assertEqual(W4.matrix,[
            [0, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 0],
        ])
        W5 = self.factory.build_matrix_for_wheel_graph(5)
        self.assertIsInstance(W5, AdjacencyMatrix)
        self.assertEqual(W5.matrix,[
            [0, 1, 0, 0, 1, 1],
            [1, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 0],
        ])

    def test_build_matrix_for_complete_graph(self):
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_complete_graph,
            0
        )

        K1 = self.factory.build_matrix_for_complete_graph(1)
        self.assertIsInstance(K1, AdjacencyMatrix)
        self.assertEqual(K1.matrix, [[0]])

        K2 = self.factory.build_matrix_for_complete_graph(2)
        self.assertIsInstance(K2, AdjacencyMatrix)
        self.assertEqual(
            K2.matrix,
            [[0, 1], [1, 0]]
        )

        K3 = self.factory.build_matrix_for_complete_graph(3)
        self.assertIsInstance(K3, AdjacencyMatrix)
        self.assertEqual(K3.matrix,[
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0],
        ])

        K4 = self.factory.build_matrix_for_complete_graph(4)
        self.assertIsInstance(K4, AdjacencyMatrix)
        self.assertEqual(K4.matrix,[
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0],
        ])

        K5 = self.factory.build_matrix_for_complete_graph(5)
        self.assertIsInstance(K5, AdjacencyMatrix)
        self.assertEqual(K5.matrix,[
            [0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0],
        ])

    def test_build_matrix_for_complete_bipartite_graph(self):
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_complete_bipartite_graph,
            1
        )
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_complete_bipartite_graph,
            (1,)
        )
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_complete_bipartite_graph,

            (0, 1)
        )
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_complete_bipartite_graph,
            (1, 0)
        )
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_complete_bipartite_graph,
            (0, 0)
        )
        K1_1 = self.factory.build_matrix_for_complete_bipartite_graph([1, 1])
        self.assertIsInstance(K1_1, AdjacencyMatrix)
        self.assertEqual(
            K1_1.matrix,
            [[0, 1], [1, 0]]
        )

        K1_2 = self.factory.build_matrix_for_complete_bipartite_graph([1, 2])
        self.assertIsInstance(K1_1, AdjacencyMatrix)
        self.assertEqual(K1_2.matrix,[
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ])

        K2_1 = self.factory.build_matrix_for_complete_bipartite_graph([2, 1])
        self.assertIsInstance(K2_1, AdjacencyMatrix)
        self.assertEqual(K2_1.matrix,[
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ])

        K2_2 = self.factory.build_matrix_for_complete_bipartite_graph([2, 2])
        self.assertIsInstance(K2_2, AdjacencyMatrix)
        self.assertEqual(K2_2.matrix,[
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
        ])

        K2_3 = self.factory.build_matrix_for_complete_bipartite_graph([2, 3])
        self.assertIsInstance(K2_3, AdjacencyMatrix)
        self.assertEqual(K2_3.matrix,[
            [0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
        ])

        K3_2 = self.factory.build_matrix_for_complete_bipartite_graph([3, 2])
        self.assertIsInstance(K3_2, AdjacencyMatrix)
        self.assertEqual(K3_2.matrix,[
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
        ])

        K3_3 = self.factory.build_matrix_for_complete_bipartite_graph([3, 3])
        self.assertIsInstance(K3_3, AdjacencyMatrix)
        self.assertEqual(K3_3.matrix,[
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
        ])

    def test_build_matrix_for_star_graph(self):
        self.assertRaises(
            self.factory.InvalidMatrixParameter,
            self.factory.build_matrix_for_star_graph,
            0
        )

        S1 = self.factory.build_matrix_for_star_graph(1)
        self.assertIsInstance(S1, AdjacencyMatrix)
        self.assertEqual(S1.matrix,[
            [0, 1],
            [1, 0],
        ])

        S2 = self.factory.build_matrix_for_star_graph(2)
        self.assertIsInstance(S2, AdjacencyMatrix)
        self.assertEqual(S2.matrix,[
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ])

        S3 = self.factory.build_matrix_for_star_graph(3)
        self.assertIsInstance(S3, AdjacencyMatrix)
        self.assertEqual(S3.matrix,[
            [0, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
        ])

        S4 = self.factory.build_matrix_for_star_graph(4)
        self.assertIsInstance(S4, AdjacencyMatrix)
        self.assertEqual(S4.matrix,[
            [0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
        ])
