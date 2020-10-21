from .graph_store import GraphStore
from src import constants as C


class App:
    graph_store = GraphStore()

    def run(self):
        self.graph_store.load_matrices_from_store()
        while True:
            print("Escolha uma das opções abaixo:")
            print("1 - Carregar um Grafo")
            print("2 - Criar um Grafo")
            print("3 - Gerar grafo das Classes Especiais")
            option = input("Opção (1-3): ")
            if option == '1':
                self.load_graph()
            elif option == '2':
                self.create_graph()
            elif option == '3':
                self.create_special_class_graph()
            else:
                print(f"Opção '{option}' inválida.")
                continue

    def load_graph(self):
        graph_name = input("Digite o nome do grafo: ")
        try:
            self.graph_store.print_adjacency_matrix(graph_name)
            self.graph_store.print_number_of_connected_components(graph_name)
        except self.graph_store.GraphDoesNotExist:
            option = input(f"Ainda não existe um grafo carregado com o nome {graph_name}, gostaria de criar (S/n)? ")
            return self.create_graph(graph_name) if option in ('s', 'S') else exit()

    def create_graph(self, graph_name=None):
        graph_name = graph_name or input("Digite o nome do grafo: ")
        n = int(input(f"Digite a ordem N do grafo '{graph_name}': "))
        upper_triangle = self.load_upper_triangle(n)
        self.graph_store.save_adjacency_matrix_from_upper_triangle(graph_name, n, upper_triangle)
        self.graph_store.print_adjacency_matrix(graph_name)
        self.graph_store.print_number_of_connected_components(graph_name)
        print(f"Grafo '{graph_name}' armazenado com sucesso!")

    def create_special_class_graph(self):
        available_inputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        print("(a) Completo Kn\n(b) Bipartido Completo Kn1,n2\n(c) Estrela Sn\n(d) Ciclo Cn, n>=3\n(e) Roda Wn, n>=3\n(f) Caminho Pn\n(g) Cubo Qn")
        user_input = input("Selecione uma das classes acima (a-g): ")
        try:
            special_class_index = available_inputs.index(user_input)
            class_name = C.SPECIAL_CLASS_GRAPHS[special_class_index]
        except ValueError:
            raise Exception("Opção Inválida!")
        if class_name == C.COMPLETE_BIPARTITE_GRAPH:
            n1_n2 = input(f"Informe o valor de n1 e n2 (separados por virgula, ex: '4,5' para n1 = 4 e n2 = 5): ")
            n = [int(x) for x in n1_n2.split(',')]
        elif class_name in (C.CYCLE_GRAPH, C.WHEEL_GRAPH, C.STAR_GRAPH):
            n = int(input(f"Informe o valor de n (deve ser maior ou igual a 3): "))
        else:
            n = int(input(f"Informe o valor de n: "))
        graph_name = self.graph_store.save_special_class_graph(class_name, n)
        self.graph_store.print_adjacency_matrix(graph_name)
        self.graph_store.print_number_of_connected_components(graph_name)
        print(f"Grafo '{graph_name}' armazenado com sucesso!")

    def load_upper_triangle(self, n):
        print("Escolha uma das opções abaixo para informar a Diagonal Superior da Matriz de Adjacência do grafo:")
        print("1 - Carregar de um Arquivo")
        print("2 - Digitar manualmente")
        answer = input("Opção (1/2): ")
        length = sum(range(n))
        if answer == '1':
            return self._load_upper_triangle_from_file(length)
        elif answer == '2':
            return self._load_upper_triangle_from_user_input(length)
        else:
            raise Exception("Opção Inválida!")

    def _load_upper_triangle_from_file(self, length):
        file_name = input("Digite o nome do arquivo: ")
        with open(file_name) as fp:
            upper_triangle = fp.readlines()
        upper_triangle = [int(i) for i in upper_triangle]
        if len(upper_triangle) != length:
            raise Exception(f"Erro ao carregar Diagonal Superior.\nQuantidade de elementos esperada: {length}\nQuantidade recebida: {len(upper_triangle)}")
        return upper_triangle

    def _load_upper_triangle_from_user_input(self, length):
        elements = input("Digite os elementos da Diagonal Superior separados por espaço (ex. '1 0 1 0 0 1 0 0 1'): ")
        upper_triangle = [int(i) for i in elements.split(' ')]
        if len(upper_triangle) != length:
            raise Exception(f"Erro ao carregar Diagonal Superior.\nQuantidade de elementos esperada: {length}\nQuantidade recebida: {len(upper_triangle)}")
        return upper_triangle
