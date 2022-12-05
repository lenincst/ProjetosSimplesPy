# Faça uma pergunta para o programa e ele responde para você

import random
import PySimpleGUI as sg


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza você deve fazer isso',
            'Não sei, você que sabe',
            'Não faz isso',
            'Acho que está na hora certa'
        ]

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(20, 10))],
            [sg.Button('Decida por mim')]
        ]
        # Criar janela
        self.janela = sg.Window('Decida por mim!', layout=layout)

        while True:
            # Ler os Valores
            self.eventos, self.valores = self.janela.read()

            # Faça algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))


decida = DecidaPorMim()
decida.Iniciar()
