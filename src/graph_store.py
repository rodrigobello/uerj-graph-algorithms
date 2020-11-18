from src.adjacency_matrix_factory import AdjacencyMatrixFactory
from src import constants as C
from os import listdir
from os.path import isfile, join

class GraphStore:
    graph_store_path = './store'
    adjacency_matrices = {}
    factory = AdjacencyMatrixFactory()

    def print_adjacency_matrix(self, graph_name):
        adjacency_matrix = self.adjacency_matrices.get(graph_name)
        if not adjacency_matrix:
            raise self.GraphDoesNotExist()
        print(f"Matriz de adjacência:\n{adjacency_matrix}")

    def print_number_of_connected_components(self, graph_name):
        adjacency_matrix = self.adjacency_matrices.get(graph_name)
        if not adjacency_matrix:
            raise self.GraphDoesNotExist()
        print(f"Número de componentes conexas: {adjacency_matrix.number_of_connected_components}")

    def print_vertex_coloring_by_greedy_algorithm(self, graph_name):
        adjacency_matrix = self.adjacency_matrices.get(graph_name)
        if not adjacency_matrix:
            raise self.GraphDoesNotExist()
        vertex_coloring = adjacency_matrix.vertex_coloring
        used_colors = max(vertex_coloring) + 1
        print(f"Vetor de coloração utilizando {used_colors} cores: {vertex_coloring}")

    def print_has_eulerian_path(self, graph_name):
        adjacency_matrix = self.adjacency_matrices.get(graph_name)
        if not adjacency_matrix:
            raise self.GraphDoesNotExist()
        has_eulerian_path = adjacency_matrix.has_eulerian_path
        print(f"Euleriano: {'Sim' if has_eulerian_path else 'Não'}")

    def save_adjacency_matrix_from_upper_triangle(self, graph_name, n, upper_triangle):
        adjacency_matrix = self.factory.build_matrix_from_upper_triangle(n, upper_triangle)
        self.adjacency_matrices[graph_name] = adjacency_matrix
        with open(f'{self.graph_store_path}/{graph_name}.txt', 'w+') as fp:
            fp.write(str(adjacency_matrix))

    def save_special_class_graph(self, class_name, n):
        graph_size = f'n{n}'
        if class_name == C.COMPLETE_GRAPH:
            adjacency_matrix = self.factory.build_matrix_for_complete_graph(n)
        elif class_name == C.STAR_GRAPH:
            adjacency_matrix = self.factory.build_matrix_for_star_graph(n)
        elif class_name == C.CYCLE_GRAPH:
            adjacency_matrix = self.factory.build_matrix_for_cycle_graph(n)
        elif class_name == C.WHEEL_GRAPH:
            adjacency_matrix = self.factory.build_matrix_for_wheel_graph(n)
        elif class_name == C.PATH_GRAPH:
            adjacency_matrix = self.factory.build_matrix_for_path_graph(n)
        elif class_name == C.HYPERCUBE_GRAPH:
            adjacency_matrix = self.factory.build_matrix_for_hypercube_graph(n)
        elif class_name == C.COMPLETE_BIPARTITE_GRAPH:
            adjacency_matrix = self.factory.build_matrix_for_complete_bipartite_graph(n)
            graph_size = f'n{n[0]},{n[1]}'
        elif class_name == C.MYCIELSKI_GRAPH:
            adjacency_matrix = self.factory.build_matrix_for_mycielski_graph(n)
            graph_size = f'omega{n[0]},chi{n[1]}'
        else:
            raise self.SpecialGraphClassDoesNotExist()

        graph_name = dict(C.SPECIAL_CLASS_GRAPH_NAMES)[class_name] % graph_size
        self.adjacency_matrices[graph_name] = adjacency_matrix
        with open(f'{self.graph_store_path}/{graph_name}.txt', 'w+') as fp:
            fp.write(str(adjacency_matrix))
        return graph_name

    def load_matrices_from_store(self):
        files = [f for f in listdir(self.graph_store_path) if isfile(join(self.graph_store_path, f))]
        for graph_file in files:
            with open(f'{self.graph_store_path}/{graph_file}', 'r+') as fp:
                lines = fp.readlines()
            graph_name = graph_file.replace('.txt','')
            adjacency_matrix = self.factory.build_matrix_from_rows(lines)
            self.adjacency_matrices[graph_name] = adjacency_matrix

    class GraphDoesNotExist(Exception):
        pass

    class SpecialGraphClassDoesNotExist(Exception):
        pass
