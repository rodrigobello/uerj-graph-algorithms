#!/usr/bin/env python3
from src.app import App


if __name__ == '__main__':
    app = App()
    print("ALGORITMOS EM GRAFOS - ALUNO: RODRIGO ABREU BELLO")
    print("Programa desenvolvido para a disciplina de Algoritmos em Grafos, ministrada pelo professor Luerbio Faria.")
    print("(Para sair do programa, pressione CTRL-C)")
    print("\n")
    try:
        app.run()
    except KeyboardInterrupt as e:
        print('\n-- PROGRAMA INTERROMPIDO (CTRL-C) --')
    except Exception as e:
        print(f'ERRO: {e}')
