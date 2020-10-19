#!/usr/bin/env python3
from src.app import App


if __name__ == '__main__':
    app = App()
    try:
        app.run()
    except Exception as e:
        print(f'ERRO: {e}')
