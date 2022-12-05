# Simulador de dados
# Simular o uso de um dado gerando um valor de 1 até 6


import random
import PySimpleGUI as sg


class SimuladorDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você Gostaria de jogar?'
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # Ler os valor da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com os valores
        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Não será gerado seu número, até logo!')
            else:
                print('Digite apenas s ou n!')
        except:
            print('Ocorreu um erro ao receber sua resposta, tente novamente!')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDado()
simulador.Iniciar()
