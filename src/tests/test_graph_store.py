import io
import sys
from unittest import TestCase, mock
from src.graph_store import GraphStore
from src import constants as C


class GraphStoreTestCase(TestCase):
    def setUp(self):
        self.store = GraphStore()
        self.store.adjacency_matrices = {'foo': 'bar'}

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_adjacency_matrix_will_not_raise_exception_if_graph_exists(self, mock_stdout):
        self.store.print_adjacency_matrix('foo')
        self.assertEqual(mock_stdout.getvalue(), "Matriz de adjacência:\nbar\n")

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_number_of_connected_components_will_not_raise_exception_if_graph_exists(self, mock_stdout):
        M = mock.Mock()
        M.number_of_connected_components = 4
        self.store.adjacency_matrices['mock'] = M
        self.store.print_number_of_connected_components('mock')
        self.assertEqual(mock_stdout.getvalue(), "Número de componentes conexas: 4\n")

    def test_print_matrix_will_raise_exception(self):
        self.assertRaises(GraphStore.GraphDoesNotExist, self.store.print_adjacency_matrix, 'random')
        self.assertRaises(GraphStore.GraphDoesNotExist, self.store.print_number_of_connected_components, 'random')

    def test_save_adjacency_matrix_from_upper_triangle(self):
        self.store.save_adjacency_matrix_from_upper_triangle('mock', 5, [1, 1, 0, 1, 1, 0, 0, 1, 0, 1])
        M = self.store.adjacency_matrices['mock']
        expected_matrix = [
            [0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 1, 0],
        ]
        self.assertEqual(M.matrix, expected_matrix)
